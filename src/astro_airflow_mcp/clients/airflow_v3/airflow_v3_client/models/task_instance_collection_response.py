from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.task_instance_response import TaskInstanceResponse


T = TypeVar("T", bound="TaskInstanceCollectionResponse")


@_attrs_define
class TaskInstanceCollectionResponse:
    """Task Instance Collection serializer for responses.

    Attributes:
        task_instances (list[TaskInstanceResponse]):
        total_entries (int):
    """

    task_instances: list[TaskInstanceResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_instances = []
        for task_instances_item_data in self.task_instances:
            task_instances_item = task_instances_item_data.to_dict()
            task_instances.append(task_instances_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_instances": task_instances,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_instance_response import TaskInstanceResponse

        d = dict(src_dict)
        task_instances = []
        _task_instances = d.pop("task_instances")
        for task_instances_item_data in _task_instances:
            task_instances_item = TaskInstanceResponse.from_dict(task_instances_item_data)

            task_instances.append(task_instances_item)

        total_entries = d.pop("total_entries")

        task_instance_collection_response = cls(
            task_instances=task_instances,
            total_entries=total_entries,
        )

        task_instance_collection_response.additional_properties = d
        return task_instance_collection_response

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
