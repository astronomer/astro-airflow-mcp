from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.x_com_create_body import XComCreateBody
from ...models.x_com_response_native import XComResponseNative
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    body: XComCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | None:
    if response.status_code == 201:
        response_201 = XComResponseNative.from_dict(response.json())

        return response_201

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative]:
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
    *,
    client: AuthenticatedClient,
    body: XComCreateBody,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative]:
    """Create Xcom Entry

     Create an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (XComCreateBody): Payload serializer for creating an XCom entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: XComCreateBody,
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | None:
    """Create Xcom Entry

     Create an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (XComCreateBody): Payload serializer for creating an XCom entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComResponseNative
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: XComCreateBody,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative]:
    """Create Xcom Entry

     Create an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (XComCreateBody): Payload serializer for creating an XCom entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    body: XComCreateBody,
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | None:
    """Create Xcom Entry

     Create an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (XComCreateBody): Payload serializer for creating an XCom entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComResponseNative
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
