from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pool import Pool
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pool_name: str,
    *,
    body: Pool,
    update_mask: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_mask: list[str] | Unset = UNSET
    if not isinstance(update_mask, Unset):
        json_update_mask = update_mask

    params["update_mask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/pools/{pool_name}".format(
            pool_name=quote(str(pool_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Pool | None:
    if response.status_code == 200:
        response_200 = Pool.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Pool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Pool,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | Pool]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (list[str] | Unset):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pool]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Pool,
    update_mask: list[str] | Unset = UNSET,
) -> Error | Pool | None:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (list[str] | Unset):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pool
    """

    return sync_detailed(
        pool_name=pool_name,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Pool,
    update_mask: list[str] | Unset = UNSET,
) -> Response[Error | Pool]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (list[str] | Unset):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pool]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: Pool,
    update_mask: list[str] | Unset = UNSET,
) -> Error | Pool | None:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (list[str] | Unset):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pool
    """

    return (
        await asyncio_detailed(
            pool_name=pool_name,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
