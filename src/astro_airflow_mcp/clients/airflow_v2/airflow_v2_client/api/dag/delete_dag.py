from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    dag_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/dags/{dag_id}".format(
            dag_id=quote(str(dag_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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
) -> Response[Any | Error]:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Error]:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Error | None:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
        )
    ).parsed
