import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hitl_detail_collection import HITLDetailCollection
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    response_received: bool | None | Unset = UNSET,
    responded_by_user_id: list[str] | Unset = UNSET,
    responded_by_user_name: list[str] | Unset = UNSET,
    subject_search: None | str | Unset = UNSET,
    body_search: None | str | Unset = UNSET,
    created_at_gte: datetime.datetime | None | Unset = UNSET,
    created_at_gt: datetime.datetime | None | Unset = UNSET,
    created_at_lte: datetime.datetime | None | Unset = UNSET,
    created_at_lt: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_dag_id_pattern: None | str | Unset
    if isinstance(dag_id_pattern, Unset):
        json_dag_id_pattern = UNSET
    else:
        json_dag_id_pattern = dag_id_pattern
    params["dag_id_pattern"] = json_dag_id_pattern

    json_task_id: None | str | Unset
    if isinstance(task_id, Unset):
        json_task_id = UNSET
    else:
        json_task_id = task_id
    params["task_id"] = json_task_id

    json_task_id_pattern: None | str | Unset
    if isinstance(task_id_pattern, Unset):
        json_task_id_pattern = UNSET
    else:
        json_task_id_pattern = task_id_pattern
    params["task_id_pattern"] = json_task_id_pattern

    json_map_index: int | None | Unset
    if isinstance(map_index, Unset):
        json_map_index = UNSET
    else:
        json_map_index = map_index
    params["map_index"] = json_map_index

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_response_received: bool | None | Unset
    if isinstance(response_received, Unset):
        json_response_received = UNSET
    else:
        json_response_received = response_received
    params["response_received"] = json_response_received

    json_responded_by_user_id: list[str] | Unset = UNSET
    if not isinstance(responded_by_user_id, Unset):
        json_responded_by_user_id = responded_by_user_id

    params["responded_by_user_id"] = json_responded_by_user_id

    json_responded_by_user_name: list[str] | Unset = UNSET
    if not isinstance(responded_by_user_name, Unset):
        json_responded_by_user_name = responded_by_user_name

    params["responded_by_user_name"] = json_responded_by_user_name

    json_subject_search: None | str | Unset
    if isinstance(subject_search, Unset):
        json_subject_search = UNSET
    else:
        json_subject_search = subject_search
    params["subject_search"] = json_subject_search

    json_body_search: None | str | Unset
    if isinstance(body_search, Unset):
        json_body_search = UNSET
    else:
        json_body_search = body_search
    params["body_search"] = json_body_search

    json_created_at_gte: None | str | Unset
    if isinstance(created_at_gte, Unset):
        json_created_at_gte = UNSET
    elif isinstance(created_at_gte, datetime.datetime):
        json_created_at_gte = created_at_gte.isoformat()
    else:
        json_created_at_gte = created_at_gte
    params["created_at_gte"] = json_created_at_gte

    json_created_at_gt: None | str | Unset
    if isinstance(created_at_gt, Unset):
        json_created_at_gt = UNSET
    elif isinstance(created_at_gt, datetime.datetime):
        json_created_at_gt = created_at_gt.isoformat()
    else:
        json_created_at_gt = created_at_gt
    params["created_at_gt"] = json_created_at_gt

    json_created_at_lte: None | str | Unset
    if isinstance(created_at_lte, Unset):
        json_created_at_lte = UNSET
    elif isinstance(created_at_lte, datetime.datetime):
        json_created_at_lte = created_at_lte.isoformat()
    else:
        json_created_at_lte = created_at_lte
    params["created_at_lte"] = json_created_at_lte

    json_created_at_lt: None | str | Unset
    if isinstance(created_at_lt, Unset):
        json_created_at_lt = UNSET
    elif isinstance(created_at_lt, datetime.datetime):
        json_created_at_lt = created_at_lt.isoformat()
    else:
        json_created_at_lt = created_at_lt
    params["created_at_lt"] = json_created_at_lt

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/dags/{dag_id}/dagRuns/{dag_run_id}/hitlDetails".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = HITLDetailCollection.from_dict(response.json())

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
) -> Response[HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError]:
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    response_received: bool | None | Unset = UNSET,
    responded_by_user_id: list[str] | Unset = UNSET,
    responded_by_user_name: list[str] | Unset = UNSET,
    subject_search: None | str | Unset = UNSET,
    body_search: None | str | Unset = UNSET,
    created_at_gte: datetime.datetime | None | Unset = UNSET,
    created_at_gt: datetime.datetime | None | Unset = UNSET,
    created_at_lte: datetime.datetime | None | Unset = UNSET,
    created_at_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError]:
    """Get Hitl Details

     Get Human-in-the-loop details.

    Args:
        dag_id (str):
        dag_run_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `ti_id, subject, responded_at,
            created_at, responded_by_user_id, responded_by_user_name, dag_id, run_id, run_after,
            rendered_map_index, task_instance_operator, task_instance_state`
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id (None | str | Unset):
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index (int | None | Unset):
        state (list[str] | Unset):
        response_received (bool | None | Unset):
        responded_by_user_id (list[str] | Unset):
        responded_by_user_name (list[str] | Unset):
        subject_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        body_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        created_at_gte (datetime.datetime | None | Unset):
        created_at_gt (datetime.datetime | None | Unset):
        created_at_lte (datetime.datetime | None | Unset):
        created_at_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id_pattern=dag_id_pattern,
        task_id=task_id,
        task_id_pattern=task_id_pattern,
        map_index=map_index,
        state=state,
        response_received=response_received,
        responded_by_user_id=responded_by_user_id,
        responded_by_user_name=responded_by_user_name,
        subject_search=subject_search,
        body_search=body_search,
        created_at_gte=created_at_gte,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_lt=created_at_lt,
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    response_received: bool | None | Unset = UNSET,
    responded_by_user_id: list[str] | Unset = UNSET,
    responded_by_user_name: list[str] | Unset = UNSET,
    subject_search: None | str | Unset = UNSET,
    body_search: None | str | Unset = UNSET,
    created_at_gte: datetime.datetime | None | Unset = UNSET,
    created_at_gt: datetime.datetime | None | Unset = UNSET,
    created_at_lte: datetime.datetime | None | Unset = UNSET,
    created_at_lt: datetime.datetime | None | Unset = UNSET,
) -> HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Hitl Details

     Get Human-in-the-loop details.

    Args:
        dag_id (str):
        dag_run_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `ti_id, subject, responded_at,
            created_at, responded_by_user_id, responded_by_user_name, dag_id, run_id, run_after,
            rendered_map_index, task_instance_operator, task_instance_state`
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id (None | str | Unset):
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index (int | None | Unset):
        state (list[str] | Unset):
        response_received (bool | None | Unset):
        responded_by_user_id (list[str] | Unset):
        responded_by_user_name (list[str] | Unset):
        subject_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        body_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        created_at_gte (datetime.datetime | None | Unset):
        created_at_gt (datetime.datetime | None | Unset):
        created_at_lte (datetime.datetime | None | Unset):
        created_at_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id_pattern=dag_id_pattern,
        task_id=task_id,
        task_id_pattern=task_id_pattern,
        map_index=map_index,
        state=state,
        response_received=response_received,
        responded_by_user_id=responded_by_user_id,
        responded_by_user_name=responded_by_user_name,
        subject_search=subject_search,
        body_search=body_search,
        created_at_gte=created_at_gte,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_lt=created_at_lt,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    response_received: bool | None | Unset = UNSET,
    responded_by_user_id: list[str] | Unset = UNSET,
    responded_by_user_name: list[str] | Unset = UNSET,
    subject_search: None | str | Unset = UNSET,
    body_search: None | str | Unset = UNSET,
    created_at_gte: datetime.datetime | None | Unset = UNSET,
    created_at_gt: datetime.datetime | None | Unset = UNSET,
    created_at_lte: datetime.datetime | None | Unset = UNSET,
    created_at_lt: datetime.datetime | None | Unset = UNSET,
) -> Response[HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError]:
    """Get Hitl Details

     Get Human-in-the-loop details.

    Args:
        dag_id (str):
        dag_run_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `ti_id, subject, responded_at,
            created_at, responded_by_user_id, responded_by_user_name, dag_id, run_id, run_after,
            rendered_map_index, task_instance_operator, task_instance_state`
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id (None | str | Unset):
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index (int | None | Unset):
        state (list[str] | Unset):
        response_received (bool | None | Unset):
        responded_by_user_id (list[str] | Unset):
        responded_by_user_name (list[str] | Unset):
        subject_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        body_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        created_at_gte (datetime.datetime | None | Unset):
        created_at_gt (datetime.datetime | None | Unset):
        created_at_lte (datetime.datetime | None | Unset):
        created_at_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id_pattern=dag_id_pattern,
        task_id=task_id,
        task_id_pattern=task_id_pattern,
        map_index=map_index,
        state=state,
        response_received=response_received,
        responded_by_user_id=responded_by_user_id,
        responded_by_user_name=responded_by_user_name,
        subject_search=subject_search,
        body_search=body_search,
        created_at_gte=created_at_gte,
        created_at_gt=created_at_gt,
        created_at_lte=created_at_lte,
        created_at_lt=created_at_lt,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    dag_id_pattern: None | str | Unset = UNSET,
    task_id: None | str | Unset = UNSET,
    task_id_pattern: None | str | Unset = UNSET,
    map_index: int | None | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    response_received: bool | None | Unset = UNSET,
    responded_by_user_id: list[str] | Unset = UNSET,
    responded_by_user_name: list[str] | Unset = UNSET,
    subject_search: None | str | Unset = UNSET,
    body_search: None | str | Unset = UNSET,
    created_at_gte: datetime.datetime | None | Unset = UNSET,
    created_at_gt: datetime.datetime | None | Unset = UNSET,
    created_at_lte: datetime.datetime | None | Unset = UNSET,
    created_at_lt: datetime.datetime | None | Unset = UNSET,
) -> HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError | None:
    """Get Hitl Details

     Get Human-in-the-loop details.

    Args:
        dag_id (str):
        dag_run_id (str):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `ti_id, subject, responded_at,
            created_at, responded_by_user_id, responded_by_user_name, dag_id, run_id, run_after,
            rendered_map_index, task_instance_operator, task_instance_state`
        dag_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        task_id (None | str | Unset):
        task_id_pattern (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        map_index (int | None | Unset):
        state (list[str] | Unset):
        response_received (bool | None | Unset):
        responded_by_user_id (list[str] | Unset):
        responded_by_user_name (list[str] | Unset):
        subject_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        body_search (None | str | Unset): SQL LIKE expression — use `%` / `_` wildcards (e.g.
            `%customer_%`). Regular expressions are **not** supported.
        created_at_gte (datetime.datetime | None | Unset):
        created_at_gt (datetime.datetime | None | Unset):
        created_at_lte (datetime.datetime | None | Unset):
        created_at_lt (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HITLDetailCollection | HTTPExceptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id_pattern=dag_id_pattern,
            task_id=task_id,
            task_id_pattern=task_id_pattern,
            map_index=map_index,
            state=state,
            response_received=response_received,
            responded_by_user_id=responded_by_user_id,
            responded_by_user_name=responded_by_user_name,
            subject_search=subject_search,
            body_search=body_search,
            created_at_gte=created_at_gte,
            created_at_gt=created_at_gt,
            created_at_lte=created_at_lte,
            created_at_lt=created_at_lt,
        )
    ).parsed
