<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Trakt MCP server

<img style="justify-content:center;text-align: center;width: 95px; height: auto;" width="793" height="411" alt="image" src="https://github.com/user-attachments/assets/abed1a04-d69b-4ab4-a490-d606064df72d" />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="public/logo-dark.png" />
  <img style="justify-content:center;text-align: center;width: 252px; height: auto;" alt="Trakt API" src="public/logo.png" />
</picture>

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Trakt](https://img.shields.io/badge/Trakt-ED1C24?style=for-the-badge&logo=trakt&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-334%2F334-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Read and write Trakt from Claude.ai and Claude Code. All 334 endpoints are tools, generated from Trakt's own contract package. Not a curated subset: shows, movies, seasons, episodes, people, comments, lists, calendars, scrobbling, check-ins and everything under a signed-in account.

<hr>

## Why not the other options

| Server | Tools | Coverage |
| --- | --- | --- |
| `wwiens/trakt_mcpserver` | 79 | 24 % |
| `niavasha/plex-mcp-server` (trakt part) | 9 | 3 % |
| This one | **334** | **100 %** |

The existing servers cover trending, popular, a user's history and a check-in. Nothing else exposes notes, smart lists, favorites, hidden items, the recommendation feed, JustWatch sources, reactions, the scrobbler, calendars beyond the basics, or most of the sync surface that makes Trakt worth scripting.

## How it stays complete

Trakt publishes no OpenAPI file, but it maintains [`trakt/api-help`](https://github.com/trakt/api-help), a typed contract package covering every endpoint, with a task that renders it to OpenAPI. `scripts/fetch_spec.sh` runs that task and slims the 5 MB result down to what the generator reads:

```bash
scripts/fetch_spec.sh
python scripts/generate_tools.py openapi.json src/trakt_mcp/tools.py
```

This uses Trakt's own generator rather than parsing their contracts independently, so the document here is the one their tooling produces. A test then compares every generated call against every operation in it, in both directions.

## Tool names

Verb first, derived from the method and path:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_movies_trending` |
| `get_*` | Read one record | `get_shows_by_id` |
| `create_*` | POST | `create_checkin`, `create_sync_history` |
| `update_*` | PUT | `update_users_by_id_lists_by_list_id` |
| `delete_*` | DELETE | `delete_sync_watchlist_remove` |

334 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## What is covered

Every group in the contract: shows, seasons, episodes, movies, people, search, calendars, comments and reactions, lists and smart lists, notes, recommendations and social recommendations, scrobble, checkin, watchnow and JustWatch sources, certifications, countries, languages, genres, networks, and the whole `sync` and `users` surface: collection, history, watchlist, favorites, hidden items, ratings, playback progress and up next.

## Setup

```bash
git clone https://github.com/rollecode/trakt-mcp.git
cd trakt-mcp
uv venv && uv pip install -e .
```

Create an application at [trakt.tv/oauth/applications](https://trakt.tv/oauth/applications) with the redirect URI `urn:ietf:wg:oauth:2.0:oob`, then:

```bash
export TRAKT_CLIENT_ID=...
export TRAKT_CLIENT_SECRET=...   # only needed for signing in
```

### Claude Code

```bash
claude mcp add trakt -- /path/to/trakt-mcp/.venv/bin/trakt-mcp
```

### Signing in

Public data needs only the client id. Anything under `sync`, `users/me`, `checkin` or `scrobble` needs an account:

1. `start_authentication` returns a code and a URL
2. Open the URL, enter the code
3. `finish_authentication` with the same device code

The token lands in `~/.cache/trakt-mcp/token.json` with mode 600 and is refreshed automatically shortly before it expires. `clear_authentication` revokes it.

## Pagination

Trakt reports paging in headers rather than the body, so every result carries a `pagination` block alongside `result` when the endpoint is paged.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

