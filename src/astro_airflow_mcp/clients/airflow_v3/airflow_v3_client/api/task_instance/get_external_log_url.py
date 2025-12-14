from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_log_url_response import ExternalLogUrlResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    map_index: int | Unset = -1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["map_index"] = map_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/externalLogUrl/{try_number}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            try_number=quote(str(try_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExternalLogUrlResponse.from_dict(response.json())

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
) -> Response[ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError]:
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
    map_index: int | Unset = -1,
) -> Response[ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get External Log Url

     Get external log URL for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        map_index (int | Unset):  Default: -1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        map_index=map_index,
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
    map_index: int | Unset = -1,
) -> ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get External Log Url

     Get external log URL for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        map_index (int | Unset):  Default: -1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        client=client,
        map_index=map_index,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    try_number: int,
    *,
    client: AuthenticatedClient,
    map_index: int | Unset = -1,
) -> Response[ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get External Log Url

     Get external log URL for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        map_index (int | Unset):  Default: -1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        try_number=try_number,
        map_index=map_index,
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
    map_index: int | Unset = -1,
) -> ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get External Log Url

     Get external log URL for a specific task instance.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        try_number (int):
        map_index (int | Unset):  Default: -1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalLogUrlResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            try_number=try_number,
            client=client,
            map_index=map_index,
        )
    ).parsed
