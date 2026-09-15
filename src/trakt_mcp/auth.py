"""Device-code sign-in, kept out of the generated tools.

Trakt's OAuth endpoints are not part of the API contract the tools come from,
and the flow needs state across three calls, so these four are written by hand.

Ref: https://trakt.docs.apiary.io/#reference/authentication-devices
"""

import json
import os
import time

import httpx

from .runtime import (
    _DESTRUCTIVE,
    _READ,
    _WRITE,
    ENV_CLIENT_SECRET,
    TraktError,
    _client,
    _err,
    clear_token,
    client_id,
    load_token,
    mcp,
    store_token,
)


def _ok(data: dict) -> str:
    return json.dumps({"status": "success", **data}, indent=2)


def _client_secret() -> str:
    secret = os.getenv(ENV_CLIENT_SECRET)
    if not secret:
        raise TraktError(
            f"{ENV_CLIENT_SECRET} is not set. It is on the same application "
            "page as the client id, at https://trakt.tv/oauth/applications"
        )
    return secret


@mcp.tool(annotations=_WRITE)
def start_authentication() -> str:
    """Begin signing in to Trakt.

    Returns a short code and a URL. Open the URL, enter the code, then call
    finish_authentication. Only needed for the endpoints that act on an
    account: sync, users/me, checkin, scrobble, recommendations and lists you
    own.
    """
    try:
        response = _client().post(
            "/oauth/device/code", json={"client_id": client_id()}
        )
        response.raise_for_status()
        device = response.json()
        return _ok(
            {
                "user_code": device["user_code"],
                "verification_url": device["verification_url"],
                "expires_in_seconds": device["expires_in"],
                "device_code": device["device_code"],
                "next_step": (
                    "Open verification_url, enter user_code, then call "
                    "finish_authentication with this device_code."
                ),
            }
        )
    except Exception as e:
        return _err(e)


@mcp.tool(annotations=_WRITE)
def finish_authentication(device_code: str, wait_seconds: int = 0) -> str:
    """Exchange an approved device code for a stored token.

    Args:
        device_code: The device_code returned by start_authentication.
        wait_seconds: How long to keep polling while you approve in the
            browser. 0 checks once and reports whether approval is still
            pending, which is the better default for an interactive session.
    """
    try:
        deadline = time.time() + max(0, wait_seconds)
        while True:
            response = _client().post(
                "/oauth/device/token",
                json={
                    "code": device_code,
                    "client_id": client_id(),
                    "client_secret": _client_secret(),
                },
            )

            if response.status_code == 200:
                store_token(response.json())
                return _ok({"authenticated": True})

            # Trakt signals flow state through the status code alone.
            pending = response.status_code == 400
            if pending and time.time() < deadline:
                time.sleep(5)
                continue

            return json.dumps(
                {
                    "status": "error",
                    "message": {
                        400: "Not approved yet. Enter the code in the browser, "
                        "then call this again.",
                        404: "Unknown device code. Run start_authentication again.",
                        409: "This code was already used.",
                        410: "The code expired. Run start_authentication again.",
                        418: "Sign-in was denied.",
                        429: "Polling too fast. Wait a few seconds.",
                    }.get(
                        response.status_code,
                        f"Trakt refused the code (HTTP {response.status_code}).",
                    ),
                }
            )
    except Exception as e:
        return _err(e)


@mcp.tool(annotations=_READ)
def get_authentication_status() -> str:
    """Report whether an account is signed in and when the token expires."""
    try:
        token = load_token()
        if not token:
            return _ok({"authenticated": False})
        expires_at = token.get("expires_at", 0)
        return _ok(
            {
                "authenticated": True,
                "expires_at": expires_at,
                "expires_in_seconds": max(0, int(expires_at - time.time())),
                "can_refresh": bool(
                    token.get("refresh_token") and os.getenv(ENV_CLIENT_SECRET)
                ),
            }
        )
    except Exception as e:
        return _err(e)


@mcp.tool(annotations=_DESTRUCTIVE)
def clear_authentication() -> str:
    """Revoke the stored token and forget it."""
    try:
        token = load_token()
        if token and os.getenv(ENV_CLIENT_SECRET):
            try:
                _client().post(
                    "/oauth/revoke",
                    json={
                        "token": token.get("access_token"),
                        "client_id": client_id(),
                        "client_secret": _client_secret(),
                    },
                )
            except httpx.HTTPError:
                # A token Trakt has already dropped still has to be forgotten
                # locally, so a failed revoke is not a failed sign-out.
                pass
        return _ok({"cleared": clear_token()})
    except Exception as e:
        return _err(e)
