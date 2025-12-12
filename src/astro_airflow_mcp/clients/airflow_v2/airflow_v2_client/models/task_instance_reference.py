from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskInstanceReference")


@_attrs_define
class TaskInstanceReference:
    """
    Attributes:
        task_id (str | Unset): The task ID.
        dag_id (str | Unset): The DAG ID.
        execution_date (str | Unset):
        dag_run_id (str | Unset): The DAG run ID.
    """

    task_id: str | Unset = UNSET
    dag_id: str | Unset = UNSET
    execution_date: str | Unset = UNSET
    dag_run_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        dag_id = self.dag_id

        execution_date = self.execution_date

        dag_run_id = self.dag_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        dag_run_id = d.pop("dag_run_id", UNSET)

        task_instance_reference = cls(
            task_id=task_id,
            dag_id=dag_id,
            execution_date=execution_date,
            dag_run_id=dag_run_id,
        )

        task_instance_reference.additional_properties = d
        return task_instance_reference

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
