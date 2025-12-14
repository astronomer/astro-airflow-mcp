from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset import Dataset
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    uri: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{uri}".format(
            uri=quote(str(uri), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dataset | Error | None:
    if response.status_code == 200:
        response_200 = Dataset.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dataset | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Dataset | Error]:
    """Get a dataset

     Get a dataset by uri.

    Args:
        uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset | Error]
    """

    kwargs = _get_kwargs(
        uri=uri,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
) -> Dataset | Error | None:
    """Get a dataset

     Get a dataset by uri.

    Args:
        uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset | Error
    """

    return sync_detailed(
        uri=uri,
        client=client,
    ).parsed


async def asyncio_detailed(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Dataset | Error]:
    """Get a dataset

     Get a dataset by uri.

    Args:
        uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dataset | Error]
    """

    kwargs = _get_kwargs(
        uri=uri,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uri: str,
    *,
    client: AuthenticatedClient | Client,
) -> Dataset | Error | None:
    """Get a dataset

     Get a dataset by uri.

    Args:
        uri (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dataset | Error
    """

    return (
        await asyncio_detailed(
            uri=uri,
            client=client,
        )
    ).parsed
