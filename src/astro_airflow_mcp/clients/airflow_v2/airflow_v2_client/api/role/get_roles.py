from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.role_collection import RoleCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/roles",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RoleCollection | None:
    if response.status_code == 200:
        response_200 = RoleCollection.from_dict(response.json())

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
) -> Response[Error | RoleCollection]:
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
) -> Response[Error | RoleCollection]:
    """List roles

     Get a list of roles.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoleCollection]
    """

    kwargs = _get_kwargs(
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
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> Error | RoleCollection | None:
    """List roles

     Get a list of roles.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoleCollection
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> Response[Error | RoleCollection]:
    """List roles

     Get a list of roles.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RoleCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    order_by: str | Unset = UNSET,
) -> Error | RoleCollection | None:
    """List roles

     Get a list of roles.

    *This API endpoint is deprecated, please use the endpoint `/auth/fab/v1` for this operation
    instead.*

    Args:
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RoleCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
