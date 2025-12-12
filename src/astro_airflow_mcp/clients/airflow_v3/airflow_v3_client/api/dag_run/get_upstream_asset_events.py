from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_event_collection_response import AssetEventCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamAssetEvents".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssetEventCollectionResponse.from_dict(response.json())

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
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Upstream Asset Events

     If dag run is asset-triggered, return the asset events that triggered it.

    Args:
        dag_id (str):
        dag_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Upstream Asset Events

     If dag run is asset-triggered, return the asset events that triggered it.

    Args:
        dag_id (str):
        dag_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Upstream Asset Events

     If dag run is asset-triggered, return the asset events that triggered it.

    Args:
        dag_id (str):
        dag_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
) -> AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Upstream Asset Events

     If dag run is asset-triggered, return the asset events that triggered it.

    Args:
        dag_id (str):
        dag_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetEventCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
        )
    ).parsed
