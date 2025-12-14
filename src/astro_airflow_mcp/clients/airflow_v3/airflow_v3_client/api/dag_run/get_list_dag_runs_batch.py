from http import HTTPStatus
from typing import Any, Literal
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_collection_response import DAGRunCollectionResponse
from ...models.dag_runs_batch_body import DAGRunsBatchBody
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    dag_id: Literal["~"],
    *,
    body: DAGRunsBatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/dags/{dag_id}/dagRuns/list".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGRunCollectionResponse.from_dict(response.json())

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
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: DAGRunsBatchBody,
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get List Dag Runs Batch

     Get a list of DAG Runs.

    Args:
        dag_id (Literal['~']):
        body (DAGRunsBatchBody): List DAG Runs body for batch endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: DAGRunsBatchBody,
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get List Dag Runs Batch

     Get a list of DAG Runs.

    Args:
        dag_id (Literal['~']):
        body (DAGRunsBatchBody): List DAG Runs body for batch endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: DAGRunsBatchBody,
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get List Dag Runs Batch

     Get a list of DAG Runs.

    Args:
        dag_id (Literal['~']):
        body (DAGRunsBatchBody): List DAG Runs body for batch endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: DAGRunsBatchBody,
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get List Dag Runs Batch

     Get a list of DAG Runs.

    Args:
        dag_id (Literal['~']):
        body (DAGRunsBatchBody): List DAG Runs body for batch endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            body=body,
        )
    ).parsed
