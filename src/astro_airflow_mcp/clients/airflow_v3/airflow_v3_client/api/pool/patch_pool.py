from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.pool_patch_body import PoolPatchBody
from ...models.pool_response import PoolResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pool_name: str,
    *,
    body: PoolPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_mask: list[str] | None | Unset
    if isinstance(update_mask, Unset):
        json_update_mask = UNSET
    elif isinstance(update_mask, list):
        json_update_mask = update_mask

    else:
        json_update_mask = update_mask
    params["update_mask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/pools/{pool_name}".format(
            pool_name=quote(str(pool_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | PoolResponse | None:
    if response.status_code == 200:
        response_200 = PoolResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HTTPExceptionResponse.from_dict(response.json())

        return response_400

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | PoolResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_name: str,
    *,
    client: AuthenticatedClient,
    body: PoolPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | PoolResponse]:
    """Patch Pool

     Update a Pool.

    Args:
        pool_name (str):
        update_mask (list[str] | None | Unset):
        body (PoolPatchBody): Pool serializer for patch bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | PoolResponse]
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
    client: AuthenticatedClient,
    body: PoolPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | PoolResponse | None:
    """Patch Pool

     Update a Pool.

    Args:
        pool_name (str):
        update_mask (list[str] | None | Unset):
        body (PoolPatchBody): Pool serializer for patch bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | PoolResponse
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
    client: AuthenticatedClient,
    body: PoolPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | PoolResponse]:
    """Patch Pool

     Update a Pool.

    Args:
        pool_name (str):
        update_mask (list[str] | None | Unset):
        body (PoolPatchBody): Pool serializer for patch bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | PoolResponse]
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
    client: AuthenticatedClient,
    body: PoolPatchBody,
    update_mask: list[str] | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | PoolResponse | None:
    """Patch Pool

     Update a Pool.

    Args:
        pool_name (str):
        update_mask (list[str] | None | Unset):
        body (PoolPatchBody): Pool serializer for patch bodies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | PoolResponse
    """

    return (
        await asyncio_detailed(
            pool_name=pool_name,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
