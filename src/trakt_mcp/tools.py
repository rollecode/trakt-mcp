"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/trakt_mcp/tools.py

One tool per operation, 334 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_checkin(body: dict) -> str:
    """Check into an item.

    POST /checkin

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/checkin", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_comments(body: dict) -> str:
    """Post a comment.

    POST /comments/

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/comments/", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_comments_by_id_like(id: str, body: dict) -> str:
    """Like a comment.

    POST /comments/{id}/like

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/comments/{id}/like", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_comments_by_id_reactions_by_reaction_type(id: str, reaction_type: str, body: dict) -> str:
    """Add comment reaction.

    POST /comments/{id}/reactions/{reaction_type}

    Args:
        id: Path parameter.
        reaction_type: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/comments/{id}/reactions/{reaction_type}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_comments_by_id_replies(id: str, body: dict) -> str:
    """Post a reply for a comment.

    POST /comments/{id}/replies

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/comments/{id}/replies", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_comments_by_id_report(id: str, body: dict) -> str:
    """Report a comment.

    POST /comments/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/comments/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_episodes_by_id_report(id: str, body: dict) -> str:
    """Report an episode.

    POST /episodes/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/episodes/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_lists_by_id_like(id: str, body: dict) -> str:
    """Like a list.

    POST /lists/{id}/like

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/lists/{id}/like", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_lists_by_id_report(id: str, body: dict) -> str:
    """Report a list.

    POST /lists/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/lists/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_movies_by_id_refresh(id: str, body: dict, images: bool | None = None) -> str:
    """Refresh movie metadata.

    POST /movies/{id}/refresh

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        images: Also queue a refresh of the resource images.
    """
    return call("POST", f"/movies/{id}/refresh", query={"images": images}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_movies_by_id_refresh_justwatch(id: str, body: dict) -> str:
    """Refresh movie JustWatch links.

    POST /movies/{id}/refresh/justwatch

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/movies/{id}/refresh/justwatch", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_movies_by_id_report(id: str, body: dict) -> str:
    """Report a movie.

    POST /movies/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/movies/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notes(body: dict) -> str:
    """Add notes.

    POST /notes

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/notes", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_oauth_device_code(body: dict) -> str:
    """Generate new device codes.

    POST /oauth/device/code

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/oauth/device/code", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_oauth_device_token(body: dict) -> str:
    """Poll for the access_token.

    POST /oauth/device/token

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/oauth/device/token", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_oauth_revoke(body: dict) -> str:
    """Revoke an access_token.

    POST /oauth/revoke

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/oauth/revoke", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_oauth_token(body: dict) -> str:
    """Exchange a token.

    POST /oauth/token

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/oauth/token", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_people_by_id_refresh(id: str, body: dict, images: bool | None = None) -> str:
    """Refresh person metadata.

    POST /people/{id}/refresh

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        images: Also queue a refresh of the resource images.
    """
    return call("POST", f"/people/{id}/refresh", query={"images": images}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_people_by_id_report(id: str, body: dict) -> str:
    """Report a person.

    POST /people/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/people/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_scrobble_pause(body: dict) -> str:
    """Pause watching in a media center.

    POST /scrobble/pause

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/scrobble/pause", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_scrobble_start(body: dict) -> str:
    """Start watching in a media center.

    POST /scrobble/start

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/scrobble/start", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_scrobble_stop(body: dict) -> str:
    """Stop or finish watching in a media center.

    POST /scrobble/stop

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/scrobble/stop", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_search_recent(body: dict) -> str:
    """Add recent search.

    POST /search/recent/

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/search/recent/", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_search_recent_remove(body: dict) -> str:
    """Remove recent search.

    POST /search/recent/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/search/recent/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_seasons_by_id_report(id: str, body: dict) -> str:
    """Report a season.

    POST /seasons/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/seasons/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_progress_watched_reset(id: str, body: dict) -> str:
    """Reset show progress.

    POST /shows/{id}/progress/watched/reset

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/shows/{id}/progress/watched/reset", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_refresh(id: str, body: dict, images: bool | None = None) -> str:
    """Refresh show metadata.

    POST /shows/{id}/refresh

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        images: Also queue a refresh of the resource images.
    """
    return call("POST", f"/shows/{id}/refresh", query={"images": images}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_refresh_justwatch(id: str, body: dict) -> str:
    """Refresh show JustWatch links.

    POST /shows/{id}/refresh/justwatch

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/shows/{id}/refresh/justwatch", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_report(id: str, body: dict) -> str:
    """Report a show.

    POST /shows/{id}/report

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/shows/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_seasons_by_season_episodes_by_episode_report(id: str, season: int, episode: int, body: dict) -> str:
    """Report an episode.

    POST /shows/{id}/seasons/{season}/episodes/{episode}/report

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/shows/{id}/seasons/{season}/episodes/{episode}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_shows_by_id_seasons_by_season_report(id: str, season: int, body: dict) -> str:
    """Report a season.

    POST /shows/{id}/seasons/{season}/report

    Args:
        id: The id/slug of the resource.
        season: Season number
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/shows/{id}/seasons/{season}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_collection(body: dict) -> str:
    """Add items to collection.

    POST /sync/collection

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/collection", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_collection_remove(body: dict) -> str:
    """Remove items from collection.

    POST /sync/collection/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/collection/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_favorites(body: dict) -> str:
    """Add items to favorites.

    POST /sync/favorites

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/favorites", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_favorites_remove(body: dict) -> str:
    """Remove items from favorites.

    POST /sync/favorites/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/favorites/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_favorites_reorder(body: dict) -> str:
    """Reorder favorited items.

    POST /sync/favorites/reorder

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/favorites/reorder", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_history(body: dict) -> str:
    """Add items to watched history.

    POST /sync/history

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/history", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_history_remove(body: dict) -> str:
    """Remove items from history.

    POST /sync/history/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/history/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_ratings(body: dict) -> str:
    """Add new ratings.

    POST /sync/ratings

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/ratings", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_ratings_remove(body: dict) -> str:
    """Remove ratings.

    POST /sync/ratings/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/ratings/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_watchlist(body: dict) -> str:
    """Add items to watchlist.

    POST /sync/watchlist

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/watchlist", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_watchlist_remove(body: dict) -> str:
    """Remove items from watchlist.

    POST /sync/watchlist/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/watchlist/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sync_watchlist_reorder(body: dict) -> str:
    """Reorder watchlist items.

    POST /sync/watchlist/reorder

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/sync/watchlist/reorder", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_block(id: str, body: dict) -> str:
    """Block this user.

    POST /users/{id}/block

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/block", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_follow(id: str, body: dict) -> str:
    """Follow this user.

    POST /users/{id}/follow

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/follow", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists(id: str, body: dict) -> str:
    """Create personal list.

    POST /users/{id}/lists

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_items(id: str, list_id: str, body: dict) -> str:
    """Add items to personal list.

    POST /users/{id}/lists/{list_id}/items

    Args:
        id: Path parameter.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/items", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_items_remove(id: str, list_id: str, body: dict) -> str:
    """Remove items from personal list.

    POST /users/{id}/lists/{list_id}/items/remove

    Args:
        id: Path parameter.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/items/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_items_reorder(id: str, list_id: str, body: dict) -> str:
    """Reorder items on a list.

    POST /users/{id}/lists/{list_id}/items/reorder

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/items/reorder", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_like(id: str, list_id: str, body: dict) -> str:
    """Like a list.

    POST /users/{id}/lists/{list_id}/like

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/like", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_reorder(id: str, list_id: str, body: dict) -> str:
    """Reorder items on a list.

    POST /users/{id}/lists/{list_id}/reorder

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/reorder", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_by_list_id_report(id: str, list_id: str, body: dict) -> str:
    """Report a user's list.

    POST /users/{id}/lists/{list_id}/report

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/{list_id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_lists_reorder(id: str, body: dict) -> str:
    """Reorder a user's lists.

    POST /users/{id}/lists/reorder

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/lists/reorder", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_report(id: str, body: dict) -> str:
    """Report a user.

    POST /users/{id}/report

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/report", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_by_id_smart_lists(id: str, body: dict) -> str:
    """Create smart list.

    POST /users/{id}/smart-lists

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/{id}/smart-lists", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_hidden_by_section(section: str, body: dict) -> str:
    """Add hidden items.

    POST /users/hidden/{section}

    Args:
        section: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/hidden/{section}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_hidden_by_section_remove(section: str, body: dict) -> str:
    """Remove hidden items.

    POST /users/hidden/{section}/remove

    Args:
        section: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/users/hidden/{section}/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_hidden_calendar_remove(body: dict) -> str:
    """Remove hidden calendar items.

    POST /users/hidden/calendar/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/hidden/calendar/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_hidden_progress_watched_remove(body: dict) -> str:
    """Remove hidden progress items.

    POST /users/hidden/progress_watched/remove

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/hidden/progress_watched/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_requests_by_id(id: str, body: dict, extended: str | None = None) -> str:
    """Approve follow request.

    POST /users/requests/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        extended: Extended information to include in the response.
    """
    return call("POST", f"/users/requests/{id}", query={"extended": extended}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_saved_filters(body: dict) -> str:
    """Add saved filters.

    POST /users/saved_filters

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/saved_filters", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_settings_plex_connect(body: dict) -> str:
    """Connect Plex.

    POST /users/settings/plex/connect

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/settings/plex/connect", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users_settings_plex_sync(body: dict) -> str:
    """Sync Plex now.

    POST /users/settings/plex/sync

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/settings/plex/sync", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_younify_connect(body: dict) -> str:
    """Create a streaming connection.

    POST /younify/connect

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/younify/connect", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_younify_users_refresh_by_service_id(service_id: str, body: dict) -> str:
    """Refresh a streaming service.

    POST /younify/users/refresh/{service_id}

    Args:
        service_id: The streaming service id (e.g. `netflix`).
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/younify/users/refresh/{service_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_younify_users_refresh_by_service_id_by_all_data(service_id: str, all_data: str, body: dict) -> str:
    """Refresh a streaming service (full re-sync).

    POST /younify/users/refresh/{service_id}/{all_data}

    Args:
        service_id: The streaming service id to re-sync (e.g. `netflix`).
        all_data: Optional trailing segment that forces a full re-sync of all data rather than an incremental one.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/younify/users/refresh/{service_id}/{all_data}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_checkin() -> str:
    """Delete any active checkins.

    DELETE /checkin
    """
    return call("DELETE", "/checkin", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_comments_by_id(id: str) -> str:
    """Delete a comment or reply.

    DELETE /comments/{id}/

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/comments/{id}/", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_comments_by_id_like(id: str) -> str:
    """Remove like on a comment.

    DELETE /comments/{id}/like

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/comments/{id}/like", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_comments_by_id_reactions_by_reaction_type(id: str, reaction_type: str) -> str:
    """Remove comment reaction.

    DELETE /comments/{id}/reactions/{reaction_type}

    Args:
        id: Path parameter.
        reaction_type: Path parameter.
    """
    return call("DELETE", f"/comments/{id}/reactions/{reaction_type}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_lists_by_id_like(id: str) -> str:
    """Remove like on a list.

    DELETE /lists/{id}/like

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/lists/{id}/like", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_notes_by_id(id: str) -> str:
    """Delete a note.

    DELETE /notes/{id}

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/notes/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_recommendations_movies_by_id(id: str) -> str:
    """Hide a movie recommendation.

    DELETE /recommendations/movies/{id}

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/recommendations/movies/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_recommendations_shows_by_id(id: str) -> str:
    """Hide a show recommendation.

    DELETE /recommendations/shows/{id}

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/recommendations/shows/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_shows_by_id_progress_watched_reset(id: str) -> str:
    """Undo reset show progress.

    DELETE /shows/{id}/progress/watched/reset

    Args:
        id: The id/slug of the resource.
    """
    return call("DELETE", f"/shows/{id}/progress/watched/reset", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_sync_playback_by_id(id: int) -> str:
    """Remove a playback item.

    DELETE /sync/playback/{id}

    Args:
        id: ID of the playback entry
    """
    return call("DELETE", f"/sync/playback/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id_block(id: str) -> str:
    """Unblock this user.

    DELETE /users/{id}/block

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
    """
    return call("DELETE", f"/users/{id}/block", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id_follow(id: str) -> str:
    """Unfollow this user.

    DELETE /users/{id}/follow

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
    """
    return call("DELETE", f"/users/{id}/follow", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id_lists_by_list_id(id: str, list_id: str) -> str:
    """Delete a user's personal list.

    DELETE /users/{id}/lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
    """
    return call("DELETE", f"/users/{id}/lists/{list_id}/", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id_lists_by_list_id_like(id: str, list_id: str) -> str:
    """Remove like on a list.

    DELETE /users/{id}/lists/{list_id}/like

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
    """
    return call("DELETE", f"/users/{id}/lists/{list_id}/like", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id_smart_lists_by_list_id(id: str, list_id: str) -> str:
    """Delete a user's smart list.

    DELETE /users/{id}/smart-lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
    """
    return call("DELETE", f"/users/{id}/smart-lists/{list_id}/", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_requests_by_id(id: str) -> str:
    """Deny follow request.

    DELETE /users/requests/{id}

    Args:
        id: Path parameter.
    """
    return call("DELETE", f"/users/requests/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_saved_filters_by_id(id: int) -> str:
    """Delete saved filter.

    DELETE /users/saved_filters/{id}

    Args:
        id: ID of the saved filter
    """
    return call("DELETE", f"/users/saved_filters/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_settings_plex_connect() -> str:
    """Disconnect Plex.

    DELETE /users/settings/plex/connect
    """
    return call("DELETE", "/users/settings/plex/connect", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_syncs_by_id(id: int) -> str:
    """Undo a data sync.

    DELETE /users/syncs/{id}

    Args:
        id: The numeric sync id, scoped to the authenticated user. A numeric segment hits a single sync; a non-numeric segment is the filtered list.
    """
    return call("DELETE", f"/users/syncs/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_younify_users_services_by_service_id(service_id: str) -> str:
    """Unlink a streaming service.

    DELETE /younify/users/services/{service_id}

    Args:
        service_id: The streaming service id (e.g. `netflix`).
    """
    return call("DELETE", f"/younify/users/services/{service_id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_dvd_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get DVD releases.

    GET /calendars/{target}/dvd/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/dvd/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_media_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, type: str | None = None, group: str | None = None) -> str:
    """Get media.

    GET /calendars/{target}/media/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        type: Narrow the feed to a single media type. Omit to return both.
        group: Collapse same-show-same-day episodes into a single card (`full_season` / `multiple_episodes`). Omit for one entry per episode.
    """
    return call("GET", f"/calendars/{target}/media/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "type": type, "group": group}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_movies_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get movies.

    GET /calendars/{target}/movies/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/movies/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_shows_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, group: str | None = None) -> str:
    """Get shows.

    GET /calendars/{target}/shows/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        group: Collapse same-show-same-day episodes into a single card (`full_season` / `multiple_episodes`). Omit for one entry per episode.
    """
    return call("GET", f"/calendars/{target}/shows/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "group": group}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_shows_finales_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get finales.

    GET /calendars/{target}/shows/finales/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/shows/finales/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_shows_new_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get new shows.

    GET /calendars/{target}/shows/new/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/shows/new/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_shows_premieres_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get season premieres.

    GET /calendars/{target}/shows/premieres/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/shows/premieres/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_by_target_streaming_by_start_date_by_days(target: str, start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get streaming releases.

    GET /calendars/{target}/streaming/{start_date}/{days}

    Args:
        target: Use "my" for all items that have been watched, collected, or watchlisted plus individual episodes on the watchlist.
      Use "all" for all items items airing during the specified period.
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/calendars/{target}/streaming/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_releases_hot_by_start_date_by_days(start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, type: str | None = None, group: str | None = None) -> str:
    """Get hot releases.

    GET /calendars/releases/hot/{start_date}/{days}

    Args:
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        type: Narrow the feed to a single media type. Omit to return both.
        group: Collapse same-show-same-day episodes into a single card (`full_season` / `multiple_episodes`). Omit for one entry per episode.
    """
    return call("GET", f"/calendars/releases/hot/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "type": type, "group": group}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_releases_hot_finales_by_start_date_by_days(start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get hot finales.

    GET /calendars/releases/hot/finales/{start_date}/{days}

    Args:
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", f"/calendars/releases/hot/finales/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_releases_hot_new_by_start_date_by_days(start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get hot new shows.

    GET /calendars/releases/hot/new/{start_date}/{days}

    Args:
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", f"/calendars/releases/hot/new/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_calendars_releases_hot_premieres_by_start_date_by_days(start_date: str, days: int, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date_query: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get hot premieres.

    GET /calendars/releases/hot/premieres/{start_date}/{days}

    Args:
        start_date: The start date of the calendar. Must be formatted as "YYYY-MM-DD".
        days: The number of days to retrieve.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date_query: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", f"/calendars/releases/hot/premieres/{start_date}/{days}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date_query, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_certifications_by_type(type: str) -> str:
    """Get certifications.

    GET /certifications/{type}

    Args:
        type: Certification media type.
    """
    return call("GET", f"/certifications/{type}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id(id: str) -> str:
    """Get a comment or reply.

    GET /comments/{id}

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/comments/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id_item(id: str, extended: str | None = None) -> str:
    """Get the attached media item.

    GET /comments/{id}/item

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/comments/{id}/item", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id_likes(id: str, page: int | None = None, limit: int | None = None) -> str:
    """Get all users who liked a comment.

    GET /comments/{id}/likes

    Args:
        id: The id/slug of the resource.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/comments/{id}/likes", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id_reactions(id: str, extended: str | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get comment reactions.

    GET /comments/{id}/reactions/

    Args:
        id: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/comments/{id}/reactions/", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id_reactions_summary(id: str) -> str:
    """Get reaction summary.

    GET /comments/{id}/reactions/summary

    Args:
        id: Path parameter.
    """
    return call("GET", f"/comments/{id}/reactions/summary", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_by_id_replies(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get replies for a comment.

    GET /comments/{id}/replies

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/comments/{id}/replies", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_recent_by_comment_type_by_type(comment_type: str, type: str, extended: str | None = None, page: int | None = None, limit: str | None = None, include_replies: bool | None = None) -> str:
    """Get recently created comments.

    GET /comments/recent/{comment_type}/{type}

    Args:
        comment_type: Comment type filter.
        type: Media type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        include_replies: Include replies inline alongside top level comments.
    """
    return call("GET", f"/comments/recent/{comment_type}/{type}", query={"extended": extended, "page": page, "limit": limit, "include_replies": include_replies}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_trending_by_comment_type_by_type(comment_type: str, type: str, extended: str | None = None, page: int | None = None, limit: str | None = None, include_replies: bool | None = None) -> str:
    """Get trending comments.

    GET /comments/trending/{comment_type}/{type}

    Args:
        comment_type: Comment type filter.
        type: Media type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        include_replies: Include replies inline alongside top level comments.
    """
    return call("GET", f"/comments/trending/{comment_type}/{type}", query={"extended": extended, "page": page, "limit": limit, "include_replies": include_replies}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_comments_updates_by_comment_type_by_type(comment_type: str, type: str, extended: str | None = None, page: int | None = None, limit: str | None = None, include_replies: bool | None = None) -> str:
    """Get recently updated comments.

    GET /comments/updates/{comment_type}/{type}

    Args:
        comment_type: Comment type filter.
        type: Media type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        include_replies: Include replies inline alongside top level comments.
    """
    return call("GET", f"/comments/updates/{comment_type}/{type}", query={"extended": extended, "page": page, "limit": limit, "include_replies": include_replies}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_countries_by_type(type: str) -> str:
    """Get countries.

    GET /countries/{type}

    Args:
        type: Media type to return countries for.
    """
    return call("GET", f"/countries/{type}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_episodes_by_id_watchnow_by_country(id: str, country: str, links: str | None = None, extended: str | None = None) -> str:
    """Get episode watch now sources.

    GET /episodes/{id}/watchnow/{country}

    Args:
        id: The Trakt ID of the resource to get the watch now sources of.
        country: 2 character country code.
        links: Query parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/episodes/{id}/watchnow/{country}", query={"links": links, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_genres_by_type(type: str, extended: str | None = None) -> str:
    """Get genres.

    GET /genres/{type}

    Args:
        type: Media type to return genres for.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/genres/{type}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_languages_by_type(type: str) -> str:
    """Get languages.

    GET /languages/{type}

    Args:
        type: Media type to return languages for.
    """
    return call("GET", f"/languages/{type}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id(id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get list.

    GET /lists/{id}

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/lists/{id}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_comments_by_sort(id: str, sort: str, extended: str | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get all list comments.

    GET /lists/{id}/comments/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Comment sort option.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/comments/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_items_by_type_by_sort_by_by_sort_how(id: str, type: str, sort_by: str, sort_how: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get items on a list.

    GET /lists/{id}/items/{type}/{sort_by}/{sort_how}

    Args:
        id: The id/slug of the resource.
        type: List item type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/items/{type}/{sort_by}/{sort_how}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_items_movie(id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get movie list items.

    GET /lists/{id}/items/movie

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/items/movie", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_items_movie_show(id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get media list items.

    GET /lists/{id}/items/movie,show

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/items/movie,show", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_items_movie_show_episode_season(id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get all list items.

    GET /lists/{id}/items/movie,show,episode,season

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/items/movie,show,episode,season", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_items_show(id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get show list items.

    GET /lists/{id}/items/show

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/lists/{id}/items/show", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_by_id_likes(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get all users who liked a list.

    GET /lists/{id}/likes

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/lists/{id}/likes", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_popular_by_type(type: str, extended: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get popular lists.

    GET /lists/popular/{type}

    Args:
        type: List type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", f"/lists/popular/{type}", query={"extended": extended, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_lists_trending_by_type(type: str, extended: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get trending lists.

    GET /lists/trending/{type}

    Args:
        type: List type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", f"/lists/trending/{type}", query={"extended": extended, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id(id: str, extended: str | None = None) -> str:
    """Get a movie.

    GET /movies/{id}

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/movies/{id}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_aliases(id: str) -> str:
    """Get all movie aliases.

    GET /movies/{id}/aliases

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/aliases", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_comments_by_sort(id: str, sort: str, extended: str | None = None, page: int | None = None, limit: str | None = None, language: str | None = None) -> str:
    """Get all movie comments.

    GET /movies/{id}/comments/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        language: Filter comments to a 2 character language code
    """
    return call("GET", f"/movies/{id}/comments/{sort}", query={"extended": extended, "page": page, "limit": limit, "language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_lists_by_type_by_sort(id: str, sort: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get lists containing this movie.

    GET /movies/{id}/lists/{type}/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/movies/{id}/lists/{type}/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_people(id: str, extended: str | None = None) -> str:
    """Get all people for a movie.

    GET /movies/{id}/people

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/movies/{id}/people", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_ratings(id: str, extended: str | None = None) -> str:
    """Get movie ratings.

    GET /movies/{id}/ratings

    Args:
        id: The id/slug of the resource.
        extended: Use `all` to include ratings from supported external sources.
    """
    return call("GET", f"/movies/{id}/ratings", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_related(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get related movies.

    GET /movies/{id}/related

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/movies/{id}/related", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_releases_by_country(id: str, country: str) -> str:
    """Get all movie releases.

    GET /movies/{id}/releases/{country}

    Args:
        id: The id/slug of the resource.
        country: 2 character country code.
    """
    return call("GET", f"/movies/{id}/releases/{country}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_sentiments(id: str) -> str:
    """Get movie sentiments.

    GET /movies/{id}/sentiments

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/sentiments", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_stats(id: str) -> str:
    """Get movie stats.

    GET /movies/{id}/stats

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_studios(id: str) -> str:
    """Get movie studios.

    GET /movies/{id}/studios

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/studios", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_translations(id: str, language: str | None = None) -> str:
    """Get all movie translations.

    GET /movies/{id}/translations

    Args:
        id: The id/slug of the resource.
        language: Filter translations to a 2 character language code
    """
    return call("GET", f"/movies/{id}/translations", query={"language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_videos(id: str) -> str:
    """Get all videos.

    GET /movies/{id}/videos

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/videos", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_watching(id: str, extended: str | None = None) -> str:
    """Get users watching right now.

    GET /movies/{id}/watching

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/movies/{id}/watching", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_watchnow_by_country(id: str, country: str, links: str | None = None, extended: str | None = None) -> str:
    """Get movie watch now sources.

    GET /movies/{id}/watchnow/{country}

    Args:
        id: The id/slug of the resource.
        country: 2 character country code.
        links: Query parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/movies/{id}/watchnow/{country}", query={"links": links, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_by_id_watchnow_justwatch_links_by_country(country: str, id: str) -> str:
    """Get movie JustWatch links.

    GET /movies/{id}/watchnow/justwatch_links/{country}

    Args:
        country: Path parameter.
        id: The id/slug of the resource.
    """
    return call("GET", f"/movies/{id}/watchnow/justwatch_links/{country}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_collected_by_period(period: str, extended: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most collected movies.

    GET /movies/collected/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/movies/collected/{period}", query={"extended": extended, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_favorited_by_period(period: str, extended: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most favorited movies.

    GET /movies/favorited/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/movies/favorited/{period}", query={"extended": extended, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_played_by_period(period: str, extended: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most played movies.

    GET /movies/played/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/movies/played/{period}", query={"extended": extended, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_streaming_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get streaming movies.

    GET /movies/streaming/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/movies/streaming/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_updates_by_start_date(start_date: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated movies.

    GET /movies/updates/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/movies/updates/{start_date}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_updates_id_by_start_date(start_date: str, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated movie Trakt IDs.

    GET /movies/updates/id/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/movies/updates/id/{start_date}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_movies_watched_by_period(period: str, extended: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most watched movies.

    GET /movies/watched/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/movies/watched/{period}", query={"extended": extended, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_notes_by_id(id: str) -> str:
    """Get a note.

    GET /notes/{id}

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/notes/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_notes_by_id_item(id: str) -> str:
    """Get the attached item.

    GET /notes/{id}/item

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/notes/{id}/item", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_by_id(id: str, extended: str | None = None) -> str:
    """Get a single person.

    GET /people/{id}/

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/people/{id}/", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_by_id_lists_by_type_by_sort(id: str, sort: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get lists containing this person.

    GET /people/{id}/lists/{type}/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/people/{id}/lists/{type}/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_by_id_movies(id: str, extended: str | None = None) -> str:
    """Get movie credits.

    GET /people/{id}/movies

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/people/{id}/movies", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_by_id_shows(id: str, extended: str | None = None) -> str:
    """Get show credits.

    GET /people/{id}/shows

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/people/{id}/shows", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_updates_by_start_date(start_date: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated people.

    GET /people/updates/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/people/updates/{start_date}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_people_updates_id_by_start_date(start_date: str, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated people Trakt IDs.

    GET /people/updates/id/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/people/updates/id/{start_date}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_search_by_id_type_by_id(id_type: str, id: str, type: str | None = None, page: int | None = None, limit: int | None = None, extended: str | None = None) -> str:
    """Get ID lookup results.

    GET /search/{id_type}/{id}

    Args:
        id_type: External ID type to look up.
        id: External ID value.
        type: Optional media type filter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/search/{id_type}/{id}", query={"type": type, "page": page, "limit": limit, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_search_by_type(type: str, query: str | None = None, page: int | None = None, limit: int | None = None, extended: str | None = None) -> str:
    """Get text query results.

    GET /search/{type}

    Args:
        type: Specify the type of results by sending a single value or a comma delimited string for multiple types.
        query: The search query to search all text based fields.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/search/{type}", query={"query": query, "page": page, "limit": limit, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_search_by_type_exact(type: str, query: str | None = None, page: int | None = None, limit: int | None = None, extended: str | None = None) -> str:
    """Get exact text query results.

    GET /search/{type}/exact

    Args:
        type: Specify the type of results by sending a single value or a comma delimited string for multiple types.
        query: The search query to search all text based fields.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/search/{type}/exact", query={"query": query, "page": page, "limit": limit, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_search_recent_by_id_global_by_type(type: str, page: int | None = None, limit: int | None = None, query: str | None = None, extended: str | None = None) -> str:
    """Get trending search results.

    GET /search/recent_by_id/global/{type}

    Args:
        type: Specify the type of results by sending a single value or a comma delimited string for multiple types.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        query: The search query to search all text based fields.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/search/recent_by_id/global/{type}", query={"page": page, "limit": limit, "query": query, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id(id: str, extended: str | None = None) -> str:
    """Get a single show.

    GET /shows/{id}

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_aliases(id: str) -> str:
    """Get all show aliases.

    GET /shows/{id}/aliases

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/aliases", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_certifications(id: str) -> str:
    """Get all show certifications.

    GET /shows/{id}/certifications

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/certifications", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_comments_by_sort(id: str, sort: str, extended: str | None = None, page: int | None = None, limit: str | None = None, language: str | None = None) -> str:
    """Get all show comments.

    GET /shows/{id}/comments/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        language: Filter comments to a 2 character language code
    """
    return call("GET", f"/shows/{id}/comments/{sort}", query={"extended": extended, "page": page, "limit": limit, "language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_last_episode(id: str, extended: str | None = None) -> str:
    """Get last episode.

    GET /shows/{id}/last_episode

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/last_episode", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_lists_by_type_by_sort(id: str, sort: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get lists containing this show.

    GET /shows/{id}/lists/{type}/{sort}

    Args:
        id: The id/slug of the resource.
        sort: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/{id}/lists/{type}/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_next_episode(id: str, extended: str | None = None) -> str:
    """Get next episode.

    GET /shows/{id}/next_episode

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/next_episode", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_people(id: str, extended: str | None = None) -> str:
    """Get all people for a show.

    GET /shows/{id}/people

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/people", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_progress_collection(id: str, extended: str | None = None, hidden: bool | None = None, specials: bool | None = None, count_specials: bool | None = None, include_stats: bool | None = None) -> str:
    """Get show collection progress.

    GET /shows/{id}/progress/collection

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        hidden: Whether to include any hidden seasons
        specials: Whether to include special seasons as season 0.
        count_specials: Whether to count specials in the overall stats (only applies if specials are included).
        include_stats: Whether to include stats in the response
    """
    return call("GET", f"/shows/{id}/progress/collection", query={"extended": extended, "hidden": hidden, "specials": specials, "count_specials": count_specials, "include_stats": include_stats}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_progress_watched(id: str, extended: str | None = None, hidden: bool | None = None, specials: bool | None = None, count_specials: bool | None = None, include_stats: bool | None = None) -> str:
    """Get show watched progress.

    GET /shows/{id}/progress/watched

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        hidden: Whether to include any hidden seasons
        specials: Whether to include special seasons as season 0.
        count_specials: Whether to count specials in the overall stats (only applies if specials are included).
        include_stats: Whether to include stats in the response
    """
    return call("GET", f"/shows/{id}/progress/watched", query={"extended": extended, "hidden": hidden, "specials": specials, "count_specials": count_specials, "include_stats": include_stats}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_ratings(id: str, extended: str | None = None) -> str:
    """Get show ratings.

    GET /shows/{id}/ratings

    Args:
        id: The id/slug of the resource.
        extended: Use `all` to include ratings from supported external sources.
    """
    return call("GET", f"/shows/{id}/ratings", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_related(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get related shows.

    GET /shows/{id}/related

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/{id}/related", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons(id: str, extended: str | None = None) -> str:
    """Get all seasons for a show.

    GET /shows/{id}/seasons

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season(id: str, season: int, extended: str | None = None) -> str:
    """Get all episodes for a single season.

    GET /shows/{id}/seasons/{season}

    Args:
        id: The id/slug of the resource.
        season: Season number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_comments_by_sort(id: str, season: int, sort: str, extended: str | None = None, page: int | None = None, limit: str | None = None, language: str | None = None) -> str:
    """Get all season comments.

    GET /shows/{id}/seasons/{season}/comments/{sort}

    Args:
        id: The id/slug of the resource.
        season: Season number
        sort: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        language: Filter comments to a 2 character language code
    """
    return call("GET", f"/shows/{id}/seasons/{season}/comments/{sort}", query={"extended": extended, "page": page, "limit": limit, "language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode(id: str, season: int, episode: int, extended: str | None = None) -> str:
    """Get a single episode for a show.

    GET /shows/{id}/seasons/{season}/episodes/{episode}

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_comments_by_sort(id: str, season: int, episode: int, sort: str, extended: str | None = None, page: int | None = None, limit: str | None = None, language: str | None = None) -> str:
    """Get all episode comments.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort}

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        sort: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
        language: Filter comments to a 2 character language code
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort}", query={"extended": extended, "page": page, "limit": limit, "language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_lists_by_type_by_sort(id: str, season: int, episode: int, sort: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get lists containing this episode.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort}

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        sort: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_people(id: str, season: int, episode: int, extended: str | None = None) -> str:
    """Get all people for an episode.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/people

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/people", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_ratings(id: str, season: int, episode: int, extended: str | None = None) -> str:
    """Get episode ratings.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/ratings

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        extended: Use `all` to include ratings from supported external sources.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/ratings", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_stats(id: str, season: int, episode: int) -> str:
    """Get episode stats.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/stats

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_translations(id: str, season: int, episode: int, language: str | None = None) -> str:
    """Get all episode translations.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/translations

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        language: Filter translations to a 2 character language code
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/translations", query={"language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_videos(id: str, season: int, episode: int) -> str:
    """Get all videos.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/videos

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/videos", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_watching(id: str, season: int, episode: int, extended: str | None = None) -> str:
    """Get users watching right now.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/watching

    Args:
        id: The id/slug of the resource.
        season: Season number
        episode: Episode number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/watching", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_episodes_by_episode_watchnow_by_country(id: str, country: str, season: int, episode: int, links: str | None = None, extended: str | None = None) -> str:
    """Get episode watch now sources.

    GET /shows/{id}/seasons/{season}/episodes/{episode}/watchnow/{country}

    Args:
        id: The id/slug of the resource.
        country: 2 character country code.
        season: Season number
        episode: Episode number
        links: Query parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/episodes/{episode}/watchnow/{country}", query={"links": links, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_info(id: str, season: int, extended: str | None = None) -> str:
    """Get single seasons for a show.

    GET /shows/{id}/seasons/{season}/info

    Args:
        id: The id/slug of the resource.
        season: Season number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/info", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_lists_by_type_by_sort(id: str, season: int, sort: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get lists containing this season.

    GET /shows/{id}/seasons/{season}/lists/{type}/{sort}

    Args:
        id: The id/slug of the resource.
        season: Season number
        sort: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/lists/{type}/{sort}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_people(id: str, season: int, extended: str | None = None) -> str:
    """Get all people for a season.

    GET /shows/{id}/seasons/{season}/people

    Args:
        id: The id/slug of the resource.
        season: Season number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/people", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_ratings(id: str, season: int, extended: str | None = None) -> str:
    """Get season ratings.

    GET /shows/{id}/seasons/{season}/ratings

    Args:
        id: The id/slug of the resource.
        season: Season number
        extended: Use `all` to include ratings from supported external sources.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/ratings", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_stats(id: str, season: int) -> str:
    """Get season stats.

    GET /shows/{id}/seasons/{season}/stats

    Args:
        id: The id/slug of the resource.
        season: Season number
    """
    return call("GET", f"/shows/{id}/seasons/{season}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_translations(id: str, season: int, language: str | None = None) -> str:
    """Get all season translations.

    GET /shows/{id}/seasons/{season}/translations

    Args:
        id: The id/slug of the resource.
        season: Season number
        language: Filter translations to a 2 character language code
    """
    return call("GET", f"/shows/{id}/seasons/{season}/translations", query={"language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_videos(id: str, season: int) -> str:
    """Get all videos.

    GET /shows/{id}/seasons/{season}/videos

    Args:
        id: The id/slug of the resource.
        season: Season number
    """
    return call("GET", f"/shows/{id}/seasons/{season}/videos", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_watching(id: str, season: int, extended: str | None = None) -> str:
    """Get users watching right now.

    GET /shows/{id}/seasons/{season}/watching

    Args:
        id: The id/slug of the resource.
        season: Season number
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/watching", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_seasons_by_season_watchnow_justwatch_links_by_country(season: str, country: str, id: str) -> str:
    """Get season JustWatch links.

    GET /shows/{id}/seasons/{season}/watchnow/justwatch_links/{country}

    Args:
        season: Path parameter.
        country: Path parameter.
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/seasons/{season}/watchnow/justwatch_links/{country}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_sentiments(id: str) -> str:
    """Get show sentiments.

    GET /shows/{id}/sentiments

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/sentiments", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_stats(id: str) -> str:
    """Get show stats.

    GET /shows/{id}/stats

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_studios(id: str) -> str:
    """Get show studios.

    GET /shows/{id}/studios

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/studios", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_translations(id: str, language: str | None = None) -> str:
    """Get all show translations.

    GET /shows/{id}/translations

    Args:
        id: The id/slug of the resource.
        language: Filter translations to a 2 character language code
    """
    return call("GET", f"/shows/{id}/translations", query={"language": language}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_videos(id: str) -> str:
    """Get all videos.

    GET /shows/{id}/videos

    Args:
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/videos", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_watching(id: str, extended: str | None = None) -> str:
    """Get users watching right now.

    GET /shows/{id}/watching

    Args:
        id: The id/slug of the resource.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/watching", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_watchnow_by_country(id: str, country: str, links: str | None = None, extended: str | None = None) -> str:
    """Get show watch now sources.

    GET /shows/{id}/watchnow/{country}

    Args:
        id: The id/slug of the resource.
        country: 2 character country code.
        links: Query parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/shows/{id}/watchnow/{country}", query={"links": links, "extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_by_id_watchnow_justwatch_links_by_country(country: str, id: str) -> str:
    """Get show JustWatch links.

    GET /shows/{id}/watchnow/justwatch_links/{country}

    Args:
        country: Path parameter.
        id: The id/slug of the resource.
    """
    return call("GET", f"/shows/{id}/watchnow/justwatch_links/{country}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_collected_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most collected shows.

    GET /shows/collected/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/shows/collected/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_favorited_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most favorited shows.

    GET /shows/favorited/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/shows/favorited/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_played_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most played shows.

    GET /shows/played/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/shows/played/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_streaming_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get streaming shows.

    GET /shows/streaming/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/shows/streaming/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_updates_by_start_date(start_date: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated shows.

    GET /shows/updates/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/updates/{start_date}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_updates_id_by_start_date(start_date: str, page: int | None = None, limit: int | None = None) -> str:
    """Get recently updated show Trakt IDs.

    GET /shows/updates/id/{start_date}

    Args:
        start_date: UTC date to start checking for updates.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/shows/updates/id/{start_date}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_shows_watched_by_period(period: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most watched shows.

    GET /shows/watched/{period}

    Args:
        period: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", f"/shows/watched/{period}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_smart_lists_by_list_id(list_id: str) -> str:
    """Get smart list.

    GET /smart-lists/{list_id}

    Args:
        list_id: Path parameter.
    """
    return call("GET", f"/smart-lists/{list_id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_smart_lists_by_list_id_items(list_id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get smart list items.

    GET /smart-lists/{list_id}/items

    Args:
        list_id: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/smart-lists/{list_id}/items", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_collection_by_type(type: str, extended: str | None = None, available_on: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get collection.

    GET /sync/collection/{type}

    Args:
        type: Sync media type filter.
        extended: Extended information to include in the response.
        available_on: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/sync/collection/{type}", query={"extended": extended, "available_on": available_on, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_favorites_by_type_by_sort_by_by_sort_how(type: str, sort_by: str, sort_how: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get favorites.

    GET /sync/favorites/{type}/{sort_by}/{sort_how}

    Args:
        type: Sync media type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/sync/favorites/{type}/{sort_by}/{sort_how}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_history_by_type_by_id(type: str, id: str, extended: str | None = None, page: int | None = None, limit: int | None = None, start_at: str | None = None, end_at: str | None = None) -> str:
    """Get watched history.

    GET /sync/history/{type}/{id}

    Args:
        type: Sync media type filter.
        id: Trakt ID for a specific item.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
    """
    return call("GET", f"/sync/history/{type}/{id}", query={"extended": extended, "page": page, "limit": limit, "start_at": start_at, "end_at": end_at}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_playback_by_type(type: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, start_at: str | None = None, end_at: str | None = None) -> str:
    """Get playback progress.

    GET /sync/playback/{type}

    Args:
        type: Sync media type filter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
    """
    return call("GET", f"/sync/playback/{type}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "start_at": start_at, "end_at": end_at}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_ratings_by_type_by_rating(type: str, rating: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get ratings.

    GET /sync/ratings/{type}/{rating}

    Args:
        type: Sync media type filter.
        rating: Rating filter from 1 to 10.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/sync/ratings/{type}/{rating}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_watched_by_type(type: str, extended: str | None = None) -> str:
    """Get watched.

    GET /sync/watched/{type}

    Args:
        type: Sync media type filter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/sync/watched/{type}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_sync_watchlist_by_type_by_sort_by_by_sort_how(type: str, sort_by: str, sort_how: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get watchlist.

    GET /sync/watchlist/{type}/{sort_by}/{sort_how}

    Args:
        type: Sync media type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/sync/watchlist/{type}/{sort_by}/{sort_how}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id(id: str, extended: str | None = None) -> str:
    """Get user profile.

    GET /users/{id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_by_type_activities(id: str, type: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get social activity.

    GET /users/{id}/{type}/activities

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: Path parameter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/{type}/activities", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_collection_by_type(id: str, type: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get collection.

    GET /users/{id}/collection/{type}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: User media type filter.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/collection/{type}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_comments_by_comment_type_by_type(id: str, comment_type: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None, include_replies: str | None = None) -> str:
    """Get comments.

    GET /users/{id}/comments/{comment_type}/{type}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        comment_type: Path parameter.
        type: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        include_replies: Query parameter.
    """
    return call("GET", f"/users/{id}/comments/{comment_type}/{type}", query={"extended": extended, "page": page, "limit": limit, "include_replies": include_replies}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_favorites_by_type_by_sort_by_by_sort_how(id: str, type: str, sort_by: str, sort_how: str, extended: str | None = None, sort_by_query: str | None = None, sort_how_query: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get favorites.

    GET /users/{id}/favorites/{type}/{sort_by}/{sort_how}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: Favorites media type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        sort_by_query: The field to sort by
        sort_how_query: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/favorites/{type}/{sort_by}/{sort_how}", query={"extended": extended, "sort_by": sort_by_query, "sort_how": sort_how_query, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_favorites_comments_by_sort(id: str, sort: str, page: int | None = None, limit: int | None = None) -> str:
    """Get all favorites comments.

    GET /users/{id}/favorites/comments/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/favorites/comments/{sort}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_favorites_media_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get favorite media.

    GET /users/{id}/favorites/media/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/favorites/media/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_favorites_movies_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get favorite movies.

    GET /users/{id}/favorites/movies/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/favorites/movies/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_favorites_shows_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get favorite shows.

    GET /users/{id}/favorites/shows/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/favorites/shows/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_followers(id: str, extended: str | None = None) -> str:
    """Get followers.

    GET /users/{id}/followers

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/followers", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_following(id: str, extended: str | None = None) -> str:
    """Get following.

    GET /users/{id}/following

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/following", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_friends(id: str, extended: str | None = None) -> str:
    """Get friends.

    GET /users/{id}/friends

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/friends", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history(id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get watched history.

    GET /users/{id}/history/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_by_type_by_item_id(id: str, item_id: str, type: str, extended: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get watched history.

    GET /users/{id}/history/{type}/{item_id}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        item_id: Path parameter.
        type: History media type filter.
        extended: Extended information to include in the response.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/{type}/{item_id}", query={"extended": extended, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_episodes(id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get episode watched history.

    GET /users/{id}/history/episodes

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/episodes", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_episodes_by_item_id(id: str, item_id: str, extended: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get history for an episode.

    GET /users/{id}/history/episodes/{item_id}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        item_id: Path parameter.
        extended: Extended information to include in the response.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/episodes/{item_id}", query={"extended": extended, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_movies(id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get movie watched history.

    GET /users/{id}/history/movies

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/movies", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_movies_by_item_id(id: str, item_id: str, extended: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get history for a movie.

    GET /users/{id}/history/movies/{item_id}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        item_id: Path parameter.
        extended: Extended information to include in the response.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/movies/{item_id}", query={"extended": extended, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_shows(id: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get show watched history.

    GET /users/{id}/history/shows

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/shows", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_history_shows_by_item_id(id: str, item_id: str, extended: str | None = None, start_at: str | None = None, end_at: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get history for a show.

    GET /users/{id}/history/shows/{item_id}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        item_id: Path parameter.
        extended: Extended information to include in the response.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/history/shows/{item_id}", query={"extended": extended, "start_at": start_at, "end_at": end_at, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_likes_by_type(id: str, type: str, extended: str | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get likes.

    GET /users/{id}/likes/{type}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: User media type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/likes/{type}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get a user's personal lists.

    GET /users/{id}/lists

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/lists", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id(id: str, list_id: str, extended: str | None = None) -> str:
    """Get personal list.

    GET /users/{id}/lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/lists/{list_id}/", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_comments_by_sort(id: str, list_id: str, sort: str, page: int | None = None, limit: int | None = None) -> str:
    """Get all list comments.

    GET /users/{id}/lists/{list_id}/comments/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        sort: Path parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/lists/{list_id}/comments/{sort}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_items_by_type_by_sort_by_by_sort_how(id: str, list_id: str, type: str, sort_by: str, sort_how: str, extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get items on a personal list.

    GET /users/{id}/lists/{list_id}/items/{type}/{sort_by}/{sort_how}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        type: List item type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/lists/{list_id}/items/{type}/{sort_by}/{sort_how}", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_items_movie(id: str, list_id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get movie list items.

    GET /users/{id}/lists/{list_id}/items/movie

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/lists/{list_id}/items/movie", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_items_movie_show(id: str, list_id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get media list items.

    GET /users/{id}/lists/{list_id}/items/movie,show

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/lists/{list_id}/items/movie,show", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_items_movie_show_season_episode(id: str, list_id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get all list items.

    GET /users/{id}/lists/{list_id}/items/movie,show,season,episode

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/lists/{list_id}/items/movie,show,season,episode", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_items_show(id: str, list_id: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get show list items.

    GET /users/{id}/lists/{list_id}/items/show

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", f"/users/{id}/lists/{list_id}/items/show", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_by_list_id_likes(id: str, list_id: str, page: int | None = None, limit: int | None = None) -> str:
    """Get all users who liked a list.

    GET /users/{id}/lists/{list_id}/likes

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/lists/{list_id}/likes", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_lists_collaborations(id: str, extended: str | None = None) -> str:
    """Get all lists a user can collaborate on.

    GET /users/{id}/lists/collaborations

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/lists/collaborations", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_mir_by_year_by_month(id: str, year: int, month: int, extended: str | None = None) -> str:
    """Get month in review.

    GET /users/{id}/mir/{year}/{month}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        year: Path parameter.
        month: Path parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/mir/{year}/{month}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_notes_by_type(id: str, type: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get notes.

    GET /users/{id}/notes/{type}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: User media type filter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/notes/{type}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_ratings(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get all ratings.

    GET /users/{id}/ratings/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/ratings/", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_ratings_by_type_by_rating(id: str, type: str, rating: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get ratings.

    GET /users/{id}/ratings/{type}/{rating}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: Rated media type filter.
        rating: Rating filter from 1 to 10.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/ratings/{type}/{rating}", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_ratings_episodes(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get episode ratings.

    GET /users/{id}/ratings/episodes

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/ratings/episodes", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_ratings_movies(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get movie ratings.

    GET /users/{id}/ratings/movies

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/ratings/movies", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_ratings_shows(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get show ratings.

    GET /users/{id}/ratings/shows

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/ratings/shows", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_smart_lists(id: str) -> str:
    """Get a user's smart lists.

    GET /users/{id}/smart-lists

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
    """
    return call("GET", f"/users/{id}/smart-lists", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_smart_lists_by_list_id(id: str, list_id: str) -> str:
    """Get smart list.

    GET /users/{id}/smart-lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
    """
    return call("GET", f"/users/{id}/smart-lists/{list_id}/", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_stats(id: str) -> str:
    """Get stats.

    GET /users/{id}/stats

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
    """
    return call("GET", f"/users/{id}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watched_by_type(id: str, type: str, extended: str | None = None, hidden: bool | None = None, specials: bool | None = None, count_specials: bool | None = None) -> str:
    """Get watched.

    GET /users/{id}/watched/{type}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: Watched media type filter.
        extended: Extended information to include in the response.
        hidden: Whether to include any hidden seasons
        specials: Whether to include special seasons as season 0.
        count_specials: Whether to count specials in the overall stats (only applies if specials are included).
    """
    return call("GET", f"/users/{id}/watched/{type}", query={"extended": extended, "hidden": hidden, "specials": specials, "count_specials": count_specials}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watched_movies(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get watched movies.

    GET /users/{id}/watched/movies

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/watched/movies", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watched_shows(id: str, extended: str | None = None, page: int | None = None, limit: int | None = None, specials: bool | None = None, season_numbers: bool | None = None) -> str:
    """Get watched shows.

    GET /users/{id}/watched/shows

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        specials: Whether to include special seasons as season 0.
        season_numbers: Query parameter.
    """
    return call("GET", f"/users/{id}/watched/shows", query={"extended": extended, "page": page, "limit": limit, "specials": specials, "season_numbers": season_numbers}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watching(id: str, extended: str | None = None) -> str:
    """Get watching.

    GET /users/{id}/watching

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/watching", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watchlist_by_type_by_sort_by_by_sort_how(id: str, type: str, sort_by: str, sort_how: str, extended: str | None = None, sort_by_query: str | None = None, sort_how_query: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, hide: str | None = None) -> str:
    """Get watchlist.

    GET /users/{id}/watchlist/{type}/{sort_by}/{sort_how}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        type: Watchlist media type filter.
        sort_by: Sort by a specific property.
        sort_how: Sort direction.
        extended: Extended information to include in the response.
        sort_by_query: The field to sort by
        sort_how_query: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        hide: Query parameter.
    """
    return call("GET", f"/users/{id}/watchlist/{type}/{sort_by}/{sort_how}", query={"extended": extended, "sort_by": sort_by_query, "sort_how": sort_how_query, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "hide": hide}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watchlist_comments_by_sort(id: str, sort: str, page: int | None = None, limit: int | None = None) -> str:
    """Get all watchlist comments.

    GET /users/{id}/watchlist/comments/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/{id}/watchlist/comments/{sort}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watchlist_movie_show_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, hide: str | None = None) -> str:
    """Get media watchlist.

    GET /users/{id}/watchlist/movie,show/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        hide: Query parameter.
    """
    return call("GET", f"/users/{id}/watchlist/movie,show/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "hide": hide}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watchlist_movies_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, hide: str | None = None) -> str:
    """Get movie watchlist.

    GET /users/{id}/watchlist/movies/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        hide: Query parameter.
    """
    return call("GET", f"/users/{id}/watchlist/movies/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "hide": hide}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_watchlist_shows_by_sort(id: str, sort: str, extended: str | None = None, sort_by: str | None = None, sort_how: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, hide: str | None = None) -> str:
    """Get show watchlist.

    GET /users/{id}/watchlist/shows/{sort}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        sort: Path parameter.
        extended: Extended information to include in the response.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        hide: Query parameter.
    """
    return call("GET", f"/users/{id}/watchlist/shows/{sort}", query={"extended": extended, "sort_by": sort_by, "sort_how": sort_how, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "hide": hide}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_yir_by_year(id: str, year: int, extended: str | None = None) -> str:
    """Get year in review.

    GET /users/{id}/yir/{year}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        year: Path parameter.
        extended: Extended information to include in the response.
    """
    return call("GET", f"/users/{id}/yir/{year}", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_hidden_by_section(section: str, extended: str | None = None, page: int | None = None, limit: int | None = None, type: str | None = None) -> str:
    """Get hidden items.

    GET /users/hidden/{section}

    Args:
        section: Path parameter.
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        type: Hidden item type filter.
    """
    return call("GET", f"/users/hidden/{section}", query={"extended": extended, "page": page, "limit": limit, "type": type}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_saved_filters_by_section(section: str, page: int | None = None, limit: int | None = None) -> str:
    """Get saved filters.

    GET /users/saved_filters/{section}

    Args:
        section: Path parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/saved_filters/{section}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_settings_plex_servers_by_server_id(server_id: str) -> str:
    """Get Plex server accounts and libraries.

    GET /users/settings/plex/servers/{server_id}

    Args:
        server_id: The Plex server machine identifier.
    """
    return call("GET", f"/users/settings/plex/servers/{server_id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_syncs_by_id(id: int) -> str:
    """Get a data sync.

    GET /users/syncs/{id}

    Args:
        id: The numeric sync id, scoped to the authenticated user. A numeric segment hits a single sync; a non-numeric segment is the filtered list.
    """
    return call("GET", f"/users/syncs/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_syncs_by_id_paused(id: int, page: int | None = None, limit: int | None = None) -> str:
    """Get paused sync items.

    GET /users/syncs/{id}/paused

    Args:
        id: The numeric sync id, scoped to the authenticated user. A numeric segment hits a single sync; a non-numeric segment is the filtered list.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/syncs/{id}/paused", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_syncs_by_id_skipped(id: int, page: int | None = None, limit: int | None = None) -> str:
    """Get skipped sync items.

    GET /users/syncs/{id}/skipped

    Args:
        id: The numeric sync id, scoped to the authenticated user. A numeric segment hits a single sync; a non-numeric segment is the filtered list.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/syncs/{id}/skipped", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_syncs_by_type(type: str, page: int | None = None, limit: int | None = None) -> str:
    """Get data syncs by type.

    GET /users/syncs/{type}

    Args:
        type: Filter syncs by the app that created them. An unknown type returns `404` rather than silently returning everything.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", f"/users/syncs/{type}", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_watchnow_sources_by_country_code(country_code: str) -> str:
    """Get watch now sources by country.

    GET /watchnow/sources/{countryCode}

    Args:
        country_code: Path parameter.
    """
    return call("GET", f"/watchnow/sources/{country_code}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_certifications_movies() -> str:
    """Get movie certifications.

    GET /certifications/movies
    """
    return call("GET", "/certifications/movies", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_certifications_shows() -> str:
    """Get show certifications.

    GET /certifications/shows
    """
    return call("GET", "/certifications/shows", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_lists_popular(extended: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get popular lists.

    GET /lists/popular

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", "/lists/popular", query={"extended": extended, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_lists_trending(extended: str | None = None, page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get trending lists.

    GET /lists/trending

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", "/lists/trending", query={"extended": extended, "page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_media_anticipated(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get anticipated media.

    GET /media/anticipated

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/media/anticipated", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_media_popular(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get popular media.

    GET /media/popular

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/media/popular", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_media_trending(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get trending media.

    GET /media/trending

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/media/trending", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_movies_anticipated(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most anticipated movies.

    GET /movies/anticipated

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/movies/anticipated", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_movies_boxoffice(extended: str | None = None) -> str:
    """Get the weekend box office.

    GET /movies/boxoffice

    Args:
        extended: Extended information to include in the response.
    """
    return call("GET", "/movies/boxoffice", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_movies_hot(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get hot movies.

    GET /movies/hot

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/movies/hot", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_movies_popular(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get popular movies.

    GET /movies/popular

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/movies/popular", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_movies_trending(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get trending movies.

    GET /movies/trending

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/movies/trending", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_networks() -> str:
    """Get networks.

    GET /networks
    """
    return call("GET", "/networks", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_oauth_authorize(response_type: str | None = None, client_id: str | None = None, redirect_uri: str | None = None, state: str | None = None) -> str:
    """Authorize Application.

    GET /oauth/authorize

    Args:
        response_type: Query parameter.
        client_id: Query parameter.
        redirect_uri: Query parameter.
        state: Query parameter.
    """
    return call("GET", "/oauth/authorize", query={"response_type": response_type, "client_id": client_id, "redirect_uri": redirect_uri, "state": state}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_recommendations_movies(extended: str | None = None, limit: int | None = None, watch_window: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get movie recommendations.

    GET /recommendations/movies/

    Args:
        extended: Extended information to include in the response.
        limit: Limit the number of results.
        watch_window: The watch window in days for the recommendations.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", "/recommendations/movies/", query={"extended": extended, "limit": limit, "watch_window": watch_window, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_recommendations_shows(extended: str | None = None, limit: int | None = None, watch_window: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None) -> str:
    """Get show recommendations.

    GET /recommendations/shows/

    Args:
        extended: Extended information to include in the response.
        limit: Limit the number of results.
        watch_window: The watch window in days for the recommendations.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
    """
    return call("GET", "/recommendations/shows/", query={"extended": extended, "limit": limit, "watch_window": watch_window, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_shows_anticipated(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get the most anticipated shows.

    GET /shows/anticipated

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/shows/anticipated", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_shows_hot(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get hot shows.

    GET /shows/hot

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/shows/hot", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_shows_popular(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get popular shows.

    GET /shows/popular

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/shows/popular", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_shows_trending(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get trending shows.

    GET /shows/trending

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/shows/trending", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_social_recommendations_movies(extended: str | None = None, limit: int | None = None, watch_window: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get social movie recommendations.

    GET /social_recommendations/movies/

    Args:
        extended: Extended information to include in the response.
        limit: Limit the number of results.
        watch_window: The watch window in days for the recommendations.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/social_recommendations/movies/", query={"extended": extended, "limit": limit, "watch_window": watch_window, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_social_recommendations_shows(extended: str | None = None, limit: int | None = None, watch_window: int | None = None, ignore_watched: bool | None = None, ignore_collected: bool | None = None, ignore_watchlisted: bool | None = None) -> str:
    """Get social show recommendations.

    GET /social_recommendations/shows/

    Args:
        extended: Extended information to include in the response.
        limit: Limit the number of results.
        watch_window: The watch window in days for the recommendations.
        ignore_watched: Ignore watched items.
        ignore_collected: Ignore collected items.
        ignore_watchlisted: Ignore watchlisted items.
    """
    return call("GET", "/social_recommendations/shows/", query={"extended": extended, "limit": limit, "watch_window": watch_window, "ignore_watched": ignore_watched, "ignore_collected": ignore_collected, "ignore_watchlisted": ignore_watchlisted}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_episodes(extended: str | None = None, available_on: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get episode collection.

    GET /sync/collection/episodes

    Args:
        extended: Extended information to include in the response.
        available_on: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", "/sync/collection/episodes", query={"extended": extended, "available_on": available_on, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_media(extended: str | None = None, available_on: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get media collection.

    GET /sync/collection/media

    Args:
        extended: Extended information to include in the response.
        available_on: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", "/sync/collection/media", query={"extended": extended, "available_on": available_on, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_minimal_episodes(available_on: str | None = None) -> str:
    """Get minimal episode collection.

    GET /sync/collection/minimal/episodes

    Args:
        available_on: Query parameter.
    """
    return call("GET", "/sync/collection/minimal/episodes", query={"available_on": available_on}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_minimal_movies(available_on: str | None = None) -> str:
    """Get minimal movie collection.

    GET /sync/collection/minimal/movies

    Args:
        available_on: Query parameter.
    """
    return call("GET", "/sync/collection/minimal/movies", query={"available_on": available_on}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_minimal_shows(available_on: str | None = None) -> str:
    """Get minimal show collection.

    GET /sync/collection/minimal/shows

    Args:
        available_on: Query parameter.
    """
    return call("GET", "/sync/collection/minimal/shows", query={"available_on": available_on}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_movies(extended: str | None = None, available_on: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get movie collection.

    GET /sync/collection/movies

    Args:
        extended: Extended information to include in the response.
        available_on: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", "/sync/collection/movies", query={"extended": extended, "available_on": available_on, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_collection_shows(extended: str | None = None, available_on: str | None = None) -> str:
    """Get show collection.

    GET /sync/collection/shows

    Args:
        extended: Extended information to include in the response.
        available_on: Query parameter.
    """
    return call("GET", "/sync/collection/shows", query={"extended": extended, "available_on": available_on}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_last_activities() -> str:
    """Get last activity.

    GET /sync/last_activities
    """
    return call("GET", "/sync/last_activities", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_playback_movies(extended: str | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, page: int | None = None, limit: int | None = None, start_at: str | None = None, end_at: str | None = None) -> str:
    """Get movie playback progress.

    GET /sync/playback/movies

    Args:
        extended: Extended information to include in the response.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        start_at: Start date for the range. Must be formatted as "YYYY-MM-DD".
        end_at: End date for the range. Must be formatted as "YYYY-MM-DD".
    """
    return call("GET", "/sync/playback/movies", query={"extended": extended, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "page": page, "limit": limit, "start_at": start_at, "end_at": end_at}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_progress_up_next(extended: str | None = None, page: int | None = None, limit: int | None = None, sort_by: str | None = None, sort_how: str | None = None, include_stats: bool | None = None, lifetime_stats: bool | None = None) -> str:
    """Get up next.

    GET /sync/progress/up_next

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        include_stats: Whether to include stats in the response
        lifetime_stats: When true, `progress.completed` and `progress.stats` reflect lifetime totals across all watches of the show. When false (default), they reflect the current watching session — i.e. counters reset by `/shows/:id/progress/watched/reset`.
    """
    return call("GET", "/sync/progress/up_next", query={"extended": extended, "page": page, "limit": limit, "sort_by": sort_by, "sort_how": sort_how, "include_stats": include_stats, "lifetime_stats": lifetime_stats}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_progress_up_next_nitro(page: int | None = None, limit: int | None = None, watchnow: str | None = None, genres: str | None = None, subgenres: str | None = None, years: str | None = None, ratings: str | None = None, start_date: str | None = None, end_date: str | None = None, runtimes: str | None = None, countries: str | None = None, certifications: str | None = None, sort_by: str | None = None, sort_how: str | None = None, intent: str | None = None) -> str:
    """Get up next nitro.

    GET /sync/progress/up_next_nitro

    Args:
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        watchnow: Use "favorites" for streaming on a favorite service of the user.
      Use "any" for streaming on any service in the user's country.
      Use "any_all" for streaming on any service in all countries.
      Use "free" for streaming for free in the user's country.
      Use "free_all" for streaming for free in all countries.
      Use "subscriptions" for streaming on any subscription service (Netflix, Hulu, etc) in the user's country.
      Use "subscriptions_all" streaming on any subscription service in all countries
        genres: Query parameter.
        subgenres: Query parameter.
        years: Query parameter.
        ratings: Query parameter.
        start_date: Query parameter.
        end_date: Query parameter.
        runtimes: Query parameter.
        countries: Query parameter.
        certifications: Query parameter.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        intent: To get shows a user is just starting, continuing, completed, or all shows.
    """
    return call("GET", "/sync/progress/up_next_nitro", query={"page": page, "limit": limit, "watchnow": watchnow, "genres": genres, "subgenres": subgenres, "years": years, "ratings": ratings, "start_date": start_date, "end_date": end_date, "runtimes": runtimes, "countries": countries, "certifications": certifications, "sort_by": sort_by, "sort_how": sort_how, "intent": intent}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sync_progress_watched(extended: str | None = None, page: int | None = None, limit: int | None = None, sort_by: str | None = None, sort_how: str | None = None, lifetime_stats: bool | None = None, hide_completed: bool | None = None, hide_not_completed: bool | None = None, only_rewatching: bool | None = None) -> str:
    """Get watched progress.

    GET /sync/progress/watched

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        sort_by: The field to sort by
        sort_how: The direction to sort in
        lifetime_stats: When true, `progress.completed` and `progress.stats` reflect lifetime totals across all watches of the show. When false (default), they reflect the current watching session — i.e. counters reset by `/shows/:id/progress/watched/reset`.
        hide_completed: Query parameter.
        hide_not_completed: Query parameter.
        only_rewatching: When true, restrict the list to shows the user is currently rewatching (i.e. those with an active `progress.reset_at`).
    """
    return call("GET", "/sync/progress/watched", query={"extended": extended, "page": page, "limit": limit, "sort_by": sort_by, "sort_how": sort_how, "lifetime_stats": lifetime_stats, "hide_completed": hide_completed, "hide_not_completed": hide_not_completed, "only_rewatching": only_rewatching}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_team(extended: str | None = None) -> str:
    """Get team members.

    GET /team/

    Args:
        extended: Extended information to include in the response.
    """
    return call("GET", "/team/", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_blocked() -> str:
    """Get blocked users.

    GET /users/blocked
    """
    return call("GET", "/users/blocked", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_hidden_dropped(extended: str | None = None, page: int | None = None, limit: int | None = None) -> str:
    """Get dropped shows.

    GET /users/hidden/dropped

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", "/users/hidden/dropped", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_hidden_progress_watched(extended: str | None = None, page: int | None = None, limit: int | None = None, type: str | None = None) -> str:
    """Get hidden progress items.

    GET /users/hidden/progress_watched

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
        type: Query parameter.
    """
    return call("GET", "/users/hidden/progress_watched", query={"extended": extended, "page": page, "limit": limit, "type": type}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_reactions_comments(extended: str | None = None, page: int | None = None, limit: str | None = None) -> str:
    """Get comment reactions.

    GET /users/reactions/comments

    Args:
        extended: Extended information to include in the response.
        page: The page number to retrieve
        limit: The number of items per page, can be a number or the value all
    """
    return call("GET", "/users/reactions/comments", query={"extended": extended, "page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_requests(extended: str | None = None) -> str:
    """Get follow requests.

    GET /users/requests/

    Args:
        extended: Extended information to include in the response.
    """
    return call("GET", "/users/requests/", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_requests_following(extended: str | None = None) -> str:
    """Get pending following requests.

    GET /users/requests/following

    Args:
        extended: Extended information to include in the response.
    """
    return call("GET", "/users/requests/following", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_settings(extended: str | None = None) -> str:
    """Retrieve settings.

    GET /users/settings

    Args:
        extended: Extended information to include in the response.
    """
    return call("GET", "/users/settings", query={"extended": extended}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_settings_plex() -> str:
    """Get Plex settings.

    GET /users/settings/plex/
    """
    return call("GET", "/users/settings/plex/", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_settings_plex_servers() -> str:
    """Get Plex servers.

    GET /users/settings/plex/servers
    """
    return call("GET", "/users/settings/plex/servers", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_syncs(page: int | None = None, limit: int | None = None) -> str:
    """Get data syncs.

    GET /users/syncs/

    Args:
        page: The page number to retrieve
        limit: The number of items per page. Defaults and maximums vary by endpoint. When pagination parameters are omitted, a low default limit is applied (often 10). When a limit is provided, it is capped at the endpoint maximum (often 250); higher values are clamped rather than rejected.
    """
    return call("GET", "/users/syncs/", query={"page": page, "limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_watchnow_sources() -> str:
    """Get watch now sources.

    GET /watchnow/sources
    """
    return call("GET", "/watchnow/sources", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_younify_connections() -> str:
    """Get streaming connections.

    GET /younify/connections
    """
    return call("GET", "/younify/connections", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def update_comments_by_id(id: str, body: dict) -> str:
    """Update a comment or reply.

    PUT /comments/{id}/

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/comments/{id}/", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_notes_by_id(id: str, body: dict) -> str:
    """Update a note.

    PUT /notes/{id}

    Args:
        id: The id/slug of the resource.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/notes/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_sync_favorites(body: dict) -> str:
    """Update favorites.

    PUT /sync/favorites

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/sync/favorites", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_sync_favorites_by_list_item_id(list_item_id: str, body: dict) -> str:
    """Update a favorite item.

    PUT /sync/favorites/{list_item_id}

    Args:
        list_item_id: List item ID.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/sync/favorites/{list_item_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_sync_watchlist(body: dict) -> str:
    """Update watchlist.

    PUT /sync/watchlist

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/sync/watchlist", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_sync_watchlist_by_list_item_id(list_item_id: str, body: dict) -> str:
    """Update a watchlist item.

    PUT /sync/watchlist/{list_item_id}

    Args:
        list_item_id: List item ID.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/sync/watchlist/{list_item_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_avatar(body: dict) -> str:
    """Update avatar.

    PUT /users/avatar

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/users/avatar", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_by_id_lists_by_list_id(id: str, list_id: str, body: dict) -> str:
    """Update personal list.

    PUT /users/{id}/lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/users/{id}/lists/{list_id}/", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_by_id_lists_by_list_id_items_by_list_item_id(id: str, list_id: str, list_item_id: str, body: dict) -> str:
    """Update a list item.

    PUT /users/{id}/lists/{list_id}/items/{list_item_id}

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        list_item_id: List item ID.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/users/{id}/lists/{list_id}/items/{list_item_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_by_id_smart_lists_by_list_id(id: str, list_id: str, body: dict) -> str:
    """Update smart list.

    PUT /users/{id}/smart-lists/{list_id}/

    Args:
        id: The slug that identifies the user, or "me" for the authenticated user.
        list_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/users/{id}/smart-lists/{list_id}/", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_set_cover(body: dict) -> str:
    """Update cover image.

    PUT /users/set_cover

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/users/set_cover", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_settings(body: dict) -> str:
    """Update settings.

    PUT /users/settings

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/users/settings", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def update_users_settings_plex(body: dict) -> str:
    """Update Plex settings.

    PUT /users/settings/plex/

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/users/settings/plex/", query=None, body=body, form=None)
