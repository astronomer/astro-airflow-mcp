from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_task_state import UpdateTaskState
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTaskInstancesState")


@_attrs_define
class UpdateTaskInstancesState:
    """
    Attributes:
        dry_run (bool | Unset): If set, don't actually run this operation. The response will contain a list of task
            instances
            planned to be affected, but won't be modified in any way.
             Default: True.
        task_id (str | Unset): The task ID.
        execution_date (str | Unset): The execution date. Either set this or dag_run_id but not both.
        dag_run_id (str | Unset): The task instance's DAG run ID. Either set this or execution_date but not both.

            *New in version 2.3.0*
        include_upstream (bool | Unset): If set to true, upstream tasks are also affected.
        include_downstream (bool | Unset): If set to true, downstream tasks are also affected.
        include_future (bool | Unset): If set to True, also tasks from future DAG Runs are affected.
        include_past (bool | Unset): If set to True, also tasks from past DAG Runs are affected.
        new_state (UpdateTaskState | Unset): Expected new state. Only a subset of TaskState are available.

            Other states are managed directly by the scheduler or the workers and cannot be updated manually through the
            REST API.
    """

    dry_run: bool | Unset = True
    task_id: str | Unset = UNSET
    execution_date: str | Unset = UNSET
    dag_run_id: str | Unset = UNSET
    include_upstream: bool | Unset = UNSET
    include_downstream: bool | Unset = UNSET
    include_future: bool | Unset = UNSET
    include_past: bool | Unset = UNSET
    new_state: UpdateTaskState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        task_id = self.task_id

        execution_date = self.execution_date

        dag_run_id = self.dag_run_id

        include_upstream = self.include_upstream

        include_downstream = self.include_downstream

        include_future = self.include_future

        include_past = self.include_past

        new_state: str | Unset = UNSET
        if not isinstance(self.new_state, Unset):
            new_state = self.new_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if include_upstream is not UNSET:
            field_dict["include_upstream"] = include_upstream
        if include_downstream is not UNSET:
            field_dict["include_downstream"] = include_downstream
        if include_future is not UNSET:
            field_dict["include_future"] = include_future
        if include_past is not UNSET:
            field_dict["include_past"] = include_past
        if new_state is not UNSET:
            field_dict["new_state"] = new_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        task_id = d.pop("task_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        include_upstream = d.pop("include_upstream", UNSET)

        include_downstream = d.pop("include_downstream", UNSET)

        include_future = d.pop("include_future", UNSET)

        include_past = d.pop("include_past", UNSET)

        _new_state = d.pop("new_state", UNSET)
        new_state: UpdateTaskState | Unset
        if isinstance(_new_state, Unset):
            new_state = UNSET
        else:
            new_state = UpdateTaskState(_new_state)

        update_task_instances_state = cls(
            dry_run=dry_run,
            task_id=task_id,
            execution_date=execution_date,
            dag_run_id=dag_run_id,
            include_upstream=include_upstream,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            new_state=new_state,
        )

        update_task_instances_state.additional_properties = d
        return update_task_instances_state

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
