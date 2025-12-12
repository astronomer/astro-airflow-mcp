from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_response import DAGRunResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.trigger_dag_run_post_body import TriggerDAGRunPostBody
from ...types import Response


def _get_kwargs(
    dag_id: Any,
    *,
    body: TriggerDAGRunPostBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/dags/{dag_id}/dagRuns".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGRunResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGRunResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = HTTPExceptionResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGRunResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: Any,
    *,
    client: AuthenticatedClient,
    body: TriggerDAGRunPostBody,
) -> Response[DAGRunResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Trigger Dag Run

     Trigger a DAG.

    Args:
        dag_id (Any):
        body (TriggerDAGRunPostBody): Trigger DAG Run Serializer for POST body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunResponse | HTTPExceptionResponse | HTTPValidationError]
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
    dag_id: Any,
    *,
    client: AuthenticatedClient,
    body: TriggerDAGRunPostBody,
) -> DAGRunResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Trigger Dag Run

     Trigger a DAG.

    Args:
        dag_id (Any):
        body (TriggerDAGRunPostBody): Trigger DAG Run Serializer for POST body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: Any,
    *,
    client: AuthenticatedClient,
    body: TriggerDAGRunPostBody,
) -> Response[DAGRunResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Trigger Dag Run

     Trigger a DAG.

    Args:
        dag_id (Any):
        body (TriggerDAGRunPostBody): Trigger DAG Run Serializer for POST body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: Any,
    *,
    client: AuthenticatedClient,
    body: TriggerDAGRunPostBody,
) -> DAGRunResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Trigger Dag Run

     Trigger a DAG.

    Args:
        dag_id (Any):
        body (TriggerDAGRunPostBody): Trigger DAG Run Serializer for POST body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            body=body,
        )
    ).parsed
