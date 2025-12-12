from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    *,
    interval: float,
    result: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["interval"] = interval

    json_result: list[str] | None | Unset
    if isinstance(result, Unset):
        json_result = UNSET
    elif isinstance(result, list):
        json_result = result

    else:
        json_result = result
    params["result"] = json_result

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/wait".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
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
    interval: float,
    result: list[str] | None | Unset = UNSET,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Experimental: Wait for a dag run to complete, and return task results if requested.

     🚧 This is an experimental endpoint and may change or be removed without notice.Successful response
    are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the DAG run
    state.

    Args:
        dag_id (str):
        dag_run_id (str):
        interval (float): Seconds to wait between dag run state checks
        result (list[str] | None | Unset): Collect result XCom from task. Can be set multiple
            times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        interval=interval,
        result=result,
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
    interval: float,
    result: list[str] | None | Unset = UNSET,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Experimental: Wait for a dag run to complete, and return task results if requested.

     🚧 This is an experimental endpoint and may change or be removed without notice.Successful response
    are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the DAG run
    state.

    Args:
        dag_id (str):
        dag_run_id (str):
        interval (float): Seconds to wait between dag run state checks
        result (list[str] | None | Unset): Collect result XCom from task. Can be set multiple
            times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        client=client,
        interval=interval,
        result=result,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
    interval: float,
    result: list[str] | None | Unset = UNSET,
) -> Response[Any | HTTPExceptionResponse | HTTPValidationError]:
    """Experimental: Wait for a dag run to complete, and return task results if requested.

     🚧 This is an experimental endpoint and may change or be removed without notice.Successful response
    are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the DAG run
    state.

    Args:
        dag_id (str):
        dag_run_id (str):
        interval (float): Seconds to wait between dag run state checks
        result (list[str] | None | Unset): Collect result XCom from task. Can be set multiple
            times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        interval=interval,
        result=result,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
    interval: float,
    result: list[str] | None | Unset = UNSET,
) -> Any | HTTPExceptionResponse | HTTPValidationError | None:
    """Experimental: Wait for a dag run to complete, and return task results if requested.

     🚧 This is an experimental endpoint and may change or be removed without notice.Successful response
    are streamed as newline-delimited JSON (NDJSON). Each line is a JSON object representing the DAG run
    state.

    Args:
        dag_id (str):
        dag_run_id (str):
        interval (float): Seconds to wait between dag run state checks
        result (list[str] | None | Unset): Collect result XCom from task. Can be set multiple
            times.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
            interval=interval,
            result=result,
        )
    ).parsed
