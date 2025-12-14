from http import HTTPStatus
from typing import Any, Literal
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.task_instance_collection_response import TaskInstanceCollectionResponse
from ...models.task_instances_batch_body import TaskInstancesBatchBody
from ...types import Response


def _get_kwargs(
    dag_id: Literal["~"],
    dag_run_id: Literal["~"],
    *,
    body: TaskInstancesBatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/list".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    if response.status_code == 200:
        response_200 = TaskInstanceCollectionResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: Literal["~"],
    dag_run_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: TaskInstancesBatchBody,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Get Task Instances Batch

     Get list of task instances.

    Args:
        dag_id (Literal['~']):
        dag_run_id (Literal['~']):
        body (TaskInstancesBatchBody): Task Instance body for get batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: Literal["~"],
    dag_run_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: TaskInstancesBatchBody,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Get Task Instances Batch

     Get list of task instances.

    Args:
        dag_id (Literal['~']):
        dag_run_id (Literal['~']):
        body (TaskInstancesBatchBody): Task Instance body for get batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: Literal["~"],
    dag_run_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: TaskInstancesBatchBody,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Get Task Instances Batch

     Get list of task instances.

    Args:
        dag_id (Literal['~']):
        dag_run_id (Literal['~']):
        body (TaskInstancesBatchBody): Task Instance body for get batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: Literal["~"],
    dag_run_id: Literal["~"],
    *,
    client: AuthenticatedClient,
    body: TaskInstancesBatchBody,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Get Task Instances Batch

     Get list of task instances.

    Args:
        dag_id (Literal['~']):
        dag_run_id (Literal['~']):
        body (TaskInstancesBatchBody): Task Instance body for get batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
            body=body,
        )
    ).parsed
