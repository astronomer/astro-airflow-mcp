import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.x_com_collection_response import XComCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    xcom_key: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    xcom_key_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index_filter: int | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_xcom_key: None | str | Unset
    if isinstance(xcom_key, Unset):
        json_xcom_key = UNSET
    else:
        json_xcom_key = xcom_key
    params["xcom_key"] = json_xcom_key

    json_map_index: int | None | Unset
    if isinstance(map_index, Unset):
        json_map_index = UNSET
    else:
        json_map_index = map_index
    params["map_index"] = json_map_index

    params["limit"] = limit

    params["offset"] = offset

    json_xcom_key_pattern: None | str | Unset
    if isinstance(xcom_key_pattern, Unset):
        json_xcom_key_pattern = UNSET
    else:
        json_xcom_key_pattern = xcom_key_pattern
    params["xcom_key_pattern"] = json_xcom_key_pattern

    json_dag_display_name_pattern: None | str | Unset
    if isinstance(dag_display_name_pattern, Unset):
        json_dag_display_name_pattern = UNSET
    else:
        json_dag_display_name_pattern = dag_display_name_pattern
    params["dag_display_name_pattern"] = json_dag_display_name_pattern

    json_run_id_pattern: None | str | Unset
    if isinstance(run_id_pattern, Unset):
        json_run_id_pattern = UNSET
    else:
        json_run_id_pattern = run_id_pattern
    params["run_id_pattern"] = json_run_id_pattern

    json_task_id_pattern: None | str | Unset
    if isinstance(task_id_pattern, Unset):
        json_task_id_pattern = UNSET
    else:
        json_task_id_pattern = task_id_pattern
    params["task_id_pattern"] = json_task_id_pattern

    json_map_index_filter: int | None | Unset
    if isinstance(map_index_filter, Unset):
        json_map_index_filter = UNSET
    else:
        json_map_index_filter = map_index_filter
    params["map_index_filter"] = json_map_index_filter

    json_logical_date_gte: None | str | Unset
    if isinstance(logical_date_gte, Unset):
        json_logical_date_gte = UNSET
    elif isinstance(logical_date_gte, datetime.datetime):
        json_logical_date_gte = logical_date_gte.isoformat()
    else:
        json_logical_date_gte = logical_date_gte
    params["logical_date_gte"] = json_logical_date_gte

    json_logical_date_gt: None | str | Unset
    if isinstance(logical_date_gt, Unset):
        json_logical_date_gt = UNSET
    elif isinstance(logical_date_gt, datetime.datetime):
        json_logical_date_gt = logical_date_gt.isoformat()
    else:
        json_logical_date_gt = logical_date_gt
    params["logical_date_gt"] = json_logical_date_gt

    json_logical_date_lte: None | str | Unset
    if isinstance(logical_date_lte, Unset):
        json_logical_date_lte = UNSET
    elif isinstance(logical_date_lte, datetime.datetime):
        json_logical_date_lte = logical_date_lte.isoformat()
    else:
        json_logical_date_lte = logical_date_lte
    params["logical_date_lte"] = json_logical_date_lte

    json_logical_date_lt: None | str | Unset
    if isinstance(logical_date_lt, Unset):
        json_logical_date_lt = UNSET
    elif isinstance(logical_date_lt, datetime.datetime):
        json_logical_date_lt = logical_date_lt.isoformat()
    else:
        json_logical_date_lt = logical_date_lt
    params["logical_date_lt"] = json_logical_date_lt

    json_run_after_gte: None | str | Unset
    if isinstance(run_after_gte, Unset):
        json_run_after_gte = UNSET
    elif isinstance(run_after_gte, datetime.datetime):
        json_run_after_gte = run_after_gte.isoformat()
    else:
        json_run_after_gte = run_after_gte
    params["run_after_gte"] = json_run_after_gte

    json_run_after_gt: None | str | Unset
    if isinstance(run_after_gt, Unset):
        json_run_after_gt = UNSET
    elif isinstance(run_after_gt, datetime.datetime):
        json_run_after_gt = run_after_gt.isoformat()
    else:
        json_run_after_gt = run_after_gt
    params["run_after_gt"] = json_run_after_gt

    json_run_after_lte: None | str | Unset
    if isinstance(run_after_lte, Unset):
        json_run_after_lte = UNSET
    elif isinstance(run_after_lte, datetime.datetime):
        json_run_after_lte = run_after_lte.isoformat()
    else:
        json_run_after_lte = run_after_lte
    params["run_after_lte"] = json_run_after_lte

    json_run_after_lt: None | str | Unset
    if isinstance(run_after_lt, Unset):
        json_run_after_lt = UNSET
    elif isinstance(run_after_lt, datetime.datetime):
        json_run_after_lt = run_after_lt.isoformat()
    else:
        json_run_after_lt = run_after_lt
    params["run_after_lt"] = json_run_after_lt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse | None:
    if response.status_code == 200:
        response_200 = XComCollectionResponse.from_dict(response.json())

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
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse]:
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
    xcom_key: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    xcom_key_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index_filter: int | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse]:
    """Get Xcom Entries

     Get all XCom entries.

    This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCom entries for
    all DAGs.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (None | str | Unset):
        map_index (int | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        xcom_key_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index_filter (int | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        limit=limit,
        offset=offset,
        xcom_key_pattern=xcom_key_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        run_id_pattern=run_id_pattern,
        task_id_pattern=task_id_pattern,
        map_index_filter=map_index_filter,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
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
    xcom_key: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    xcom_key_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index_filter: int | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse | None:
    """Get Xcom Entries

     Get all XCom entries.

    This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCom entries for
    all DAGs.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (None | str | Unset):
        map_index (int | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        xcom_key_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index_filter (int | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        xcom_key=xcom_key,
        map_index=map_index,
        limit=limit,
        offset=offset,
        xcom_key_pattern=xcom_key_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        run_id_pattern=run_id_pattern,
        task_id_pattern=task_id_pattern,
        map_index_filter=map_index_filter,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    xcom_key: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    xcom_key_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index_filter: int | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse]:
    """Get Xcom Entries

     Get all XCom entries.

    This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCom entries for
    all DAGs.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (None | str | Unset):
        map_index (int | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        xcom_key_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index_filter (int | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        limit=limit,
        offset=offset,
        xcom_key_pattern=xcom_key_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        run_id_pattern=run_id_pattern,
        task_id_pattern=task_id_pattern,
        map_index_filter=map_index_filter,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    xcom_key: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    xcom_key_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index_filter: int | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse | None:
    """Get Xcom Entries

     Get all XCom entries.

    This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCom entries for
    all DAGs.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (None | str | Unset):
        map_index (int | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        xcom_key_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index_filter (int | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | XComCollectionResponse
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
            xcom_key=xcom_key,
            map_index=map_index,
            limit=limit,
            offset=offset,
            xcom_key_pattern=xcom_key_pattern,
            dag_display_name_pattern=dag_display_name_pattern,
            run_id_pattern=run_id_pattern,
            task_id_pattern=task_id_pattern,
            map_index_filter=map_index_filter,
            logical_date_gte=logical_date_gte,
            logical_date_gt=logical_date_gt,
            logical_date_lte=logical_date_lte,
            logical_date_lt=logical_date_lt,
            run_after_gte=run_after_gte,
            run_after_gt=run_after_gt,
            run_after_lte=run_after_lte,
            run_after_lt=run_after_lt,
        )
    ).parsed
