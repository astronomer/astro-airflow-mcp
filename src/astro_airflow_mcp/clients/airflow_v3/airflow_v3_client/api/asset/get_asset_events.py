import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_event_collection_response import AssetEventCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    asset_id: int | None | Unset = UNSET,
    source_dag_id: None | str | Unset = UNSET,
    source_task_id: None | str | Unset = UNSET,
    source_run_id: None | str | Unset = UNSET,
    source_map_index: int | None | Unset = UNSET,
    timestamp_gte: datetime.datetime | None | Unset = UNSET,
    timestamp_gt: datetime.datetime | None | Unset = UNSET,
    timestamp_lte: datetime.datetime | None | Unset = UNSET,
    timestamp_lt: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_asset_id: int | None | Unset
    if isinstance(asset_id, Unset):
        json_asset_id = UNSET
    else:
        json_asset_id = asset_id
    params["asset_id"] = json_asset_id

    json_source_dag_id: None | str | Unset
    if isinstance(source_dag_id, Unset):
        json_source_dag_id = UNSET
    else:
        json_source_dag_id = source_dag_id
    params["source_dag_id"] = json_source_dag_id

    json_source_task_id: None | str | Unset
    if isinstance(source_task_id, Unset):
        json_source_task_id = UNSET
    else:
        json_source_task_id = source_task_id
    params["source_task_id"] = json_source_task_id

    json_source_run_id: None | str | Unset
    if isinstance(source_run_id, Unset):
        json_source_run_id = UNSET
    else:
        json_source_run_id = source_run_id
    params["source_run_id"] = json_source_run_id

    json_source_map_index: int | None | Unset
    if isinstance(source_map_index, Unset):
        json_source_map_index = UNSET
    else:
        json_source_map_index = source_map_index
    params["source_map_index"] = json_source_map_index

    json_timestamp_gte: None | str | Unset
    if isinstance(timestamp_gte, Unset):
        json_timestamp_gte = UNSET
    elif isinstance(timestamp_gte, datetime.datetime):
        json_timestamp_gte = timestamp_gte.isoformat()
    else:
        json_timestamp_gte = timestamp_gte
    params["timestamp_gte"] = json_timestamp_gte

    json_timestamp_gt: None | str | Unset
    if isinstance(timestamp_gt, Unset):
        json_timestamp_gt = UNSET
    elif isinstance(timestamp_gt, datetime.datetime):
        json_timestamp_gt = timestamp_gt.isoformat()
    else:
        json_timestamp_gt = timestamp_gt
    params["timestamp_gt"] = json_timestamp_gt

    json_timestamp_lte: None | str | Unset
    if isinstance(timestamp_lte, Unset):
        json_timestamp_lte = UNSET
    elif isinstance(timestamp_lte, datetime.datetime):
        json_timestamp_lte = timestamp_lte.isoformat()
    else:
        json_timestamp_lte = timestamp_lte
    params["timestamp_lte"] = json_timestamp_lte

    json_timestamp_lt: None | str | Unset
    if isinstance(timestamp_lt, Unset):
        json_timestamp_lt = UNSET
    elif isinstance(timestamp_lt, datetime.datetime):
        json_timestamp_lt = timestamp_lt.isoformat()
    else:
        json_timestamp_lt = timestamp_lt
    params["timestamp_lt"] = json_timestamp_lt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/assets/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssetEventCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPExceptionResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = HTTPExceptionResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
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
    asset_id: int | None | Unset = UNSET,
    source_dag_id: None | str | Unset = UNSET,
    source_task_id: None | str | Unset = UNSET,
    source_run_id: None | str | Unset = UNSET,
    source_map_index: int | None | Unset = UNSET,
    timestamp_gte: datetime.datetime | None | Unset = UNSET,
    timestamp_gt: datetime.datetime | None | Unset = UNSET,
    timestamp_lte: datetime.datetime | None | Unset = UNSET,
    timestamp_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Asset Events

     Get asset events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `source_task_id,
            source_dag_id, source_run_id, source_map_index, timestamp`
        asset_id (int | None | Unset):
        source_dag_id (None | str | Unset):
        source_task_id (None | str | Unset):
        source_run_id (None | str | Unset):
        source_map_index (int | None | Unset):
        timestamp_gte (datetime.datetime | None | Unset):
        timestamp_gt (datetime.datetime | None | Unset):
        timestamp_lte (datetime.datetime | None | Unset):
        timestamp_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        asset_id=asset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
        timestamp_gte=timestamp_gte,
        timestamp_gt=timestamp_gt,
        timestamp_lte=timestamp_lte,
        timestamp_lt=timestamp_lt,
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
    asset_id: int | None | Unset = UNSET,
    source_dag_id: None | str | Unset = UNSET,
    source_task_id: None | str | Unset = UNSET,
    source_run_id: None | str | Unset = UNSET,
    source_map_index: int | None | Unset = UNSET,
    timestamp_gte: datetime.datetime | None | Unset = UNSET,
    timestamp_gt: datetime.datetime | None | Unset = UNSET,
    timestamp_lte: datetime.datetime | None | Unset = UNSET,
    timestamp_lt: datetime.datetime | None | Unset = UNSET,
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Asset Events

     Get asset events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `source_task_id,
            source_dag_id, source_run_id, source_map_index, timestamp`
        asset_id (int | None | Unset):
        source_dag_id (None | str | Unset):
        source_task_id (None | str | Unset):
        source_run_id (None | str | Unset):
        source_map_index (int | None | Unset):
        timestamp_gte (datetime.datetime | None | Unset):
        timestamp_gt (datetime.datetime | None | Unset):
        timestamp_lte (datetime.datetime | None | Unset):
        timestamp_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        asset_id=asset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
        timestamp_gte=timestamp_gte,
        timestamp_gt=timestamp_gt,
        timestamp_lte=timestamp_lte,
        timestamp_lt=timestamp_lt,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    asset_id: int | None | Unset = UNSET,
    source_dag_id: None | str | Unset = UNSET,
    source_task_id: None | str | Unset = UNSET,
    source_run_id: None | str | Unset = UNSET,
    source_map_index: int | None | Unset = UNSET,
    timestamp_gte: datetime.datetime | None | Unset = UNSET,
    timestamp_gt: datetime.datetime | None | Unset = UNSET,
    timestamp_lte: datetime.datetime | None | Unset = UNSET,
    timestamp_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Asset Events

     Get asset events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `source_task_id,
            source_dag_id, source_run_id, source_map_index, timestamp`
        asset_id (int | None | Unset):
        source_dag_id (None | str | Unset):
        source_task_id (None | str | Unset):
        source_run_id (None | str | Unset):
        source_map_index (int | None | Unset):
        timestamp_gte (datetime.datetime | None | Unset):
        timestamp_gt (datetime.datetime | None | Unset):
        timestamp_lte (datetime.datetime | None | Unset):
        timestamp_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        asset_id=asset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
        timestamp_gte=timestamp_gte,
        timestamp_gt=timestamp_gt,
        timestamp_lte=timestamp_lte,
        timestamp_lt=timestamp_lt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    asset_id: int | None | Unset = UNSET,
    source_dag_id: None | str | Unset = UNSET,
    source_task_id: None | str | Unset = UNSET,
    source_run_id: None | str | Unset = UNSET,
    source_map_index: int | None | Unset = UNSET,
    timestamp_gte: datetime.datetime | None | Unset = UNSET,
    timestamp_gt: datetime.datetime | None | Unset = UNSET,
    timestamp_lte: datetime.datetime | None | Unset = UNSET,
    timestamp_lt: datetime.datetime | None | Unset = UNSET,
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Asset Events

     Get asset events.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `source_task_id,
            source_dag_id, source_run_id, source_map_index, timestamp`
        asset_id (int | None | Unset):
        source_dag_id (None | str | Unset):
        source_task_id (None | str | Unset):
        source_run_id (None | str | Unset):
        source_map_index (int | None | Unset):
        timestamp_gte (datetime.datetime | None | Unset):
        timestamp_gt (datetime.datetime | None | Unset):
        timestamp_lte (datetime.datetime | None | Unset):
        timestamp_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            asset_id=asset_id,
            source_dag_id=source_dag_id,
            source_task_id=source_task_id,
            source_run_id=source_run_id,
            source_map_index=source_map_index,
            timestamp_gte=timestamp_gte,
            timestamp_gt=timestamp_gt,
            timestamp_lte=timestamp_lte,
            timestamp_lt=timestamp_lt,
        )
    ).parsed
