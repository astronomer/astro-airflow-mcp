from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_log_accept import GetLogAccept
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.task_instances_log_response import TaskInstancesLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    full_content: bool | Unset = False,
    map_index: int | Unset = -1,
    token: None | str | Unset = UNSET,
    accept: GetLogAccept | Unset = GetLogAccept.VALUE_2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = str(accept)

    params: dict[str, Any] = {}

    params["full_content"] = full_content

    params["map_index"] = map_index

    json_token: None | str | Unset
    if isinstance(token, Unset):
        json_token = UNSET
    else:
        json_token = token
    params["token"] = json_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{try_number}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            try_number=quote(str(try_number), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse | None:
    if response.status_code == 200:
        response_200 = TaskInstancesLogResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse]:
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
    try_number: int,
    *,
    client: AuthenticatedClient,
    full_content: bool | Unset = False,
    map_index: int | Unset = -1,
    token: None | str | Unset = UNSET,
    accept: GetLogAccept | Unset = GetLogAccept.VALUE_2,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse]:
    """Get Log

     Get logs for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        full_content (bool | Unset):  Default: False.
        map_index (int | Unset):  Default: -1.
        token (None | str | Unset):
        accept (GetLogAccept | Unset):  Default: GetLogAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        full_content=full_content,
        map_index=map_index,
        token=token,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    client: AuthenticatedClient,
    full_content: bool | Unset = False,
    map_index: int | Unset = -1,
    token: None | str | Unset = UNSET,
    accept: GetLogAccept | Unset = GetLogAccept.VALUE_2,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse | None:
    """Get Log

     Get logs for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        full_content (bool | Unset):  Default: False.
        map_index (int | Unset):  Default: -1.
        token (None | str | Unset):
        accept (GetLogAccept | Unset):  Default: GetLogAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        client=client,
        full_content=full_content,
        map_index=map_index,
        token=token,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    client: AuthenticatedClient,
    full_content: bool | Unset = False,
    map_index: int | Unset = -1,
    token: None | str | Unset = UNSET,
    accept: GetLogAccept | Unset = GetLogAccept.VALUE_2,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse]:
    """Get Log

     Get logs for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        full_content (bool | Unset):  Default: False.
        map_index (int | Unset):  Default: -1.
        token (None | str | Unset):
        accept (GetLogAccept | Unset):  Default: GetLogAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        full_content=full_content,
        map_index=map_index,
        token=token,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    client: AuthenticatedClient,
    full_content: bool | Unset = False,
    map_index: int | Unset = -1,
    token: None | str | Unset = UNSET,
    accept: GetLogAccept | Unset = GetLogAccept.VALUE_2,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse | None:
    """Get Log

     Get logs for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        full_content (bool | Unset):  Default: False.
        map_index (int | Unset):  Default: -1.
        token (None | str | Unset):
        accept (GetLogAccept | Unset):  Default: GetLogAccept.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstancesLogResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            try_number=try_number,
            client=client,
            full_content=full_content,
            map_index=map_index,
            token=token,
            accept=accept,
        )
    ).parsed
