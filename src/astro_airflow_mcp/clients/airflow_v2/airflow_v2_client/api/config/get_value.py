from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config import Config
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    section: str,
    option: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/config/section/{section}/option/{option}".format(
            section=quote(str(section), safe=""),
            option=quote(str(option), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Config | Error | None:
    if response.status_code == 200:
        response_200 = Config.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Config | Error]:
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
    client: AuthenticatedClient | Client,
) -> Response[Config | Error]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Config | Error]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient | Client,
) -> Config | Error | None:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Config | Error
    """

    return sync_detailed(
        section=section,
        option=option,
        client=client,
    ).parsed


async def asyncio_detailed(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Config | Error]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Config | Error]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section: str,
    option: str,
    *,
    client: AuthenticatedClient | Client,
) -> Config | Error | None:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Config | Error
    """

    return (
        await asyncio_detailed(
            section=section,
            option=option,
            client=client,
        )
    ).parsed
