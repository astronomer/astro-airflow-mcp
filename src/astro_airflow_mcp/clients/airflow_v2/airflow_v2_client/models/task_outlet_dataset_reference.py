from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskOutletDatasetReference")


@_attrs_define
class TaskOutletDatasetReference:
    """A datasets reference to an upstream task.

    *New in version 2.4.0*

        Attributes:
            dag_id (None | str | Unset): The DAG ID that updates the dataset.
            task_id (None | str | Unset): The task ID that updates the dataset.
            created_at (str | Unset): The dataset creation time
            updated_at (str | Unset): The dataset update time
    """

    dag_id: None | str | Unset = UNSET
    task_id: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_id: None | str | Unset
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        task_outlet_dataset_reference = cls(
            dag_id=dag_id,
            task_id=task_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        task_outlet_dataset_reference.additional_properties = d
        return task_outlet_dataset_reference

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
