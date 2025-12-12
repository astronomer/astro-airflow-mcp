import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.event_log_collection import EventLogCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    dag_id: str | Unset = UNSET,
    task_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    event: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    included_events: str | Unset = UNSET,
    excluded_events: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params["dag_id"] = dag_id

    params["task_id"] = task_id

    params["run_id"] = run_id

    params["event"] = event

    params["owner"] = owner

    json_before: str | Unset = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    json_after: str | Unset = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params["included_events"] = included_events

    params["excluded_events"] = excluded_events

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/eventLogs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | EventLogCollection | None:
    if response.status_code == 200:
        response_200 = EventLogCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | EventLogCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    dag_id: str | Unset = UNSET,
    task_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    event: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    included_events: str | Unset = UNSET,
    excluded_events: str | Unset = UNSET,
) -> Response[Error | EventLogCollection]:
    """List log entries

     List log entries from event log.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        dag_id (str | Unset):
        task_id (str | Unset):
        run_id (str | Unset):
        event (str | Unset):
        owner (str | Unset):
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):
        included_events (str | Unset):
        excluded_events (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | EventLogCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    dag_id: str | Unset = UNSET,
    task_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    event: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    included_events: str | Unset = UNSET,
    excluded_events: str | Unset = UNSET,
) -> Error | EventLogCollection | None:
    """List log entries

     List log entries from event log.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        dag_id (str | Unset):
        task_id (str | Unset):
        run_id (str | Unset):
        event (str | Unset):
        owner (str | Unset):
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):
        included_events (str | Unset):
        excluded_events (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | EventLogCollection
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    dag_id: str | Unset = UNSET,
    task_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    event: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    included_events: str | Unset = UNSET,
    excluded_events: str | Unset = UNSET,
) -> Response[Error | EventLogCollection]:
    """List log entries

     List log entries from event log.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        dag_id (str | Unset):
        task_id (str | Unset):
        run_id (str | Unset):
        event (str | Unset):
        owner (str | Unset):
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):
        included_events (str | Unset):
        excluded_events (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | EventLogCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    dag_id: str | Unset = UNSET,
    task_id: str | Unset = UNSET,
    run_id: str | Unset = UNSET,
    event: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    before: datetime.datetime | Unset = UNSET,
    after: datetime.datetime | Unset = UNSET,
    included_events: str | Unset = UNSET,
    excluded_events: str | Unset = UNSET,
) -> Error | EventLogCollection | None:
    """List log entries

     List log entries from event log.

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        dag_id (str | Unset):
        task_id (str | Unset):
        run_id (str | Unset):
        event (str | Unset):
        owner (str | Unset):
        before (datetime.datetime | Unset):
        after (datetime.datetime | Unset):
        included_events (str | Unset):
        excluded_events (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | EventLogCollection
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
            event=event,
            owner=owner,
            before=before,
            after=after,
            included_events=included_events,
            excluded_events=excluded_events,
        )
    ).parsed
