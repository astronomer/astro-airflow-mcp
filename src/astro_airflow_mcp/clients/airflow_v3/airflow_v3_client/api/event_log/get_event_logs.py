import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_log_collection_response import EventLogCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    run_id: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    try_number: int | None | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    event: None | str | Unset = UNSET,
    excluded_events: list[str] | None | Unset = UNSET,
    included_events: list[str] | None | Unset = UNSET,
    before: datetime.datetime | None | Unset = UNSET,
    after: datetime.datetime | None | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    owner_pattern: None | str | Unset = UNSET,
    event_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_dag_id: None | str | Unset
    if isinstance(dag_id, Unset):
        json_dag_id = UNSET
    else:
        json_dag_id = dag_id
    params["dag_id"] = json_dag_id

    json_task_id: None | str | Unset
    if isinstance(task_id, Unset):
        json_task_id = UNSET
    else:
        json_task_id = task_id
    params["task_id"] = json_task_id

    json_run_id: None | str | Unset
    if isinstance(run_id, Unset):
        json_run_id = UNSET
    else:
        json_run_id = run_id
    params["run_id"] = json_run_id

    json_map_index: int | None | Unset
    if isinstance(map_index, Unset):
        json_map_index = UNSET
    else:
        json_map_index = map_index
    params["map_index"] = json_map_index

    json_try_number: int | None | Unset
    if isinstance(try_number, Unset):
        json_try_number = UNSET
    else:
        json_try_number = try_number
    params["try_number"] = json_try_number

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_event: None | str | Unset
    if isinstance(event, Unset):
        json_event = UNSET
    else:
        json_event = event
    params["event"] = json_event

    json_excluded_events: list[str] | None | Unset
    if isinstance(excluded_events, Unset):
        json_excluded_events = UNSET
    elif isinstance(excluded_events, list):
        json_excluded_events = excluded_events

    else:
        json_excluded_events = excluded_events
    params["excluded_events"] = json_excluded_events

    json_included_events: list[str] | None | Unset
    if isinstance(included_events, Unset):
        json_included_events = UNSET
    elif isinstance(included_events, list):
        json_included_events = included_events

    else:
        json_included_events = included_events
    params["included_events"] = json_included_events

    json_before: None | str | Unset
    if isinstance(before, Unset):
        json_before = UNSET
    elif isinstance(before, datetime.datetime):
        json_before = before.isoformat()
    else:
        json_before = before
    params["before"] = json_before

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    elif isinstance(after, datetime.datetime):
        json_after = after.isoformat()
    else:
        json_after = after
    params["after"] = json_after

    json_dag_id_pattern: None | str | Unset
    if isinstance(dag_id_pattern, Unset):
        json_dag_id_pattern = UNSET
    else:
        json_dag_id_pattern = dag_id_pattern
    params["dag_id_pattern"] = json_dag_id_pattern

    json_task_id_pattern: None | str | Unset
    if isinstance(task_id_pattern, Unset):
        json_task_id_pattern = UNSET
    else:
        json_task_id_pattern = task_id_pattern
    params["task_id_pattern"] = json_task_id_pattern

    json_run_id_pattern: None | str | Unset
    if isinstance(run_id_pattern, Unset):
        json_run_id_pattern = UNSET
    else:
        json_run_id_pattern = run_id_pattern
    params["run_id_pattern"] = json_run_id_pattern

    json_owner_pattern: None | str | Unset
    if isinstance(owner_pattern, Unset):
        json_owner_pattern = UNSET
    else:
        json_owner_pattern = owner_pattern
    params["owner_pattern"] = json_owner_pattern

    json_event_pattern: None | str | Unset
    if isinstance(event_pattern, Unset):
        json_event_pattern = UNSET
    else:
        json_event_pattern = event_pattern
    params["event_pattern"] = json_event_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/eventLogs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EventLogCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPExceptionResponse.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    run_id: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    try_number: int | None | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    event: None | str | Unset = UNSET,
    excluded_events: list[str] | None | Unset = UNSET,
    included_events: list[str] | None | Unset = UNSET,
    before: datetime.datetime | None | Unset = UNSET,
    after: datetime.datetime | None | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    owner_pattern: None | str | Unset = UNSET,
    event_pattern: None | str | Unset = UNSET,
) -> Response[EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Event Logs

     Get all Event Logs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dttm, dag_id, task_id,
            run_id, event, logical_date, owner, extra, when, event_log_id`
        dag_id (None | str | Unset):
        task_id (None | str | Unset):
        run_id (None | str | Unset):
        map_index (int | None | Unset):
        try_number (int | None | Unset):
        owner (None | str | Unset):
        event (None | str | Unset):
        excluded_events (list[str] | None | Unset):
        included_events (list[str] | None | Unset):
        before (datetime.datetime | None | Unset):
        after (datetime.datetime | None | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        owner_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        event_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        owner=owner,
        event=event,
        excluded_events=excluded_events,
        included_events=included_events,
        before=before,
        after=after,
        dag_id_pattern=dag_id_pattern,
        task_id_pattern=task_id_pattern,
        run_id_pattern=run_id_pattern,
        owner_pattern=owner_pattern,
        event_pattern=event_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    run_id: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    try_number: int | None | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    event: None | str | Unset = UNSET,
    excluded_events: list[str] | None | Unset = UNSET,
    included_events: list[str] | None | Unset = UNSET,
    before: datetime.datetime | None | Unset = UNSET,
    after: datetime.datetime | None | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    owner_pattern: None | str | Unset = UNSET,
    event_pattern: None | str | Unset = UNSET,
) -> EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Event Logs

     Get all Event Logs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dttm, dag_id, task_id,
            run_id, event, logical_date, owner, extra, when, event_log_id`
        dag_id (None | str | Unset):
        task_id (None | str | Unset):
        run_id (None | str | Unset):
        map_index (int | None | Unset):
        try_number (int | None | Unset):
        owner (None | str | Unset):
        event (None | str | Unset):
        excluded_events (list[str] | None | Unset):
        included_events (list[str] | None | Unset):
        before (datetime.datetime | None | Unset):
        after (datetime.datetime | None | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        owner_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        event_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        owner=owner,
        event=event,
        excluded_events=excluded_events,
        included_events=included_events,
        before=before,
        after=after,
        dag_id_pattern=dag_id_pattern,
        task_id_pattern=task_id_pattern,
        run_id_pattern=run_id_pattern,
        owner_pattern=owner_pattern,
        event_pattern=event_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    run_id: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    try_number: int | None | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    event: None | str | Unset = UNSET,
    excluded_events: list[str] | None | Unset = UNSET,
    included_events: list[str] | None | Unset = UNSET,
    before: datetime.datetime | None | Unset = UNSET,
    after: datetime.datetime | None | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    owner_pattern: None | str | Unset = UNSET,
    event_pattern: None | str | Unset = UNSET,
) -> Response[EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Event Logs

     Get all Event Logs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dttm, dag_id, task_id,
            run_id, event, logical_date, owner, extra, when, event_log_id`
        dag_id (None | str | Unset):
        task_id (None | str | Unset):
        run_id (None | str | Unset):
        map_index (int | None | Unset):
        try_number (int | None | Unset):
        owner (None | str | Unset):
        event (None | str | Unset):
        excluded_events (list[str] | None | Unset):
        included_events (list[str] | None | Unset):
        before (datetime.datetime | None | Unset):
        after (datetime.datetime | None | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        owner_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        event_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        owner=owner,
        event=event,
        excluded_events=excluded_events,
        included_events=included_events,
        before=before,
        after=after,
        dag_id_pattern=dag_id_pattern,
        task_id_pattern=task_id_pattern,
        run_id_pattern=run_id_pattern,
        owner_pattern=owner_pattern,
        event_pattern=event_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    run_id: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    try_number: int | None | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    event: None | str | Unset = UNSET,
    excluded_events: list[str] | None | Unset = UNSET,
    included_events: list[str] | None | Unset = UNSET,
    before: datetime.datetime | None | Unset = UNSET,
    after: datetime.datetime | None | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    owner_pattern: None | str | Unset = UNSET,
    event_pattern: None | str | Unset = UNSET,
) -> EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Event Logs

     Get all Event Logs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dttm, dag_id, task_id,
            run_id, event, logical_date, owner, extra, when, event_log_id`
        dag_id (None | str | Unset):
        task_id (None | str | Unset):
        run_id (None | str | Unset):
        map_index (int | None | Unset):
        try_number (int | None | Unset):
        owner (None | str | Unset):
        event (None | str | Unset):
        excluded_events (list[str] | None | Unset):
        included_events (list[str] | None | Unset):
        before (datetime.datetime | None | Unset):
        after (datetime.datetime | None | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        owner_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        event_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventLogCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            owner=owner,
            event=event,
            excluded_events=excluded_events,
            included_events=included_events,
            before=before,
            after=after,
            dag_id_pattern=dag_id_pattern,
            task_id_pattern=task_id_pattern,
            run_id_pattern=run_id_pattern,
            owner_pattern=owner_pattern,
            event_pattern=event_pattern,
        )
    ).parsed
