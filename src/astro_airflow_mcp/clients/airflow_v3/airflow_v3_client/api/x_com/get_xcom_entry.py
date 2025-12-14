from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.x_com_response_native import XComResponseNative
from ...models.x_com_response_string import XComResponseString
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    map_index: int | Unset = -1,
    deserialize: bool | Unset = False,
    stringify: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["map_index"] = map_index

    params["deserialize"] = deserialize

    params["stringify"] = stringify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            xcom_key=quote(str(xcom_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> XComResponseNative | XComResponseString:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = XComResponseNative.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = XComResponseString.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString]:
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
    xcom_key: str,
    *,
    client: AuthenticatedClient,
    map_index: int | Unset = -1,
    deserialize: bool | Unset = False,
    stringify: bool | Unset = False,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString]:
    """Get Xcom Entry

     Get an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (int | Unset):  Default: -1.
        deserialize (bool | Unset):  Default: False.
        stringify (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: AuthenticatedClient,
    map_index: int | Unset = -1,
    deserialize: bool | Unset = False,
    stringify: bool | Unset = False,
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString | None:
    """Get Xcom Entry

     Get an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (int | Unset):  Default: -1.
        deserialize (bool | Unset):  Default: False.
        stringify (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        client=client,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: AuthenticatedClient,
    map_index: int | Unset = -1,
    deserialize: bool | Unset = False,
    stringify: bool | Unset = False,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString]:
    """Get Xcom Entry

     Get an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (int | Unset):  Default: -1.
        deserialize (bool | Unset):  Default: False.
        stringify (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: AuthenticatedClient,
    map_index: int | Unset = -1,
    deserialize: bool | Unset = False,
    stringify: bool | Unset = False,
) -> HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString | None:
    """Get Xcom Entry

     Get an XCom entry.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (int | Unset):  Default: -1.
        deserialize (bool | Unset):  Default: False.
        stringify (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComResponseNative | XComResponseString
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            xcom_key=xcom_key,
            client=client,
            map_index=map_index,
            deserialize=deserialize,
            stringify=stringify,
        )
    ).parsed
