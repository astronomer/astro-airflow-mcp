import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_collection_response import DAGRunCollectionResponse
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
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
    run_type: list[str] | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    dag_version: list[int] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    triggering_user_name_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

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

    json_run_type: list[str] | Unset = UNSET
    if not isinstance(run_type, Unset):
        json_run_type = run_type

    params["run_type"] = json_run_type

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_dag_version: list[int] | Unset = UNSET
    if not isinstance(dag_version, Unset):
        json_dag_version = dag_version

    params["dag_version"] = json_dag_version

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_run_id_pattern: None | str | Unset
    if isinstance(run_id_pattern, Unset):
        json_run_id_pattern = UNSET
    else:
        json_run_id_pattern = run_id_pattern
    params["run_id_pattern"] = json_run_id_pattern

    json_triggering_user_name_pattern: None | str | Unset
    if isinstance(triggering_user_name_pattern, Unset):
        json_triggering_user_name_pattern = UNSET
    else:
        json_triggering_user_name_pattern = triggering_user_name_pattern
    params["triggering_user_name_pattern"] = json_triggering_user_name_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGRunCollectionResponse.from_dict(response.json())

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
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
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
    run_type: list[str] | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    dag_version: list[int] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    triggering_user_name_pattern: None | str | Unset = UNSET,
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Runs

     Get all DAG Runs.

    This endpoint allows specifying `~` as the dag_id to retrieve Dag Runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
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
        run_type (list[str] | Unset):
        state (list[str] | Unset):
        dag_version (list[int] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, dag_id, run_id,
            logical_date, run_after, start_date, end_date, updated_at, conf, duration, dag_run_id`
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        triggering_user_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
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
        run_type=run_type,
        state=state,
        dag_version=dag_version,
        order_by=order_by,
        run_id_pattern=run_id_pattern,
        triggering_user_name_pattern=triggering_user_name_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
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
    run_type: list[str] | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    dag_version: list[int] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    triggering_user_name_pattern: None | str | Unset = UNSET,
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Runs

     Get all DAG Runs.

    This endpoint allows specifying `~` as the dag_id to retrieve Dag Runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
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
        run_type (list[str] | Unset):
        state (list[str] | Unset):
        dag_version (list[int] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, dag_id, run_id,
            logical_date, run_after, start_date, end_date, updated_at, conf, duration, dag_run_id`
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        triggering_user_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        limit=limit,
        offset=offset,
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
        run_type=run_type,
        state=state,
        dag_version=dag_version,
        order_by=order_by,
        run_id_pattern=run_id_pattern,
        triggering_user_name_pattern=triggering_user_name_pattern,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
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
    run_type: list[str] | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    dag_version: list[int] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    triggering_user_name_pattern: None | str | Unset = UNSET,
) -> Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dag Runs

     Get all DAG Runs.

    This endpoint allows specifying `~` as the dag_id to retrieve Dag Runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
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
        run_type (list[str] | Unset):
        state (list[str] | Unset):
        dag_version (list[int] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, dag_id, run_id,
            logical_date, run_after, start_date, end_date, updated_at, conf, duration, dag_run_id`
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        triggering_user_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
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
        run_type=run_type,
        state=state,
        dag_version=dag_version,
        order_by=order_by,
        run_id_pattern=run_id_pattern,
        triggering_user_name_pattern=triggering_user_name_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
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
    run_type: list[str] | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    dag_version: list[int] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    run_id_pattern: None | str | Unset = UNSET,
    triggering_user_name_pattern: None | str | Unset = UNSET,
) -> DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dag Runs

     Get all DAG Runs.

    This endpoint allows specifying `~` as the dag_id to retrieve Dag Runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
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
        run_type (list[str] | Unset):
        state (list[str] | Unset):
        dag_version (list[int] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, state, dag_id, run_id,
            logical_date, run_after, start_date, end_date, updated_at, conf, duration, dag_run_id`
        run_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        triggering_user_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            limit=limit,
            offset=offset,
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
            run_type=run_type,
            state=state,
            dag_version=dag_version,
            order_by=order_by,
            run_id_pattern=run_id_pattern,
            triggering_user_name_pattern=triggering_user_name_pattern,
        )
    ).parsed
