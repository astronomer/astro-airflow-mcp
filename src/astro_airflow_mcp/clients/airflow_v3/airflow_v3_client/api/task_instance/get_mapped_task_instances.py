import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.task_instance_collection_response import TaskInstanceCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    updated_at_gte: datetime.datetime | None | Unset = UNSET,
    updated_at_gt: datetime.datetime | None | Unset = UNSET,
    updated_at_lte: datetime.datetime | None | Unset = UNSET,
    updated_at_lt: datetime.datetime | None | Unset = UNSET,
    duration_gte: float | None | Unset = UNSET,
    duration_gt: float | None | Unset = UNSET,
    duration_lte: float | None | Unset = UNSET,
    duration_lt: float | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    queue: list[str] | Unset = UNSET,
    executor: list[str] | Unset = UNSET,
    version_number: list[int] | Unset = UNSET,
    try_number: list[int] | Unset = UNSET,
    operator: list[str] | Unset = UNSET,
    map_index: list[int] | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_start_date_gte: None | str | Unset
    if isinstance(start_date_gte, Unset):
        json_start_date_gte = UNSET
    elif isinstance(start_date_gte, datetime.datetime):
        json_start_date_gte = start_date_gte.isoformat()
    else:
        json_start_date_gte = start_date_gte
    params["start_date_gte"] = json_start_date_gte

    json_start_date_gt: None | str | Unset
    if isinstance(start_date_gt, Unset):
        json_start_date_gt = UNSET
    elif isinstance(start_date_gt, datetime.datetime):
        json_start_date_gt = start_date_gt.isoformat()
    else:
        json_start_date_gt = start_date_gt
    params["start_date_gt"] = json_start_date_gt

    json_start_date_lte: None | str | Unset
    if isinstance(start_date_lte, Unset):
        json_start_date_lte = UNSET
    elif isinstance(start_date_lte, datetime.datetime):
        json_start_date_lte = start_date_lte.isoformat()
    else:
        json_start_date_lte = start_date_lte
    params["start_date_lte"] = json_start_date_lte

    json_start_date_lt: None | str | Unset
    if isinstance(start_date_lt, Unset):
        json_start_date_lt = UNSET
    elif isinstance(start_date_lt, datetime.datetime):
        json_start_date_lt = start_date_lt.isoformat()
    else:
        json_start_date_lt = start_date_lt
    params["start_date_lt"] = json_start_date_lt

    json_end_date_gte: None | str | Unset
    if isinstance(end_date_gte, Unset):
        json_end_date_gte = UNSET
    elif isinstance(end_date_gte, datetime.datetime):
        json_end_date_gte = end_date_gte.isoformat()
    else:
        json_end_date_gte = end_date_gte
    params["end_date_gte"] = json_end_date_gte

    json_end_date_gt: None | str | Unset
    if isinstance(end_date_gt, Unset):
        json_end_date_gt = UNSET
    elif isinstance(end_date_gt, datetime.datetime):
        json_end_date_gt = end_date_gt.isoformat()
    else:
        json_end_date_gt = end_date_gt
    params["end_date_gt"] = json_end_date_gt

    json_end_date_lte: None | str | Unset
    if isinstance(end_date_lte, Unset):
        json_end_date_lte = UNSET
    elif isinstance(end_date_lte, datetime.datetime):
        json_end_date_lte = end_date_lte.isoformat()
    else:
        json_end_date_lte = end_date_lte
    params["end_date_lte"] = json_end_date_lte

    json_end_date_lt: None | str | Unset
    if isinstance(end_date_lt, Unset):
        json_end_date_lt = UNSET
    elif isinstance(end_date_lt, datetime.datetime):
        json_end_date_lt = end_date_lt.isoformat()
    else:
        json_end_date_lt = end_date_lt
    params["end_date_lt"] = json_end_date_lt

    json_updated_at_gte: None | str | Unset
    if isinstance(updated_at_gte, Unset):
        json_updated_at_gte = UNSET
    elif isinstance(updated_at_gte, datetime.datetime):
        json_updated_at_gte = updated_at_gte.isoformat()
    else:
        json_updated_at_gte = updated_at_gte
    params["updated_at_gte"] = json_updated_at_gte

    json_updated_at_gt: None | str | Unset
    if isinstance(updated_at_gt, Unset):
        json_updated_at_gt = UNSET
    elif isinstance(updated_at_gt, datetime.datetime):
        json_updated_at_gt = updated_at_gt.isoformat()
    else:
        json_updated_at_gt = updated_at_gt
    params["updated_at_gt"] = json_updated_at_gt

    json_updated_at_lte: None | str | Unset
    if isinstance(updated_at_lte, Unset):
        json_updated_at_lte = UNSET
    elif isinstance(updated_at_lte, datetime.datetime):
        json_updated_at_lte = updated_at_lte.isoformat()
    else:
        json_updated_at_lte = updated_at_lte
    params["updated_at_lte"] = json_updated_at_lte

    json_updated_at_lt: None | str | Unset
    if isinstance(updated_at_lt, Unset):
        json_updated_at_lt = UNSET
    elif isinstance(updated_at_lt, datetime.datetime):
        json_updated_at_lt = updated_at_lt.isoformat()
    else:
        json_updated_at_lt = updated_at_lt
    params["updated_at_lt"] = json_updated_at_lt

    json_duration_gte: float | None | Unset
    if isinstance(duration_gte, Unset):
        json_duration_gte = UNSET
    else:
        json_duration_gte = duration_gte
    params["duration_gte"] = json_duration_gte

    json_duration_gt: float | None | Unset
    if isinstance(duration_gt, Unset):
        json_duration_gt = UNSET
    else:
        json_duration_gt = duration_gt
    params["duration_gt"] = json_duration_gt

    json_duration_lte: float | None | Unset
    if isinstance(duration_lte, Unset):
        json_duration_lte = UNSET
    else:
        json_duration_lte = duration_lte
    params["duration_lte"] = json_duration_lte

    json_duration_lt: float | None | Unset
    if isinstance(duration_lt, Unset):
        json_duration_lt = UNSET
    else:
        json_duration_lt = duration_lt
    params["duration_lt"] = json_duration_lt

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_pool: list[str] | Unset = UNSET
    if not isinstance(pool, Unset):
        json_pool = pool

    params["pool"] = json_pool

    json_queue: list[str] | Unset = UNSET
    if not isinstance(queue, Unset):
        json_queue = queue

    params["queue"] = json_queue

    json_executor: list[str] | Unset = UNSET
    if not isinstance(executor, Unset):
        json_executor = executor

    params["executor"] = json_executor

    json_version_number: list[int] | Unset = UNSET
    if not isinstance(version_number, Unset):
        json_version_number = version_number

    params["version_number"] = json_version_number

    json_try_number: list[int] | Unset = UNSET
    if not isinstance(try_number, Unset):
        json_try_number = try_number

    params["try_number"] = json_try_number

    json_operator: list[str] | Unset = UNSET
    if not isinstance(operator, Unset):
        json_operator = operator

    params["operator"] = json_operator

    json_map_index: list[int] | Unset = UNSET
    if not isinstance(map_index, Unset):
        json_map_index = map_index

    params["map_index"] = json_map_index

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
        "params": params,
    }

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
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    updated_at_gte: datetime.datetime | None | Unset = UNSET,
    updated_at_gt: datetime.datetime | None | Unset = UNSET,
    updated_at_lte: datetime.datetime | None | Unset = UNSET,
    updated_at_lt: datetime.datetime | None | Unset = UNSET,
    duration_gte: float | None | Unset = UNSET,
    duration_gt: float | None | Unset = UNSET,
    duration_lte: float | None | Unset = UNSET,
    duration_lt: float | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    queue: list[str] | Unset = UNSET,
    executor: list[str] | Unset = UNSET,
    version_number: list[int] | Unset = UNSET,
    try_number: list[int] | Unset = UNSET,
    operator: list[str] | Unset = UNSET,
    map_index: list[int] | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Get Mapped Task Instances

     Get list of mapped task instances.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        updated_at_gte (datetime.datetime | None | Unset):
        updated_at_gt (datetime.datetime | None | Unset):
        updated_at_lte (datetime.datetime | None | Unset):
        updated_at_lt (datetime.datetime | None | Unset):
        duration_gte (float | None | Unset):
        duration_gt (float | None | Unset):
        duration_lte (float | None | Unset):
        duration_lt (float | None | Unset):
        state (list[str] | Unset):
        pool (list[str] | Unset):
        queue (list[str] | Unset):
        executor (list[str] | Unset):
        version_number (list[int] | Unset):
        try_number (list[int] | Unset):
        operator (list[str] | Unset):
        map_index (list[int] | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, duration,
            start_date, end_date, map_index, try_number, logical_date, run_after, data_interval_start,
            data_interval_end, rendered_map_index, operator, run_after, logical_date,
            data_interval_start, data_interval_end`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        updated_at_gte=updated_at_gte,
        updated_at_gt=updated_at_gt,
        updated_at_lte=updated_at_lte,
        updated_at_lt=updated_at_lt,
        duration_gte=duration_gte,
        duration_gt=duration_gt,
        duration_lte=duration_lte,
        duration_lt=duration_lt,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
        version_number=version_number,
        try_number=try_number,
        operator=operator,
        map_index=map_index,
        limit=limit,
        offset=offset,
        order_by=order_by,
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
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    updated_at_gte: datetime.datetime | None | Unset = UNSET,
    updated_at_gt: datetime.datetime | None | Unset = UNSET,
    updated_at_lte: datetime.datetime | None | Unset = UNSET,
    updated_at_lt: datetime.datetime | None | Unset = UNSET,
    duration_gte: float | None | Unset = UNSET,
    duration_gt: float | None | Unset = UNSET,
    duration_lte: float | None | Unset = UNSET,
    duration_lt: float | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    queue: list[str] | Unset = UNSET,
    executor: list[str] | Unset = UNSET,
    version_number: list[int] | Unset = UNSET,
    try_number: list[int] | Unset = UNSET,
    operator: list[str] | Unset = UNSET,
    map_index: list[int] | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Get Mapped Task Instances

     Get list of mapped task instances.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        updated_at_gte (datetime.datetime | None | Unset):
        updated_at_gt (datetime.datetime | None | Unset):
        updated_at_lte (datetime.datetime | None | Unset):
        updated_at_lt (datetime.datetime | None | Unset):
        duration_gte (float | None | Unset):
        duration_gt (float | None | Unset):
        duration_lte (float | None | Unset):
        duration_lt (float | None | Unset):
        state (list[str] | Unset):
        pool (list[str] | Unset):
        queue (list[str] | Unset):
        executor (list[str] | Unset):
        version_number (list[int] | Unset):
        try_number (list[int] | Unset):
        operator (list[str] | Unset):
        map_index (list[int] | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, duration,
            start_date, end_date, map_index, try_number, logical_date, run_after, data_interval_start,
            data_interval_end, rendered_map_index, operator, run_after, logical_date,
            data_interval_start, data_interval_end`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        updated_at_gte=updated_at_gte,
        updated_at_gt=updated_at_gt,
        updated_at_lte=updated_at_lte,
        updated_at_lt=updated_at_lt,
        duration_gte=duration_gte,
        duration_gt=duration_gt,
        duration_lte=duration_lte,
        duration_lt=duration_lt,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
        version_number=version_number,
        try_number=try_number,
        operator=operator,
        map_index=map_index,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    updated_at_gte: datetime.datetime | None | Unset = UNSET,
    updated_at_gt: datetime.datetime | None | Unset = UNSET,
    updated_at_lte: datetime.datetime | None | Unset = UNSET,
    updated_at_lt: datetime.datetime | None | Unset = UNSET,
    duration_gte: float | None | Unset = UNSET,
    duration_gt: float | None | Unset = UNSET,
    duration_lte: float | None | Unset = UNSET,
    duration_lt: float | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    queue: list[str] | Unset = UNSET,
    executor: list[str] | Unset = UNSET,
    version_number: list[int] | Unset = UNSET,
    try_number: list[int] | Unset = UNSET,
    operator: list[str] | Unset = UNSET,
    map_index: list[int] | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]:
    """Get Mapped Task Instances

     Get list of mapped task instances.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        updated_at_gte (datetime.datetime | None | Unset):
        updated_at_gt (datetime.datetime | None | Unset):
        updated_at_lte (datetime.datetime | None | Unset):
        updated_at_lt (datetime.datetime | None | Unset):
        duration_gte (float | None | Unset):
        duration_gt (float | None | Unset):
        duration_lte (float | None | Unset):
        duration_lt (float | None | Unset):
        state (list[str] | Unset):
        pool (list[str] | Unset):
        queue (list[str] | Unset):
        executor (list[str] | Unset):
        version_number (list[int] | Unset):
        try_number (list[int] | Unset):
        operator (list[str] | Unset):
        map_index (list[int] | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, duration,
            start_date, end_date, map_index, try_number, logical_date, run_after, data_interval_start,
            data_interval_end, rendered_map_index, operator, run_after, logical_date,
            data_interval_start, data_interval_end`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        run_after_gte=run_after_gte,
        run_after_gt=run_after_gt,
        run_after_lte=run_after_lte,
        run_after_lt=run_after_lt,
        logical_date_gte=logical_date_gte,
        logical_date_gt=logical_date_gt,
        logical_date_lte=logical_date_lte,
        logical_date_lt=logical_date_lt,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        updated_at_gte=updated_at_gte,
        updated_at_gt=updated_at_gt,
        updated_at_lte=updated_at_lte,
        updated_at_lt=updated_at_lt,
        duration_gte=duration_gte,
        duration_gt=duration_gt,
        duration_lte=duration_lte,
        duration_lt=duration_lt,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
        version_number=version_number,
        try_number=try_number,
        operator=operator,
        map_index=map_index,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: AuthenticatedClient,
    run_after_gte: datetime.datetime | None | Unset = UNSET,
    run_after_gt: datetime.datetime | None | Unset = UNSET,
    run_after_lte: datetime.datetime | None | Unset = UNSET,
    run_after_lt: datetime.datetime | None | Unset = UNSET,
    logical_date_gte: datetime.datetime | None | Unset = UNSET,
    logical_date_gt: datetime.datetime | None | Unset = UNSET,
    logical_date_lte: datetime.datetime | None | Unset = UNSET,
    logical_date_lt: datetime.datetime | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    updated_at_gte: datetime.datetime | None | Unset = UNSET,
    updated_at_gt: datetime.datetime | None | Unset = UNSET,
    updated_at_lte: datetime.datetime | None | Unset = UNSET,
    updated_at_lt: datetime.datetime | None | Unset = UNSET,
    duration_gte: float | None | Unset = UNSET,
    duration_gt: float | None | Unset = UNSET,
    duration_lte: float | None | Unset = UNSET,
    duration_lt: float | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    queue: list[str] | Unset = UNSET,
    executor: list[str] | Unset = UNSET,
    version_number: list[int] | Unset = UNSET,
    try_number: list[int] | Unset = UNSET,
    operator: list[str] | Unset = UNSET,
    map_index: list[int] | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | TaskInstanceCollectionResponse | None:
    """Get Mapped Task Instances

     Get list of mapped task instances.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        updated_at_gte (datetime.datetime | None | Unset):
        updated_at_gt (datetime.datetime | None | Unset):
        updated_at_lte (datetime.datetime | None | Unset):
        updated_at_lt (datetime.datetime | None | Unset):
        duration_gte (float | None | Unset):
        duration_gt (float | None | Unset):
        duration_lte (float | None | Unset):
        duration_lt (float | None | Unset):
        state (list[str] | Unset):
        pool (list[str] | Unset):
        queue (list[str] | Unset):
        executor (list[str] | Unset):
        version_number (list[int] | Unset):
        try_number (list[int] | Unset):
        operator (list[str] | Unset):
        map_index (list[int] | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, duration,
            start_date, end_date, map_index, try_number, logical_date, run_after, data_interval_start,
            data_interval_end, rendered_map_index, operator, run_after, logical_date,
            data_interval_start, data_interval_end`

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
            task_id=task_id,
            client=client,
            run_after_gte=run_after_gte,
            run_after_gt=run_after_gt,
            run_after_lte=run_after_lte,
            run_after_lt=run_after_lt,
            logical_date_gte=logical_date_gte,
            logical_date_gt=logical_date_gt,
            logical_date_lte=logical_date_lte,
            logical_date_lt=logical_date_lt,
            start_date_gte=start_date_gte,
            start_date_gt=start_date_gt,
            start_date_lte=start_date_lte,
            start_date_lt=start_date_lt,
            end_date_gte=end_date_gte,
            end_date_gt=end_date_gt,
            end_date_lte=end_date_lte,
            end_date_lt=end_date_lt,
            updated_at_gte=updated_at_gte,
            updated_at_gt=updated_at_gt,
            updated_at_lte=updated_at_lte,
            updated_at_lt=updated_at_lt,
            duration_gte=duration_gte,
            duration_gt=duration_gt,
            duration_lte=duration_lte,
            duration_lt=duration_lt,
            state=state,
            pool=pool,
            queue=queue,
            executor=executor,
            version_number=version_number,
            try_number=try_number,
            operator=operator,
            map_index=map_index,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
