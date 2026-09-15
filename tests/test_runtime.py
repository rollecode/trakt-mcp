import json
import time

import httpx
import pytest

from trakt_mcp import runtime


@pytest.fixture(autouse=True)
def reset(monkeypatch, tmp_path):
    monkeypatch.setenv("TRAKT_CLIENT_ID", "cid")
    monkeypatch.setenv("TRAKT_CLIENT_SECRET", "secret")
    monkeypatch.setattr(runtime, "_TOKEN_PATH", tmp_path / "token.json")
    runtime._http = None
    runtime._token = None
    yield
    runtime._http = None
    runtime._token = None


def install(handler):
    runtime._http = httpx.Client(
        base_url=runtime.BASE_URL, transport=httpx.MockTransport(handler)
    )


def test_missing_client_id_says_where_to_get_one(monkeypatch):
    monkeypatch.delenv("TRAKT_CLIENT_ID", raising=False)
    message = json.loads(runtime.call("GET", "/movies/popular"))["message"]
    assert "TRAKT_CLIENT_ID" in message


def test_required_headers_are_sent():
    seen = {}

    def handler(request):
        seen.update(request.headers)
        return httpx.Response(200, json=[])

    install(handler)
    runtime.call("GET", "/movies/popular")
    assert seen["trakt-api-key"] == "cid"
    assert seen["trakt-api-version"] == "2"
    assert "authorization" not in seen


def test_a_stored_token_becomes_a_bearer_header():
    runtime.store_token(
        {"access_token": "tok", "expires_in": 7200, "created_at": int(time.time())}
    )
    seen = {}

    def handler(request):
        seen.update(request.headers)
        return httpx.Response(200, json=[])

    install(handler)
    runtime.call("GET", "/sync/history")
    assert seen["authorization"] == "Bearer tok"


def test_an_expiring_token_is_refreshed_before_use():
    runtime.store_token(
        {
            "access_token": "old",
            "refresh_token": "r",
            "expires_in": 60,
            "created_at": int(time.time()),
        }
    )
    calls = []

    def handler(request):
        calls.append(request.url.path)
        if request.url.path == "/oauth/token":
            return httpx.Response(
                200,
                json={
                    "access_token": "new",
                    "refresh_token": "r2",
                    "expires_in": 7200,
                    "created_at": int(time.time()),
                },
            )
        return httpx.Response(200, json=[])

    install(handler)
    runtime.call("GET", "/sync/history")
    assert "/oauth/token" in calls
    assert runtime.load_token()["access_token"] == "new"


def test_a_failed_refresh_does_not_lose_the_token():
    runtime.store_token(
        {
            "access_token": "old",
            "refresh_token": "r",
            "expires_in": 60,
            "created_at": int(time.time()),
        }
    )

    def handler(request):
        if request.url.path == "/oauth/token":
            return httpx.Response(401, json={})
        return httpx.Response(200, json=[])

    install(handler)
    runtime.call("GET", "/sync/history")
    assert runtime.load_token()["access_token"] == "old"


def test_the_token_file_is_not_world_readable():
    runtime.store_token({"access_token": "tok", "expires_in": 1, "created_at": 0})
    assert oct(runtime._TOKEN_PATH.stat().st_mode)[-3:] == "600"


def test_pagination_headers_are_reported():
    install(
        lambda request: httpx.Response(
            200,
            json=[],
            headers={"X-Pagination-Page": "2", "X-Pagination-Page-Count": "9"},
        )
    )
    result = json.loads(runtime.call("GET", "/movies/popular"))
    assert result["pagination"] == {"page": "2", "page_count": "9"}


def test_vip_only_endpoints_say_so():
    install(lambda request: httpx.Response(426))
    assert "VIP" in json.loads(runtime.call("GET", "/movies/popular"))["message"]


def test_rate_limit_is_explained():
    install(lambda request: httpx.Response(429))
    assert "Rate limit" in json.loads(runtime.call("GET", "/movies/popular"))["message"]


def test_empty_body_is_success():
    install(lambda request: httpx.Response(204))
    assert json.loads(runtime.call("DELETE", "/users/me/lists/1"))["result"] is None


def test_clear_token_reports_whether_anything_was_there():
    assert runtime.clear_token() is False
    runtime.store_token({"access_token": "t", "expires_in": 1, "created_at": 0})
    assert runtime.clear_token() is True


def test_every_tool_registers():
    import asyncio

    from trakt_mcp import auth, tools  # noqa: F401 -- registers the tools

    registered = asyncio.run(runtime.mcp.list_tools())
    assert len(registered) == 338
