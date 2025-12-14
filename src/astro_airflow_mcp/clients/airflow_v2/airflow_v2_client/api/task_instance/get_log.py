from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_log_response_200 import GetLogResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    task_try_number: int,
    *,
    full_content: bool | Unset = UNSET,
    map_index: int | Unset = UNSET,
    token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["full_content"] = full_content

    params["map_index"] = map_index

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number}".format(
            dag_id=quote(str(dag_id), safe=""),
            dag_run_id=quote(str(dag_run_id), safe=""),
            task_id=quote(str(task_id), safe=""),
            task_try_number=quote(str(task_try_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GetLogResponse200 | None:
    if response.status_code == 200:
        response_200 = GetLogResponse200.from_dict(response.json())

        return response_200

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GetLogResponse200]:
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
    task_try_number: int,
    *,
    client: AuthenticatedClient | Client,
    full_content: bool | Unset = UNSET,
    map_index: int | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[Error | GetLogResponse200]:
    r"""Get logs

     Get logs for a specific task instance and its try number.
    To get log from specific character position, following way of using
    URLSafeSerializer can be used.

    Example:
    ```
    from itsdangerous.url_safe import URLSafeSerializer

    request_url = f\"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/1\"
    key = app.config[\"SECRET_KEY\"]
    serializer = URLSafeSerializer(key)
    token = serializer.dumps({\"log_pos\": 10000})

    response = self.client.get(
        request_url,
        query_string={\"token\": token},
        headers={\"Accept\": \"text/plain\"},
        environ_overrides={\"REMOTE_USER\": \"test\"},
    )
    continuation_token = response.json[\"continuation_token\"]
        metadata = URLSafeSerializer(key).loads(continuation_token)
        log_pos = metadata[\"log_pos\"]
        end_of_log = metadata[\"end_of_log\"]
    ```
    If log_pos is passed as 10000 like the above example, it renders the logs starting
    from char position 10000 to last (not the end as the logs may be tailing behind in
    running state). This way pagination can be done with metadata as part of the token.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        task_try_number (int):
        full_content (bool | Unset):
        map_index (int | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetLogResponse200]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        task_try_number=task_try_number,
        full_content=full_content,
        map_index=map_index,
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    task_try_number: int,
    *,
    client: AuthenticatedClient | Client,
    full_content: bool | Unset = UNSET,
    map_index: int | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Error | GetLogResponse200 | None:
    r"""Get logs

     Get logs for a specific task instance and its try number.
    To get log from specific character position, following way of using
    URLSafeSerializer can be used.

    Example:
    ```
    from itsdangerous.url_safe import URLSafeSerializer

    request_url = f\"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/1\"
    key = app.config[\"SECRET_KEY\"]
    serializer = URLSafeSerializer(key)
    token = serializer.dumps({\"log_pos\": 10000})

    response = self.client.get(
        request_url,
        query_string={\"token\": token},
        headers={\"Accept\": \"text/plain\"},
        environ_overrides={\"REMOTE_USER\": \"test\"},
    )
    continuation_token = response.json[\"continuation_token\"]
        metadata = URLSafeSerializer(key).loads(continuation_token)
        log_pos = metadata[\"log_pos\"]
        end_of_log = metadata[\"end_of_log\"]
    ```
    If log_pos is passed as 10000 like the above example, it renders the logs starting
    from char position 10000 to last (not the end as the logs may be tailing behind in
    running state). This way pagination can be done with metadata as part of the token.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        task_try_number (int):
        full_content (bool | Unset):
        map_index (int | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetLogResponse200
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        task_try_number=task_try_number,
        client=client,
        full_content=full_content,
        map_index=map_index,
        token=token,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    task_try_number: int,
    *,
    client: AuthenticatedClient | Client,
    full_content: bool | Unset = UNSET,
    map_index: int | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Response[Error | GetLogResponse200]:
    r"""Get logs

     Get logs for a specific task instance and its try number.
    To get log from specific character position, following way of using
    URLSafeSerializer can be used.

    Example:
    ```
    from itsdangerous.url_safe import URLSafeSerializer

    request_url = f\"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/1\"
    key = app.config[\"SECRET_KEY\"]
    serializer = URLSafeSerializer(key)
    token = serializer.dumps({\"log_pos\": 10000})

    response = self.client.get(
        request_url,
        query_string={\"token\": token},
        headers={\"Accept\": \"text/plain\"},
        environ_overrides={\"REMOTE_USER\": \"test\"},
    )
    continuation_token = response.json[\"continuation_token\"]
        metadata = URLSafeSerializer(key).loads(continuation_token)
        log_pos = metadata[\"log_pos\"]
        end_of_log = metadata[\"end_of_log\"]
    ```
    If log_pos is passed as 10000 like the above example, it renders the logs starting
    from char position 10000 to last (not the end as the logs may be tailing behind in
    running state). This way pagination can be done with metadata as part of the token.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        task_try_number (int):
        full_content (bool | Unset):
        map_index (int | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetLogResponse200]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        task_try_number=task_try_number,
        full_content=full_content,
        map_index=map_index,
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    task_try_number: int,
    *,
    client: AuthenticatedClient | Client,
    full_content: bool | Unset = UNSET,
    map_index: int | Unset = UNSET,
    token: str | Unset = UNSET,
) -> Error | GetLogResponse200 | None:
    r"""Get logs

     Get logs for a specific task instance and its try number.
    To get log from specific character position, following way of using
    URLSafeSerializer can be used.

    Example:
    ```
    from itsdangerous.url_safe import URLSafeSerializer

    request_url = f\"api/v1/dags/{DAG_ID}/dagRuns/{RUN_ID}/taskInstances/{TASK_ID}/logs/1\"
    key = app.config[\"SECRET_KEY\"]
    serializer = URLSafeSerializer(key)
    token = serializer.dumps({\"log_pos\": 10000})

    response = self.client.get(
        request_url,
        query_string={\"token\": token},
        headers={\"Accept\": \"text/plain\"},
        environ_overrides={\"REMOTE_USER\": \"test\"},
    )
    continuation_token = response.json[\"continuation_token\"]
        metadata = URLSafeSerializer(key).loads(continuation_token)
        log_pos = metadata[\"log_pos\"]
        end_of_log = metadata[\"end_of_log\"]
    ```
    If log_pos is passed as 10000 like the above example, it renders the logs starting
    from char position 10000 to last (not the end as the logs may be tailing behind in
    running state). This way pagination can be done with metadata as part of the token.

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        task_try_number (int):
        full_content (bool | Unset):
        map_index (int | Unset):
        token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetLogResponse200
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            task_try_number=task_try_number,
            client=client,
            full_content=full_content,
            map_index=map_index,
            token=token,
        )
    ).parsed
