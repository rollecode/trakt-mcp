"""Server instance, OAuth client and the call helper every generated tool uses."""

import importlib.metadata
import json
import logging
import os
import time
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import Icon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP = "trakt"
TITLE = "Trakt"
BASE_URL = "https://api.trakt.tv"
DEFAULT_PORT = 8580

ENV_CLIENT_ID = "TRAKT_CLIENT_ID"
ENV_CLIENT_SECRET = "TRAKT_CLIENT_SECRET"

# Trakt pins its API generation in a header rather than the path.
API_VERSION = "2"

_TOKEN_PATH = (
    Path(os.getenv("XDG_CACHE_HOME") or Path.home() / ".cache")
    / "trakt-mcp"
    / "token.json"
)

# Refresh a little before expiry rather than after a 401, so a long call does
# not fail on a token that lapses mid-flight.
_REFRESH_MARGIN_SECONDS = 600

try:
    __version__ = importlib.metadata.version(f"{APP}-mcp")
except importlib.metadata.PackageNotFoundError:  # running from a source tree
    __version__ = "0.0.0"

_ICON_BASE = os.getenv("MCP_PUBLIC_URL", "").rstrip("/")
_ICON_SIZES = (48, 96, 256)

mcp = FastMCP(
    APP,
    icons=(
        [
            Icon(
                src=f"{_ICON_BASE}/icon.png"
                if size == 256
                else f"{_ICON_BASE}/icon-{size}.png",
                mimeType="image/png",
                sizes=[f"{size}x{size}"],
            )
            for size in _ICON_SIZES
        ]
        if _ICON_BASE
        else None
    ),
    website_url=_ICON_BASE or None,
    instructions=(
        "Read and write Trakt: shows, movies, seasons, episodes, people, "
        "comments, lists, recommendations, calendars, scrobbling, check-ins "
        "and the signed-in user's collection, watchlist, history and ratings. "
        "Every endpoint is a tool, named verb-first: list_* and get_* read, "
        "create_* posts, update_* puts and delete_* removes. "
        "Public data needs only a client id. Anything under sync, users/me or "
        "checkin needs a signed-in account: run start_authentication, open the "
        "URL it returns, enter the code, then call finish_authentication. "
        "Ids may be a Trakt id, a slug, or an IMDB id."
    ),
)

mcp._mcp_server.version = __version__

_READ = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": True,
}
_WRITE = {
    "readOnlyHint": False,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": True,
}
_DESTRUCTIVE = {**_WRITE, "destructiveHint": True}

_http: httpx.Client | None = None
_token: dict | None = None


class TraktError(RuntimeError):
    """Trakt refused a request for a reason worth repeating verbatim."""


def client_id() -> str:
    value = os.getenv(ENV_CLIENT_ID)
    if not value:
        raise TraktError(
            f"{ENV_CLIENT_ID} is not set. Create an application at "
            "https://trakt.tv/oauth/applications and use its client id."
        )
    return value


def _client() -> httpx.Client:
    global _http
    if _http is None:
        _http = httpx.Client(base_url=BASE_URL, timeout=60.0)
    return _http


# -- token storage ----------------------------------------------------


def load_token() -> dict | None:
    global _token
    if _token is None:
        try:
            _token = json.loads(_TOKEN_PATH.read_text())
        except (OSError, ValueError):
            return None
    return _token


def store_token(token: dict) -> None:
    global _token
    token = dict(token)
    token["expires_at"] = int(token.get("created_at", time.time())) + int(
        token.get("expires_in", 0)
    )
    _TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    _TOKEN_PATH.write_text(json.dumps(token))
    _TOKEN_PATH.chmod(0o600)
    _token = token


def clear_token() -> bool:
    global _token
    _token = None
    try:
        _TOKEN_PATH.unlink()
    except FileNotFoundError:
        return False
    return True


def access_token() -> str | None:
    """The current access token, refreshed when it is close to expiring."""
    token = load_token()
    if not token:
        return None

    expires_at = token.get("expires_at", 0)
    if expires_at and time.time() > expires_at - _REFRESH_MARGIN_SECONDS:
        refreshed = _refresh(token)
        if refreshed:
            return refreshed.get("access_token")
    return token.get("access_token")


def _refresh(token: dict) -> dict | None:
    secret = os.getenv(ENV_CLIENT_SECRET)
    refresh = token.get("refresh_token")
    if not secret or not refresh:
        return None
    try:
        response = _client().post(
            "/oauth/token",
            json={
                "refresh_token": refresh,
                "client_id": client_id(),
                "client_secret": secret,
                "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
                "grant_type": "refresh_token",
            },
        )
        response.raise_for_status()
    except (httpx.HTTPError, TraktError):
        logger.warning("Token refresh failed; the stored token may have been revoked")
        return None

    fresh = response.json()
    store_token(fresh)
    return fresh


# -- transport --------------------------------------------------------


def _headers() -> dict[str, str]:
    headers = {
        "Content-Type": "application/json",
        "trakt-api-version": API_VERSION,
        "trakt-api-key": client_id(),
    }
    token = access_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _err(e: Exception) -> str:
    if isinstance(e, TraktError):
        msg = str(e)
    elif isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        hints = {
            # Ref: https://trakt.docs.apiary.io/#introduction/status-codes
            401: "Not signed in, or the token expired. Run start_authentication.",
            403: f"Invalid API key. Check {ENV_CLIENT_ID}.",
            404: "No such resource. Check the id, slug or IMDB id.",
            409: "Already exists, or the episode is already being watched.",
            420: "Account limit reached. Trakt VIP raises list and item limits.",
            423: "Locked user account. Contact Trakt support.",
            426: "VIP only. This endpoint needs a Trakt VIP subscription.",
            429: "Rate limit exceeded. Wait before retrying.",
        }
        msg = hints.get(status) or f"{TITLE} API error (HTTP {status}): {_detail(e.response)}"
    elif isinstance(e, httpx.ConnectError):
        msg = f"Could not connect to {TITLE}. Check network connectivity."
    elif isinstance(e, httpx.TimeoutException):
        msg = f"Request timed out. {TITLE} may be slow -- try again."
    else:
        msg = f"{type(e).__name__}: {e}"

    return json.dumps({"status": "error", "message": msg})


def _detail(response: httpx.Response) -> str:
    try:
        return json.dumps(response.json())[:800]
    except ValueError:
        return response.text[:400]


def call(
    method: str,
    path: str,
    query: dict | None = None,
    body: dict | None = None,
    form: dict | None = None,
) -> str:
    """Perform one API call and return its result as a JSON string.

    Paged endpoints report their totals in headers rather than the body, so
    those are handed back alongside the results.
    """
    try:
        params = {k: v for k, v in (query or {}).items() if v is not None}
        params.update({k: v for k, v in (form or {}).items() if v is not None})

        response = _client().request(
            method,
            path,
            params=params or None,
            json=body,
            headers=_headers(),
        )
        response.raise_for_status()

        payload: dict = {"status": "success"}

        pagination = {
            key: response.headers[header]
            for key, header in (
                ("page", "X-Pagination-Page"),
                ("limit", "X-Pagination-Limit"),
                ("page_count", "X-Pagination-Page-Count"),
                ("item_count", "X-Pagination-Item-Count"),
            )
            if header in response.headers
        }
        if pagination:
            payload["pagination"] = pagination

        if not response.content:
            payload["result"] = None
            return json.dumps(payload)
        try:
            payload["result"] = response.json()
        except ValueError:
            payload["result"] = response.text
        return json.dumps(payload, indent=2)
    except Exception as e:
        return _err(e)


def main() -> None:
    import argparse

    from dotenv import find_dotenv, load_dotenv

    from . import auth, tools  # noqa: F401 -- importing registers every tool

    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path and load_dotenv(dotenv_path, override=False):
        logger.info("Loaded .env from %s", dotenv_path)

    parser = argparse.ArgumentParser(prog=f"{APP}-mcp")
    parser.add_argument(
        "--transport",
        choices=("stdio", "http"),
        default=os.getenv("MCP_TRANSPORT", "stdio"),
    )
    parser.add_argument("--host", default=os.getenv("MCP_HOST", "127.0.0.1"))
    parser.add_argument(
        "--port", type=int, default=int(os.getenv("MCP_PORT", str(DEFAULT_PORT)))
    )
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
        return

    if args.host not in ("127.0.0.1", "::1", "localhost"):
        raise SystemExit(
            f"refusing to listen on {args.host}: this server has no login of "
            "its own. Keep it on the local machine and put a proxy in front."
        )

    mcp.settings.host = args.host
    mcp.settings.port = args.port
    logger.info("Listening on http://%s:%d/mcp", args.host, args.port)
    mcp.run(transport="streamable-http")
