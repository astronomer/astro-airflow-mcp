import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_collection_response import DAGCollectionResponse
from ...models.dag_run_state import DagRunState
from ...models.get_dags_tags_match_mode_type_0 import GetDagsTagsMatchModeType0
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: GetDagsTagsMatchModeType0 | None | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
    has_import_errors: bool | None | Unset = UNSET,
    last_dag_run_state: DagRunState | None | Unset = UNSET,
    bundle_name: None | str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    has_asset_schedule: bool | None | Unset = UNSET,
    asset_dependency: None | str | Unset = UNSET,
    dag_run_start_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_state: list[str] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_tags_match_mode: None | str | Unset
    if isinstance(tags_match_mode, Unset):
        json_tags_match_mode = UNSET
    elif isinstance(tags_match_mode, GetDagsTagsMatchModeType0):
        json_tags_match_mode = tags_match_mode.value
    else:
        json_tags_match_mode = tags_match_mode
    params["tags_match_mode"] = json_tags_match_mode

    json_owners: list[str] | Unset = UNSET
    if not isinstance(owners, Unset):
        json_owners = owners

    params["owners"] = json_owners

    json_dag_id_pattern: None | str | Unset
    if isinstance(dag_id_pattern, Unset):
        json_dag_id_pattern = UNSET
    else:
        json_dag_id_pattern = dag_id_pattern
    params["dag_id_pattern"] = json_dag_id_pattern

    json_dag_display_name_pattern: None | str | Unset
    if isinstance(dag_display_name_pattern, Unset):
        json_dag_display_name_pattern = UNSET
    else:
        json_dag_display_name_pattern = dag_display_name_pattern
    params["dag_display_name_pattern"] = json_dag_display_name_pattern

    params["exclude_stale"] = exclude_stale

    json_paused: bool | None | Unset
    if isinstance(paused, Unset):
        json_paused = UNSET
    else:
        json_paused = paused
    params["paused"] = json_paused

    json_has_import_errors: bool | None | Unset
    if isinstance(has_import_errors, Unset):
        json_has_import_errors = UNSET
    else:
        json_has_import_errors = has_import_errors
    params["has_import_errors"] = json_has_import_errors

    json_last_dag_run_state: None | str | Unset
    if isinstance(last_dag_run_state, Unset):
        json_last_dag_run_state = UNSET
    elif isinstance(last_dag_run_state, DagRunState):
        json_last_dag_run_state = last_dag_run_state.value
    else:
        json_last_dag_run_state = last_dag_run_state
    params["last_dag_run_state"] = json_last_dag_run_state

    json_bundle_name: None | str | Unset
    if isinstance(bundle_name, Unset):
        json_bundle_name = UNSET
    else:
        json_bundle_name = bundle_name
    params["bundle_name"] = json_bundle_name

    json_bundle_version: None | str | Unset
    if isinstance(bundle_version, Unset):
        json_bundle_version = UNSET
    else:
        json_bundle_version = bundle_version
    params["bundle_version"] = json_bundle_version

    json_has_asset_schedule: bool | None | Unset
    if isinstance(has_asset_schedule, Unset):
        json_has_asset_schedule = UNSET
    else:
        json_has_asset_schedule = has_asset_schedule
    params["has_asset_schedule"] = json_has_asset_schedule

    json_asset_dependency: None | str | Unset
    if isinstance(asset_dependency, Unset):
        json_asset_dependency = UNSET
    else:
        json_asset_dependency = asset_dependency
    params["asset_dependency"] = json_asset_dependency

    json_dag_run_start_date_gte: None | str | Unset
    if isinstance(dag_run_start_date_gte, Unset):
        json_dag_run_start_date_gte = UNSET
    elif isinstance(dag_run_start_date_gte, datetime.datetime):
        json_dag_run_start_date_gte = dag_run_start_date_gte.isoformat()
    else:
        json_dag_run_start_date_gte = dag_run_start_date_gte
    params["dag_run_start_date_gte"] = json_dag_run_start_date_gte

    json_dag_run_start_date_gt: None | str | Unset
    if isinstance(dag_run_start_date_gt, Unset):
        json_dag_run_start_date_gt = UNSET
    elif isinstance(dag_run_start_date_gt, datetime.datetime):
        json_dag_run_start_date_gt = dag_run_start_date_gt.isoformat()
    else:
        json_dag_run_start_date_gt = dag_run_start_date_gt
    params["dag_run_start_date_gt"] = json_dag_run_start_date_gt

    json_dag_run_start_date_lte: None | str | Unset
    if isinstance(dag_run_start_date_lte, Unset):
        json_dag_run_start_date_lte = UNSET
    elif isinstance(dag_run_start_date_lte, datetime.datetime):
        json_dag_run_start_date_lte = dag_run_start_date_lte.isoformat()
    else:
        json_dag_run_start_date_lte = dag_run_start_date_lte
    params["dag_run_start_date_lte"] = json_dag_run_start_date_lte

    json_dag_run_start_date_lt: None | str | Unset
    if isinstance(dag_run_start_date_lt, Unset):
        json_dag_run_start_date_lt = UNSET
    elif isinstance(dag_run_start_date_lt, datetime.datetime):
        json_dag_run_start_date_lt = dag_run_start_date_lt.isoformat()
    else:
        json_dag_run_start_date_lt = dag_run_start_date_lt
    params["dag_run_start_date_lt"] = json_dag_run_start_date_lt

    json_dag_run_end_date_gte: None | str | Unset
    if isinstance(dag_run_end_date_gte, Unset):
        json_dag_run_end_date_gte = UNSET
    elif isinstance(dag_run_end_date_gte, datetime.datetime):
        json_dag_run_end_date_gte = dag_run_end_date_gte.isoformat()
    else:
        json_dag_run_end_date_gte = dag_run_end_date_gte
    params["dag_run_end_date_gte"] = json_dag_run_end_date_gte

    json_dag_run_end_date_gt: None | str | Unset
    if isinstance(dag_run_end_date_gt, Unset):
        json_dag_run_end_date_gt = UNSET
    elif isinstance(dag_run_end_date_gt, datetime.datetime):
        json_dag_run_end_date_gt = dag_run_end_date_gt.isoformat()
    else:
        json_dag_run_end_date_gt = dag_run_end_date_gt
    params["dag_run_end_date_gt"] = json_dag_run_end_date_gt

    json_dag_run_end_date_lte: None | str | Unset
    if isinstance(dag_run_end_date_lte, Unset):
        json_dag_run_end_date_lte = UNSET
    elif isinstance(dag_run_end_date_lte, datetime.datetime):
        json_dag_run_end_date_lte = dag_run_end_date_lte.isoformat()
    else:
        json_dag_run_end_date_lte = dag_run_end_date_lte
    params["dag_run_end_date_lte"] = json_dag_run_end_date_lte

    json_dag_run_end_date_lt: None | str | Unset
    if isinstance(dag_run_end_date_lt, Unset):
        json_dag_run_end_date_lt = UNSET
    elif isinstance(dag_run_end_date_lt, datetime.datetime):
        json_dag_run_end_date_lt = dag_run_end_date_lt.isoformat()
    else:
        json_dag_run_end_date_lt = dag_run_end_date_lt
    params["dag_run_end_date_lt"] = json_dag_run_end_date_lt

    json_dag_run_state: list[str] | Unset = UNSET
    if not isinstance(dag_run_state, Unset):
        json_dag_run_state = dag_run_state

    params["dag_run_state"] = json_dag_run_state

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_is_favorite: bool | None | Unset
    if isinstance(is_favorite, Unset):
        json_is_favorite = UNSET
    else:
        json_is_favorite = is_favorite
    params["is_favorite"] = json_is_favorite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DAGCollectionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HTTPExceptionResponse.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: GetDagsTagsMatchModeType0 | None | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
    has_import_errors: bool | None | Unset = UNSET,
    last_dag_run_state: DagRunState | None | Unset = UNSET,
    bundle_name: None | str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    has_asset_schedule: bool | None | Unset = UNSET,
    asset_dependency: None | str | Unset = UNSET,
    dag_run_start_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_state: list[str] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dags

     Get all DAGs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (GetDagsTagsMatchModeType0 | None | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        has_import_errors (bool | None | Unset): Filter Dags by having import errors. Only Dags
            that have been successfully loaded before will be returned.
        last_dag_run_state (DagRunState | None | Unset):
        bundle_name (None | str | Unset):
        bundle_version (None | str | Unset):
        has_asset_schedule (bool | None | Unset): Filter Dags with asset-based scheduling
        asset_dependency (None | str | Unset): Filter Dags by asset dependency (name or URI)
        dag_run_start_date_gte (datetime.datetime | None | Unset):
        dag_run_start_date_gt (datetime.datetime | None | Unset):
        dag_run_start_date_lte (datetime.datetime | None | Unset):
        dag_run_start_date_lt (datetime.datetime | None | Unset):
        dag_run_end_date_gte (datetime.datetime | None | Unset):
        dag_run_end_date_gt (datetime.datetime | None | Unset):
        dag_run_end_date_lte (datetime.datetime | None | Unset):
        dag_run_end_date_lt (datetime.datetime | None | Unset):
        dag_run_state (list[str] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, dag_display_name,
            next_dagrun, state, start_date, last_run_state, last_run_start_date`
        is_favorite (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
        has_import_errors=has_import_errors,
        last_dag_run_state=last_dag_run_state,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        has_asset_schedule=has_asset_schedule,
        asset_dependency=asset_dependency,
        dag_run_start_date_gte=dag_run_start_date_gte,
        dag_run_start_date_gt=dag_run_start_date_gt,
        dag_run_start_date_lte=dag_run_start_date_lte,
        dag_run_start_date_lt=dag_run_start_date_lt,
        dag_run_end_date_gte=dag_run_end_date_gte,
        dag_run_end_date_gt=dag_run_end_date_gt,
        dag_run_end_date_lte=dag_run_end_date_lte,
        dag_run_end_date_lt=dag_run_end_date_lt,
        dag_run_state=dag_run_state,
        order_by=order_by,
        is_favorite=is_favorite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: GetDagsTagsMatchModeType0 | None | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
    has_import_errors: bool | None | Unset = UNSET,
    last_dag_run_state: DagRunState | None | Unset = UNSET,
    bundle_name: None | str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    has_asset_schedule: bool | None | Unset = UNSET,
    asset_dependency: None | str | Unset = UNSET,
    dag_run_start_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_state: list[str] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dags

     Get all DAGs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (GetDagsTagsMatchModeType0 | None | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        has_import_errors (bool | None | Unset): Filter Dags by having import errors. Only Dags
            that have been successfully loaded before will be returned.
        last_dag_run_state (DagRunState | None | Unset):
        bundle_name (None | str | Unset):
        bundle_version (None | str | Unset):
        has_asset_schedule (bool | None | Unset): Filter Dags with asset-based scheduling
        asset_dependency (None | str | Unset): Filter Dags by asset dependency (name or URI)
        dag_run_start_date_gte (datetime.datetime | None | Unset):
        dag_run_start_date_gt (datetime.datetime | None | Unset):
        dag_run_start_date_lte (datetime.datetime | None | Unset):
        dag_run_start_date_lt (datetime.datetime | None | Unset):
        dag_run_end_date_gte (datetime.datetime | None | Unset):
        dag_run_end_date_gt (datetime.datetime | None | Unset):
        dag_run_end_date_lte (datetime.datetime | None | Unset):
        dag_run_end_date_lt (datetime.datetime | None | Unset):
        dag_run_state (list[str] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, dag_display_name,
            next_dagrun, state, start_date, last_run_state, last_run_start_date`
        is_favorite (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
        has_import_errors=has_import_errors,
        last_dag_run_state=last_dag_run_state,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        has_asset_schedule=has_asset_schedule,
        asset_dependency=asset_dependency,
        dag_run_start_date_gte=dag_run_start_date_gte,
        dag_run_start_date_gt=dag_run_start_date_gt,
        dag_run_start_date_lte=dag_run_start_date_lte,
        dag_run_start_date_lt=dag_run_start_date_lt,
        dag_run_end_date_gte=dag_run_end_date_gte,
        dag_run_end_date_gt=dag_run_end_date_gt,
        dag_run_end_date_lte=dag_run_end_date_lte,
        dag_run_end_date_lt=dag_run_end_date_lt,
        dag_run_state=dag_run_state,
        order_by=order_by,
        is_favorite=is_favorite,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: GetDagsTagsMatchModeType0 | None | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
    has_import_errors: bool | None | Unset = UNSET,
    last_dag_run_state: DagRunState | None | Unset = UNSET,
    bundle_name: None | str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    has_asset_schedule: bool | None | Unset = UNSET,
    asset_dependency: None | str | Unset = UNSET,
    dag_run_start_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_state: list[str] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]:
    """Get Dags

     Get all DAGs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (GetDagsTagsMatchModeType0 | None | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        has_import_errors (bool | None | Unset): Filter Dags by having import errors. Only Dags
            that have been successfully loaded before will be returned.
        last_dag_run_state (DagRunState | None | Unset):
        bundle_name (None | str | Unset):
        bundle_version (None | str | Unset):
        has_asset_schedule (bool | None | Unset): Filter Dags with asset-based scheduling
        asset_dependency (None | str | Unset): Filter Dags by asset dependency (name or URI)
        dag_run_start_date_gte (datetime.datetime | None | Unset):
        dag_run_start_date_gt (datetime.datetime | None | Unset):
        dag_run_start_date_lte (datetime.datetime | None | Unset):
        dag_run_start_date_lt (datetime.datetime | None | Unset):
        dag_run_end_date_gte (datetime.datetime | None | Unset):
        dag_run_end_date_gt (datetime.datetime | None | Unset):
        dag_run_end_date_lte (datetime.datetime | None | Unset):
        dag_run_end_date_lt (datetime.datetime | None | Unset):
        dag_run_state (list[str] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, dag_display_name,
            next_dagrun, state, start_date, last_run_state, last_run_start_date`
        is_favorite (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        tags=tags,
        tags_match_mode=tags_match_mode,
        owners=owners,
        dag_id_pattern=dag_id_pattern,
        dag_display_name_pattern=dag_display_name_pattern,
        exclude_stale=exclude_stale,
        paused=paused,
        has_import_errors=has_import_errors,
        last_dag_run_state=last_dag_run_state,
        bundle_name=bundle_name,
        bundle_version=bundle_version,
        has_asset_schedule=has_asset_schedule,
        asset_dependency=asset_dependency,
        dag_run_start_date_gte=dag_run_start_date_gte,
        dag_run_start_date_gt=dag_run_start_date_gt,
        dag_run_start_date_lte=dag_run_start_date_lte,
        dag_run_start_date_lt=dag_run_start_date_lt,
        dag_run_end_date_gte=dag_run_end_date_gte,
        dag_run_end_date_gt=dag_run_end_date_gt,
        dag_run_end_date_lte=dag_run_end_date_lte,
        dag_run_end_date_lt=dag_run_end_date_lt,
        dag_run_state=dag_run_state,
        order_by=order_by,
        is_favorite=is_favorite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    tags: list[str] | Unset = UNSET,
    tags_match_mode: GetDagsTagsMatchModeType0 | None | Unset = UNSET,
    owners: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    dag_display_name_pattern: None | str | Unset = UNSET,
    exclude_stale: bool | Unset = True,
    paused: bool | None | Unset = UNSET,
    has_import_errors: bool | None | Unset = UNSET,
    last_dag_run_state: DagRunState | None | Unset = UNSET,
    bundle_name: None | str | Unset = UNSET,
    bundle_version: None | str | Unset = UNSET,
    has_asset_schedule: bool | None | Unset = UNSET,
    asset_dependency: None | str | Unset = UNSET,
    dag_run_start_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_start_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_gt: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lte: datetime.datetime | None | Unset = UNSET,
    dag_run_end_date_lt: datetime.datetime | None | Unset = UNSET,
    dag_run_state: list[str] | Unset = UNSET,
    order_by: list[str] | Unset = UNSET,
    is_favorite: bool | None | Unset = UNSET,
) -> DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Dags

     Get all DAGs.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        tags (list[str] | Unset):
        tags_match_mode (GetDagsTagsMatchModeType0 | None | Unset):
        owners (list[str] | Unset):
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        dag_display_name_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_`
            wildcards (e.g. `%customer_%`). Regular expressions are **not** supported.
        exclude_stale (bool | Unset):  Default: True.
        paused (bool | None | Unset):
        has_import_errors (bool | None | Unset): Filter Dags by having import errors. Only Dags
            that have been successfully loaded before will be returned.
        last_dag_run_state (DagRunState | None | Unset):
        bundle_name (None | str | Unset):
        bundle_version (None | str | Unset):
        has_asset_schedule (bool | None | Unset): Filter Dags with asset-based scheduling
        asset_dependency (None | str | Unset): Filter Dags by asset dependency (name or URI)
        dag_run_start_date_gte (datetime.datetime | None | Unset):
        dag_run_start_date_gt (datetime.datetime | None | Unset):
        dag_run_start_date_lte (datetime.datetime | None | Unset):
        dag_run_start_date_lt (datetime.datetime | None | Unset):
        dag_run_end_date_gte (datetime.datetime | None | Unset):
        dag_run_end_date_gt (datetime.datetime | None | Unset):
        dag_run_end_date_lte (datetime.datetime | None | Unset):
        dag_run_end_date_lt (datetime.datetime | None | Unset):
        dag_run_state (list[str] | Unset):
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `dag_id, dag_display_name,
            next_dagrun, state, start_date, last_run_state, last_run_start_date`
        is_favorite (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGCollectionResponse | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            tags=tags,
            tags_match_mode=tags_match_mode,
            owners=owners,
            dag_id_pattern=dag_id_pattern,
            dag_display_name_pattern=dag_display_name_pattern,
            exclude_stale=exclude_stale,
            paused=paused,
            has_import_errors=has_import_errors,
            last_dag_run_state=last_dag_run_state,
            bundle_name=bundle_name,
            bundle_version=bundle_version,
            has_asset_schedule=has_asset_schedule,
            asset_dependency=asset_dependency,
            dag_run_start_date_gte=dag_run_start_date_gte,
            dag_run_start_date_gt=dag_run_start_date_gt,
            dag_run_start_date_lte=dag_run_start_date_lte,
            dag_run_start_date_lt=dag_run_start_date_lt,
            dag_run_end_date_gte=dag_run_end_date_gte,
            dag_run_end_date_gt=dag_run_end_date_gt,
            dag_run_end_date_lte=dag_run_end_date_lte,
            dag_run_end_date_lt=dag_run_end_date_lt,
            dag_run_state=dag_run_state,
            order_by=order_by,
            is_favorite=is_favorite,
        )
    ).parsed
