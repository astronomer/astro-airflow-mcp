from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.task_instance_history_response import TaskInstanceHistoryResponse
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    task_try_number: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/tries/{task_try_number}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            map_index=quote(str(map_index), safe=""),
            task_try_number=quote(str(task_try_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse | None:
    if response.status_code == 200:
        response_200 = TaskInstanceHistoryResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    task_try_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse]:
    """Get Mapped Task Instance Try Details

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):
        task_try_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        task_try_number=task_try_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    task_try_number: int,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse | None:
    """Get Mapped Task Instance Try Details

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):
        task_try_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        task_try_number=task_try_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    task_try_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse]:
    """Get Mapped Task Instance Try Details

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):
        task_try_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        task_try_number=task_try_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    map_index: int,
    task_try_number: int,
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse | None:
    """Get Mapped Task Instance Try Details

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int):
        task_try_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceHistoryResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            map_index=map_index,
            task_try_number=task_try_number,
            client=client,
        )
    ).parsed
