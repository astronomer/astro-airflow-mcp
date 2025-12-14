from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config import Config
from ...models.get_config_value_accept import GetConfigValueAccept
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response, Unset


def _get_kwargs(
    section: str,
    option: str,
    *,
    accept: GetConfigValueAccept | Unset = GetConfigValueAccept.VALUE_2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = str(accept)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/config/section/{section}/option/{option}".format(
            section=quote(str(section), safe=""),
            option=quote(str(option), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Config | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Config.from_dict(response.json())

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

    if response.status_code == 406:
        response_406 = HTTPExceptionResponse.from_dict(response.json())

        return response_406

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Config | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient,
    accept: GetConfigValueAccept | Unset = GetConfigValueAccept.VALUE_2,
) -> Response[Config | HTTPExceptionResponse | HTTPValidationError]:
    """Get Config Value

    Args:
        section (str):
        option (str):
        accept (GetConfigValueAccept | Unset):  Default: GetConfigValueAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Config | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient,
    accept: GetConfigValueAccept | Unset = GetConfigValueAccept.VALUE_2,
) -> Config | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Config Value

    Args:
        section (str):
        option (str):
        accept (GetConfigValueAccept | Unset):  Default: GetConfigValueAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Config | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        section=section,
        option=option,
        client=client,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient,
    accept: GetConfigValueAccept | Unset = GetConfigValueAccept.VALUE_2,
) -> Response[Config | HTTPExceptionResponse | HTTPValidationError]:
    """Get Config Value

    Args:
        section (str):
        option (str):
        accept (GetConfigValueAccept | Unset):  Default: GetConfigValueAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Config | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient,
    accept: GetConfigValueAccept | Unset = GetConfigValueAccept.VALUE_2,
) -> Config | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Config Value

    Args:
        section (str):
        option (str):
        accept (GetConfigValueAccept | Unset):  Default: GetConfigValueAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Config | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            section=section,
            option=option,
            client=client,
            accept=accept,
        )
    ).parsed
