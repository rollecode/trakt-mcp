"""Call real generated tools and check the requests they build.

The coverage tests read tools.py as text and the runtime tests exercise call()
directly, so without this nothing proves a generated function actually
produces the request its docstring claims.
"""

import json
import time

import httpx
import pytest

from trakt_mcp import runtime, tools


@pytest.fixture(autouse=True)
def transport(monkeypatch, tmp_path):
    monkeypatch.setenv("TRAKT_CLIENT_ID", "cid")
    monkeypatch.setenv("TRAKT_CLIENT_SECRET", "secret")
    monkeypatch.setattr(runtime, "_TOKEN_PATH", tmp_path / "token.json")
    runtime._http = None
    runtime._token = None
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        seen["query"] = dict(request.url.params)
        seen["headers"] = dict(request.headers)
        seen["body"] = json.loads(request.content) if request.content else None
        return httpx.Response(200, json=[])

    runtime._http = httpx.Client(
        base_url=runtime.BASE_URL, transport=httpx.MockTransport(handler)
    )
    yield seen
    runtime._http = None
    runtime._token = None


def test_a_collection_read_hits_the_collection(transport):
    result = json.loads(tools.list_movies_trending())
    assert result["status"] == "success"
    assert transport["method"] == "GET"
    assert transport["path"] == "/movies/trending"


def test_a_path_parameter_lands_in_the_url(transport):
    tools.get_movies_by_id("tron-legacy-2010")
    assert transport["path"] == "/movies/tron-legacy-2010"


def test_query_parameters_are_sent(transport):
    tools.list_movies_trending(page=2)
    assert transport["query"]["page"] == "2"


def test_generated_tools_carry_the_api_headers(transport):
    tools.list_movies_trending()
    assert transport["headers"]["trakt-api-key"] == "cid"
    assert transport["headers"]["trakt-api-version"] == "2"


def test_an_authenticated_call_carries_the_bearer_token(transport):
    runtime.store_token(
        {"access_token": "tok", "expires_in": 7200, "created_at": int(time.time())}
    )
    tools.list_sync_last_activities()
    assert transport["headers"]["authorization"] == "Bearer tok"


def test_a_write_sends_its_payload(transport):
    tools.create_checkin({"movie": {"ids": {"trakt": 1}}})
    assert transport["method"] == "POST"
    assert transport["path"] == "/checkin"
    assert transport["body"] == {"movie": {"ids": {"trakt": 1}}}


def test_a_delete_reaches_the_right_path(transport):
    tools.delete_checkin()
    assert transport["method"] == "DELETE"
    assert transport["path"] == "/checkin"


def test_a_failure_comes_back_as_a_structured_error():
    runtime._http = httpx.Client(
        base_url=runtime.BASE_URL,
        transport=httpx.MockTransport(lambda request: httpx.Response(404)),
    )
    result = json.loads(tools.get_movies_by_id("nope"))
    assert result["status"] == "error"
    assert "id" in result["message"]


def test_annotations_match_what_each_tool_does():
    import asyncio

    registered = {t.name: t for t in asyncio.run(runtime.mcp.list_tools())}
    assert registered["list_movies_trending"].annotations.readOnlyHint is True
    assert registered["delete_checkin"].annotations.destructiveHint is True
    assert registered["create_checkin"].annotations.readOnlyHint is False


def test_the_hand_written_auth_tools_are_registered_too():
    import asyncio

    from trakt_mcp import auth  # noqa: F401 -- registers the four auth tools

    names = {t.name for t in asyncio.run(runtime.mcp.list_tools())}
    assert {
        "start_authentication",
        "finish_authentication",
        "get_authentication_status",
        "clear_authentication",
    } <= names
