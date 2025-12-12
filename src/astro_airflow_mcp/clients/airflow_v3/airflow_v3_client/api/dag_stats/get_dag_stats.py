from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_stats_collection_response import DagStatsCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dag_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dag_ids: list[str] | Unset = UNSET
    if not isinstance(dag_ids, Unset):
        json_dag_ids = dag_ids

    params["dag_ids"] = json_dag_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dagStats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DagStatsCollectionResponse.from_dict(response.json())

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
) -> Response[DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    dag_ids: list[str] | Unset = UNSET,
) -> Response[DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Stats

     Get Dag statistics.

    Args:
        dag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_ids=dag_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    dag_ids: list[str] | Unset = UNSET,
) -> DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Stats

     Get Dag statistics.

    Args:
        dag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        dag_ids=dag_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dag_ids: list[str] | Unset = UNSET,
) -> Response[DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Stats

     Get Dag statistics.

    Args:
        dag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_ids=dag_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    dag_ids: list[str] | Unset = UNSET,
) -> DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Stats

     Get Dag statistics.

    Args:
        dag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DagStatsCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            dag_ids=dag_ids,
        )
    ).parsed
