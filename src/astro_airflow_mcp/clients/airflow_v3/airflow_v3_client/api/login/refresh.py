from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    next_: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_next_: None | str | Unset
    if isinstance(next_, Unset):
        json_next_ = UNSET
    else:
        json_next_ = next_
    params["next"] = json_next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/auth/refresh",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 307:
        response_307 = HTTPExceptionResponse.from_dict(response.json())

        return response_307

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    next_: None | str | Unset = UNSET,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Refresh

     Refresh the authentication token.

    Args:
        next_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        next_=next_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    next_: None | str | Unset = UNSET,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Refresh

     Refresh the authentication token.

    Args:
        next_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    next_: None | str | Unset = UNSET,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Refresh

     Refresh the authentication token.

    Args:
        next_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        next_=next_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    next_: None | str | Unset = UNSET,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Refresh

     Refresh the authentication token.

    Args:
        next_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            next_=next_,
        )
    ).parsed
