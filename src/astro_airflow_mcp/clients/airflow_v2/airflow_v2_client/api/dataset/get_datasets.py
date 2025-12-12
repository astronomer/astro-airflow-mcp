from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_collection import DatasetCollection
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    uri_pattern: str | Unset = UNSET,
    dag_ids: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params["uri_pattern"] = uri_pattern

    params["dag_ids"] = dag_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetCollection | Error | None:
    if response.status_code == 200:
        response_200 = DatasetCollection.from_dict(response.json())

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
) -> Response[DatasetCollection | Error]:
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
    uri_pattern: str | Unset = UNSET,
    dag_ids: str | Unset = UNSET,
) -> Response[DatasetCollection | Error]:
    """List datasets

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        uri_pattern (str | Unset):
        dag_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCollection | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        uri_pattern=uri_pattern,
        dag_ids=dag_ids,
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
    uri_pattern: str | Unset = UNSET,
    dag_ids: str | Unset = UNSET,
) -> DatasetCollection | Error | None:
    """List datasets

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        uri_pattern (str | Unset):
        dag_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCollection | Error
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        uri_pattern=uri_pattern,
        dag_ids=dag_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    uri_pattern: str | Unset = UNSET,
    dag_ids: str | Unset = UNSET,
) -> Response[DatasetCollection | Error]:
    """List datasets

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        uri_pattern (str | Unset):
        dag_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCollection | Error]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        uri_pattern=uri_pattern,
        dag_ids=dag_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
    uri_pattern: str | Unset = UNSET,
    dag_ids: str | Unset = UNSET,
) -> DatasetCollection | Error | None:
    """List datasets

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):
        uri_pattern (str | Unset):
        dag_ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCollection | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            uri_pattern=uri_pattern,
            dag_ids=dag_ids,
        )
    ).parsed
