from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.import_error_response import ImportErrorResponse
from ...types import Response


def _get_kwargs(
    import_error_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/importErrors/{import_error_id}".format(
            import_error_id=quote(str(import_error_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse | None:
    if response.status_code == 200:
        response_200 = ImportErrorResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    import_error_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse]:
    """Get Import Error

     Get an import error.

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse]
    """

    kwargs = _get_kwargs(
        import_error_id=import_error_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    import_error_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse | None:
    """Get Import Error

     Get an import error.

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse
    """

    return sync_detailed(
        import_error_id=import_error_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    import_error_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse]:
    """Get Import Error

     Get an import error.

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse]
    """

    kwargs = _get_kwargs(
        import_error_id=import_error_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    import_error_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse | None:
    """Get Import Error

     Get an import error.

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | ImportErrorResponse
    """

    return (
        await asyncio_detailed(
            import_error_id=import_error_id,
            client=client,
        )
    ).parsed
