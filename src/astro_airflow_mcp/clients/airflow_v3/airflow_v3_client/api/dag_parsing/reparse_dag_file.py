from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    file_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v2/parseDagFile/{file_token}".format(
            file_token=quote(str(file_token), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = response.json()
        return response_201

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
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Reparse Dag File

     Request re-parsing a DAG file.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        file_token=file_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_token: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Reparse Dag File

     Request re-parsing a DAG file.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        file_token=file_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_token: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Reparse Dag File

     Request re-parsing a DAG file.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        file_token=file_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_token: str,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Reparse Dag File

     Request re-parsing a DAG file.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            file_token=file_token,
            client=client,
        )
    ).parsed
