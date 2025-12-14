import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_response import HTTPExceptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.job_collection_response import JobCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_alive: bool | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    job_state: None | str | Unset = UNSET,
    job_type: None | str | Unset = UNSET,
    hostname: None | str | Unset = UNSET,
    executor_class: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_is_alive: bool | None | Unset
    if isinstance(is_alive, Unset):
        json_is_alive = UNSET
    else:
        json_is_alive = is_alive
    params["is_alive"] = json_is_alive

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

    params["limit"] = limit

    params["offset"] = offset

    json_order_by: list[str] | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["order_by"] = json_order_by

    json_job_state: None | str | Unset
    if isinstance(job_state, Unset):
        json_job_state = UNSET
    else:
        json_job_state = job_state
    params["job_state"] = json_job_state

    json_job_type: None | str | Unset
    if isinstance(job_type, Unset):
        json_job_type = UNSET
    else:
        json_job_type = job_type
    params["job_type"] = json_job_type

    json_hostname: None | str | Unset
    if isinstance(hostname, Unset):
        json_hostname = UNSET
    else:
        json_hostname = hostname
    params["hostname"] = json_hostname

    json_executor_class: None | str | Unset
    if isinstance(executor_class, Unset):
        json_executor_class = UNSET
    else:
        json_executor_class = executor_class
    params["executor_class"] = json_executor_class

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse | None:
    if response.status_code == 200:
        response_200 = JobCollectionResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_alive: bool | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    job_state: None | str | Unset = UNSET,
    job_type: None | str | Unset = UNSET,
    hostname: None | str | Unset = UNSET,
    executor_class: None | str | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse]:
    """Get Jobs

     Get all jobs.

    Args:
        is_alive (bool | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dag_id, state, job_type,
            start_date, end_date, latest_heartbeat, executor_class, hostname, unixname`
        job_state (None | str | Unset):
        job_type (None | str | Unset):
        hostname (None | str | Unset):
        executor_class (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse]
    """

    kwargs = _get_kwargs(
        is_alive=is_alive,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        limit=limit,
        offset=offset,
        order_by=order_by,
        job_state=job_state,
        job_type=job_type,
        hostname=hostname,
        executor_class=executor_class,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_alive: bool | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    job_state: None | str | Unset = UNSET,
    job_type: None | str | Unset = UNSET,
    hostname: None | str | Unset = UNSET,
    executor_class: None | str | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse | None:
    """Get Jobs

     Get all jobs.

    Args:
        is_alive (bool | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dag_id, state, job_type,
            start_date, end_date, latest_heartbeat, executor_class, hostname, unixname`
        job_state (None | str | Unset):
        job_type (None | str | Unset):
        hostname (None | str | Unset):
        executor_class (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse
    """

    return sync_detailed(
        client=client,
        is_alive=is_alive,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        limit=limit,
        offset=offset,
        order_by=order_by,
        job_state=job_state,
        job_type=job_type,
        hostname=hostname,
        executor_class=executor_class,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_alive: bool | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    job_state: None | str | Unset = UNSET,
    job_type: None | str | Unset = UNSET,
    hostname: None | str | Unset = UNSET,
    executor_class: None | str | Unset = UNSET,
) -> Response[HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse]:
    """Get Jobs

     Get all jobs.

    Args:
        is_alive (bool | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dag_id, state, job_type,
            start_date, end_date, latest_heartbeat, executor_class, hostname, unixname`
        job_state (None | str | Unset):
        job_type (None | str | Unset):
        hostname (None | str | Unset):
        executor_class (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse]
    """

    kwargs = _get_kwargs(
        is_alive=is_alive,
        start_date_gte=start_date_gte,
        start_date_gt=start_date_gt,
        start_date_lte=start_date_lte,
        start_date_lt=start_date_lt,
        end_date_gte=end_date_gte,
        end_date_gt=end_date_gt,
        end_date_lte=end_date_lte,
        end_date_lt=end_date_lt,
        limit=limit,
        offset=offset,
        order_by=order_by,
        job_state=job_state,
        job_type=job_type,
        hostname=hostname,
        executor_class=executor_class,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_alive: bool | None | Unset = UNSET,
    start_date_gte: datetime.datetime | None | Unset = UNSET,
    start_date_gt: datetime.datetime | None | Unset = UNSET,
    start_date_lte: datetime.datetime | None | Unset = UNSET,
    start_date_lt: datetime.datetime | None | Unset = UNSET,
    end_date_gte: datetime.datetime | None | Unset = UNSET,
    end_date_gt: datetime.datetime | None | Unset = UNSET,
    end_date_lte: datetime.datetime | None | Unset = UNSET,
    end_date_lt: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    order_by: list[str] | Unset = UNSET,
    job_state: None | str | Unset = UNSET,
    job_type: None | str | Unset = UNSET,
    hostname: None | str | Unset = UNSET,
    executor_class: None | str | Unset = UNSET,
) -> HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse | None:
    """Get Jobs

     Get all jobs.

    Args:
        is_alive (bool | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        order_by (list[str] | Unset): Attributes to order by, multi criteria sort is supported.
            Prefix with `-` for descending order. Supported attributes: `id, dag_id, state, job_type,
            start_date, end_date, latest_heartbeat, executor_class, hostname, unixname`
        job_state (None | str | Unset):
        job_type (None | str | Unset):
        hostname (None | str | Unset):
        executor_class (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionResponse | HTTPValidationError | JobCollectionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            is_alive=is_alive,
            start_date_gte=start_date_gte,
            start_date_gt=start_date_gt,
            start_date_lte=start_date_lte,
            start_date_lt=start_date_lt,
            end_date_gte=end_date_gte,
            end_date_gt=end_date_gt,
            end_date_lte=end_date_lte,
            end_date_lt=end_date_lt,
            limit=limit,
            offset=offset,
            order_by=order_by,
            job_state=job_state,
            job_type=job_type,
            hostname=hostname,
            executor_class=executor_class,
        )
    ).parsed
