from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XCom")


@_attrs_define
class XCom:
    """Full representations of XCom entry.

    Attributes:
        key (str | Unset):
        timestamp (str | Unset):
        execution_date (str | Unset):
        map_index (int | Unset):
        task_id (str | Unset):
        dag_id (str | Unset):
        value (str | Unset): The value
    """

    key: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    execution_date: str | Unset = UNSET
    map_index: int | Unset = UNSET
    task_id: str | Unset = UNSET
    dag_id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        timestamp = self.timestamp

        execution_date = self.execution_date

        map_index = self.map_index

        task_id = self.task_id

        dag_id = self.dag_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if map_index is not UNSET:
            field_dict["map_index"] = map_index
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        execution_date = d.pop("execution_date", UNSET)

        map_index = d.pop("map_index", UNSET)

        task_id = d.pop("task_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        value = d.pop("value", UNSET)

        x_com = cls(
            key=key,
            timestamp=timestamp,
            execution_date=execution_date,
            map_index=map_index,
            task_id=task_id,
            dag_id=dag_id,
            value=value,
        )

        x_com.additional_properties = d
        return x_com

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
