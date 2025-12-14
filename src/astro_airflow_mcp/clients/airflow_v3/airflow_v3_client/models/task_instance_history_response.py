from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_instance_state import TaskInstanceState

if TYPE_CHECKING:
    from ..models.dag_version_response import DagVersionResponse


T = TypeVar("T", bound="TaskInstanceHistoryResponse")


@_attrs_define
class TaskInstanceHistoryResponse:
    """TaskInstanceHistory serializer for responses.

    Attributes:
        task_id (str):
        dag_id (str):
        dag_run_id (str):
        map_index (int):
        start_date (datetime.datetime | None):
        end_date (datetime.datetime | None):
        duration (float | None):
        state (None | TaskInstanceState):
        try_number (int):
        max_tries (int):
        task_display_name (str):
        dag_display_name (str):
        hostname (None | str):
        unixname (None | str):
        pool (str):
        pool_slots (int):
        queue (None | str):
        priority_weight (int | None):
        operator (None | str):
        operator_name (None | str):
        queued_when (datetime.datetime | None):
        scheduled_when (datetime.datetime | None):
        pid (int | None):
        executor (None | str):
        executor_config (str):
        dag_version (DagVersionResponse | None):
    """

    task_id: str
    dag_id: str
    dag_run_id: str
    map_index: int
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    duration: float | None
    state: None | TaskInstanceState
    try_number: int
    max_tries: int
    task_display_name: str
    dag_display_name: str
    hostname: None | str
    unixname: None | str
    pool: str
    pool_slots: int
    queue: None | str
    priority_weight: int | None
    operator: None | str
    operator_name: None | str
    queued_when: datetime.datetime | None
    scheduled_when: datetime.datetime | None
    pid: int | None
    executor: None | str
    executor_config: str
    dag_version: DagVersionResponse | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dag_version_response import DagVersionResponse

        task_id = self.task_id

        dag_id = self.dag_id

        dag_run_id = self.dag_run_id

        map_index = self.map_index

        start_date: None | str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        duration: float | None
        duration = self.duration

        state: None | str
        if isinstance(self.state, TaskInstanceState):
            state = self.state.value
        else:
            state = self.state

        try_number = self.try_number

        max_tries = self.max_tries

        task_display_name = self.task_display_name

        dag_display_name = self.dag_display_name

        hostname: None | str
        hostname = self.hostname

        unixname: None | str
        unixname = self.unixname

        pool = self.pool

        pool_slots = self.pool_slots

        queue: None | str
        queue = self.queue

        priority_weight: int | None
        priority_weight = self.priority_weight

        operator: None | str
        operator = self.operator

        operator_name: None | str
        operator_name = self.operator_name

        queued_when: None | str
        if isinstance(self.queued_when, datetime.datetime):
            queued_when = self.queued_when.isoformat()
        else:
            queued_when = self.queued_when

        scheduled_when: None | str
        if isinstance(self.scheduled_when, datetime.datetime):
            scheduled_when = self.scheduled_when.isoformat()
        else:
            scheduled_when = self.scheduled_when

        pid: int | None
        pid = self.pid

        executor: None | str
        executor = self.executor

        executor_config = self.executor_config

        dag_version: dict[str, Any] | None
        if isinstance(self.dag_version, DagVersionResponse):
            dag_version = self.dag_version.to_dict()
        else:
            dag_version = self.dag_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "dag_id": dag_id,
                "dag_run_id": dag_run_id,
                "map_index": map_index,
                "start_date": start_date,
                "end_date": end_date,
                "duration": duration,
                "state": state,
                "try_number": try_number,
                "max_tries": max_tries,
                "task_display_name": task_display_name,
                "dag_display_name": dag_display_name,
                "hostname": hostname,
                "unixname": unixname,
                "pool": pool,
                "pool_slots": pool_slots,
                "queue": queue,
                "priority_weight": priority_weight,
                "operator": operator,
                "operator_name": operator_name,
                "queued_when": queued_when,
                "scheduled_when": scheduled_when,
                "pid": pid,
                "executor": executor,
                "executor_config": executor_config,
                "dag_version": dag_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_version_response import DagVersionResponse

        d = dict(src_dict)
        task_id = d.pop("task_id")

        dag_id = d.pop("dag_id")

        dag_run_id = d.pop("dag_run_id")

        map_index = d.pop("map_index")

        def _parse_start_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_end_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_date = _parse_end_date(d.pop("end_date"))

        def _parse_duration(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration = _parse_duration(d.pop("duration"))

        def _parse_state(data: object) -> None | TaskInstanceState:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = TaskInstanceState(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskInstanceState, data)

        state = _parse_state(d.pop("state"))

        try_number = d.pop("try_number")

        max_tries = d.pop("max_tries")

        task_display_name = d.pop("task_display_name")

        dag_display_name = d.pop("dag_display_name")

        def _parse_hostname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hostname = _parse_hostname(d.pop("hostname"))

        def _parse_unixname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unixname = _parse_unixname(d.pop("unixname"))

        pool = d.pop("pool")

        pool_slots = d.pop("pool_slots")

        def _parse_queue(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        queue = _parse_queue(d.pop("queue"))

        def _parse_priority_weight(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority_weight = _parse_priority_weight(d.pop("priority_weight"))

        def _parse_operator(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operator = _parse_operator(d.pop("operator"))

        def _parse_operator_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operator_name = _parse_operator_name(d.pop("operator_name"))

        def _parse_queued_when(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queued_when_type_0 = isoparse(data)

                return queued_when_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        queued_when = _parse_queued_when(d.pop("queued_when"))

        def _parse_scheduled_when(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_when_type_0 = isoparse(data)

                return scheduled_when_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scheduled_when = _parse_scheduled_when(d.pop("scheduled_when"))

        def _parse_pid(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        pid = _parse_pid(d.pop("pid"))

        def _parse_executor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        executor = _parse_executor(d.pop("executor"))

        executor_config = d.pop("executor_config")

        def _parse_dag_version(data: object) -> DagVersionResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dag_version_type_0 = DagVersionResponse.from_dict(data)

                return dag_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DagVersionResponse | None, data)

        dag_version = _parse_dag_version(d.pop("dag_version"))

        task_instance_history_response = cls(
            task_id=task_id,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            map_index=map_index,
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            state=state,
            try_number=try_number,
            max_tries=max_tries,
            task_display_name=task_display_name,
            dag_display_name=dag_display_name,
            hostname=hostname,
            unixname=unixname,
            pool=pool,
            pool_slots=pool_slots,
            queue=queue,
            priority_weight=priority_weight,
            operator=operator,
            operator_name=operator_name,
            queued_when=queued_when,
            scheduled_when=scheduled_when,
            pid=pid,
            executor=executor,
            executor_config=executor_config,
            dag_version=dag_version,
        )

        task_instance_history_response.additional_properties = d
        return task_instance_history_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
