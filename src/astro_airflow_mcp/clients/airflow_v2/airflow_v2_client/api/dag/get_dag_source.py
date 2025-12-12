from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_dag_source_response_200 import GetDagSourceResponse200
from ...types import Response


def _get_kwargs(
    file_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dagSources/{file_token}".format(
            file_token=quote(str(file_token), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetDagSourceResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDagSourceResponse200.from_dict(response.json())

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

    if response.status_code == 406:
        response_406 = Error.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetDagSourceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetDagSourceResponse200]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetDagSourceResponse200]
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
    client: AuthenticatedClient | Client,
) -> Error | GetDagSourceResponse200 | None:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetDagSourceResponse200
    """

    return sync_detailed(
        file_token=file_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | GetDagSourceResponse200]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetDagSourceResponse200]
    """

    kwargs = _get_kwargs(
        file_token=file_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_token: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | GetDagSourceResponse200 | None:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetDagSourceResponse200
    """

    return (
        await asyncio_detailed(
            file_token=file_token,
            client=client,
        )
    ).parsed
