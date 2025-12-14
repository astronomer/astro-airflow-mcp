from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.variable_response import VariableResponse
from ...types import Response


def _get_kwargs(
    variable_key: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/variables/{variable_key}".format(
            variable_key=quote(str(variable_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | VariableResponse | None:
    if response.status_code == 200:
        response_200 = VariableResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | VariableResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    variable_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | VariableResponse]:
    """Get Variable

     Get a variable entry.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | VariableResponse]
    """

    kwargs = _get_kwargs(
        variable_key=variable_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    variable_key: str,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | VariableResponse | None:
    """Get Variable

     Get a variable entry.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | VariableResponse
    """

    return sync_detailed(
        variable_key=variable_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    variable_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | VariableResponse]:
    """Get Variable

     Get a variable entry.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | VariableResponse]
    """

    kwargs = _get_kwargs(
        variable_key=variable_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    variable_key: str,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | VariableResponse | None:
    """Get Variable

     Get a variable entry.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | VariableResponse
    """

    return (
        await asyncio_detailed(
            variable_key=variable_key,
            client=client,
        )
    ).parsed
