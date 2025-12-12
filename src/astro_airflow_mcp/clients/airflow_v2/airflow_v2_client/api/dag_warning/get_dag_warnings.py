from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_warning_collection import DagWarningCollection
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dag_id: str | Unset = UNSET,
    warning_type: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dag_id"] = dag_id

    params["warning_type"] = warning_type

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dagWarnings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DagWarningCollection | Error | None:
    if response.status_code == 200:
        response_200 = DagWarningCollection.from_dict(response.json())

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
) -> Response[DagWarningCollection | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    dag_id: str | Unset = UNSET,
    warning_type: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> Response[DagWarningCollection | Error]:
    """List dag warnings

    Args:
        dag_id (str | Unset):
        warning_type (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DagWarningCollection | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    dag_id: str | Unset = UNSET,
    warning_type: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> DagWarningCollection | Error | None:
    """List dag warnings

    Args:
        dag_id (str | Unset):
        warning_type (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DagWarningCollection | Error
    """

    return sync_detailed(
        client=client,
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dag_id: str | Unset = UNSET,
    warning_type: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> Response[DagWarningCollection | Error]:
    """List dag warnings

    Args:
        dag_id (str | Unset):
        warning_type (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DagWarningCollection | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    dag_id: str | Unset = UNSET,
    warning_type: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> DagWarningCollection | Error | None:
    """List dag warnings

    Args:
        dag_id (str | Unset):
        warning_type (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DagWarningCollection | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            dag_id=dag_id,
            warning_type=warning_type,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
