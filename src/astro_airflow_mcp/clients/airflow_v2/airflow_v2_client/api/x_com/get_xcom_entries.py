from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.x_com_collection import XComCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    map_index: int | Unset = UNSET,
    xcom_key: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["map_index"] = map_index

    params["xcom_key"] = xcom_key

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | XComCollection | None:
    if response.status_code == 200:
        response_200 = XComCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | XComCollection]:
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
    client: AuthenticatedClient | Client,
    map_index: int | Unset = UNSET,
    xcom_key: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
) -> Response[Error | XComCollection]:
    """List XCom entries

     This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for
    for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use
    this endpoint to get a list of XCom entries and then fetch individual entry to get value.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | Unset):
        xcom_key (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | XComCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        xcom_key=xcom_key,
        limit=limit,
        offset=offset,
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
    client: AuthenticatedClient | Client,
    map_index: int | Unset = UNSET,
    xcom_key: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
) -> Error | XComCollection | None:
    """List XCom entries

     This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for
    for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use
    this endpoint to get a list of XCom entries and then fetch individual entry to get value.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | Unset):
        xcom_key (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | XComCollection
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        map_index=map_index,
        xcom_key=xcom_key,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    map_index: int | Unset = UNSET,
    xcom_key: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
) -> Response[Error | XComCollection]:
    """List XCom entries

     This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for
    for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use
    this endpoint to get a list of XCom entries and then fetch individual entry to get value.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | Unset):
        xcom_key (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | XComCollection]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        map_index=map_index,
        xcom_key=xcom_key,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    map_index: int | Unset = UNSET,
    xcom_key: str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
) -> Error | XComCollection | None:
    """List XCom entries

     This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for
    for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use
    this endpoint to get a list of XCom entries and then fetch individual entry to get value.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        map_index (int | Unset):
        xcom_key (str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | XComCollection
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
            map_index=map_index,
            xcom_key=xcom_key,
            limit=limit,
            offset=offset,
        )
    ).parsed
