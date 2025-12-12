import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_collection import DAGRunCollection
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    execution_date_gte: datetime.datetime | Unset = UNSET,
    execution_date_lte: datetime.datetime | Unset = UNSET,
    start_date_gte: datetime.datetime | Unset = UNSET,
    start_date_lte: datetime.datetime | Unset = UNSET,
    end_date_gte: datetime.datetime | Unset = UNSET,
    end_date_lte: datetime.datetime | Unset = UNSET,
    updated_at_gte: datetime.datetime | Unset = UNSET,
    updated_at_lte: datetime.datetime | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    order_by: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_execution_date_gte: str | Unset = UNSET
    if not isinstance(execution_date_gte, Unset):
        json_execution_date_gte = execution_date_gte.isoformat()
    params["execution_date_gte"] = json_execution_date_gte

    json_execution_date_lte: str | Unset = UNSET
    if not isinstance(execution_date_lte, Unset):
        json_execution_date_lte = execution_date_lte.isoformat()
    params["execution_date_lte"] = json_execution_date_lte

    json_start_date_gte: str | Unset = UNSET
    if not isinstance(start_date_gte, Unset):
        json_start_date_gte = start_date_gte.isoformat()
    params["start_date_gte"] = json_start_date_gte

    json_start_date_lte: str | Unset = UNSET
    if not isinstance(start_date_lte, Unset):
        json_start_date_lte = start_date_lte.isoformat()
    params["start_date_lte"] = json_start_date_lte

    json_end_date_gte: str | Unset = UNSET
    if not isinstance(end_date_gte, Unset):
        json_end_date_gte = end_date_gte.isoformat()
    params["end_date_gte"] = json_end_date_gte

    json_end_date_lte: str | Unset = UNSET
    if not isinstance(end_date_lte, Unset):
        json_end_date_lte = end_date_lte.isoformat()
    params["end_date_lte"] = json_end_date_lte

    json_updated_at_gte: str | Unset = UNSET
    if not isinstance(updated_at_gte, Unset):
        json_updated_at_gte = updated_at_gte.isoformat()
    params["updated_at_gte"] = json_updated_at_gte

    json_updated_at_lte: str | Unset = UNSET
    if not isinstance(updated_at_lte, Unset):
        json_updated_at_lte = updated_at_lte.isoformat()
    params["updated_at_lte"] = json_updated_at_lte

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params["order_by"] = order_by

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/dagRuns".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DAGRunCollection | Error | None:
    if response.status_code == 200:
        response_200 = DAGRunCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DAGRunCollection | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    execution_date_gte: datetime.datetime | Unset = UNSET,
    execution_date_lte: datetime.datetime | Unset = UNSET,
    start_date_gte: datetime.datetime | Unset = UNSET,
    start_date_lte: datetime.datetime | Unset = UNSET,
    end_date_gte: datetime.datetime | Unset = UNSET,
    end_date_lte: datetime.datetime | Unset = UNSET,
    updated_at_gte: datetime.datetime | Unset = UNSET,
    updated_at_lte: datetime.datetime | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    order_by: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
) -> Response[DAGRunCollection | Error]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        execution_date_gte (datetime.datetime | Unset):
        execution_date_lte (datetime.datetime | Unset):
        start_date_gte (datetime.datetime | Unset):
        start_date_lte (datetime.datetime | Unset):
        end_date_gte (datetime.datetime | Unset):
        end_date_lte (datetime.datetime | Unset):
        updated_at_gte (datetime.datetime | Unset):
        updated_at_lte (datetime.datetime | Unset):
        state (list[str] | Unset):
        order_by (str | Unset):
        fields (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollection | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    execution_date_gte: datetime.datetime | Unset = UNSET,
    execution_date_lte: datetime.datetime | Unset = UNSET,
    start_date_gte: datetime.datetime | Unset = UNSET,
    start_date_lte: datetime.datetime | Unset = UNSET,
    end_date_gte: datetime.datetime | Unset = UNSET,
    end_date_lte: datetime.datetime | Unset = UNSET,
    updated_at_gte: datetime.datetime | Unset = UNSET,
    updated_at_lte: datetime.datetime | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    order_by: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
) -> DAGRunCollection | Error | None:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        execution_date_gte (datetime.datetime | Unset):
        execution_date_lte (datetime.datetime | Unset):
        start_date_gte (datetime.datetime | Unset):
        start_date_lte (datetime.datetime | Unset):
        end_date_gte (datetime.datetime | Unset):
        end_date_lte (datetime.datetime | Unset):
        updated_at_gte (datetime.datetime | Unset):
        updated_at_lte (datetime.datetime | Unset):
        state (list[str] | Unset):
        order_by (str | Unset):
        fields (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollection | Error
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    execution_date_gte: datetime.datetime | Unset = UNSET,
    execution_date_lte: datetime.datetime | Unset = UNSET,
    start_date_gte: datetime.datetime | Unset = UNSET,
    start_date_lte: datetime.datetime | Unset = UNSET,
    end_date_gte: datetime.datetime | Unset = UNSET,
    end_date_lte: datetime.datetime | Unset = UNSET,
    updated_at_gte: datetime.datetime | Unset = UNSET,
    updated_at_lte: datetime.datetime | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    order_by: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
) -> Response[DAGRunCollection | Error]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        execution_date_gte (datetime.datetime | Unset):
        execution_date_lte (datetime.datetime | Unset):
        start_date_gte (datetime.datetime | Unset):
        start_date_lte (datetime.datetime | Unset):
        end_date_gte (datetime.datetime | Unset):
        end_date_lte (datetime.datetime | Unset):
        updated_at_gte (datetime.datetime | Unset):
        updated_at_lte (datetime.datetime | Unset):
        state (list[str] | Unset):
        order_by (str | Unset):
        fields (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DAGRunCollection | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    offset: int | Unset = UNSET,
    execution_date_gte: datetime.datetime | Unset = UNSET,
    execution_date_lte: datetime.datetime | Unset = UNSET,
    start_date_gte: datetime.datetime | Unset = UNSET,
    start_date_lte: datetime.datetime | Unset = UNSET,
    end_date_gte: datetime.datetime | Unset = UNSET,
    end_date_lte: datetime.datetime | Unset = UNSET,
    updated_at_gte: datetime.datetime | Unset = UNSET,
    updated_at_lte: datetime.datetime | Unset = UNSET,
    state: list[str] | Unset = UNSET,
    order_by: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
) -> DAGRunCollection | Error | None:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):
        execution_date_gte (datetime.datetime | Unset):
        execution_date_lte (datetime.datetime | Unset):
        start_date_gte (datetime.datetime | Unset):
        start_date_lte (datetime.datetime | Unset):
        end_date_gte (datetime.datetime | Unset):
        end_date_lte (datetime.datetime | Unset):
        updated_at_gte (datetime.datetime | Unset):
        updated_at_lte (datetime.datetime | Unset):
        state (list[str] | Unset):
        order_by (str | Unset):
        fields (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DAGRunCollection | Error
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            updated_at_gte=updated_at_gte,
            updated_at_lte=updated_at_lte,
            state=state,
            order_by=order_by,
            fields=fields,
        )
    ).parsed
