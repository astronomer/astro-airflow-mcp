from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.task_dependency_response import TaskDependencyResponse


T = TypeVar("T", bound="TaskDependencyCollectionResponse")


@_attrs_define
class TaskDependencyCollectionResponse:
    """Task scheduling dependencies collection serializer for responses.

    Attributes:
        dependencies (list[TaskDependencyResponse]):
    """

    dependencies: list[TaskDependencyResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dependencies = []
        for dependencies_item_data in self.dependencies:
            dependencies_item = dependencies_item_data.to_dict()
            dependencies.append(dependencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dependencies": dependencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_dependency_response import TaskDependencyResponse

        d = dict(src_dict)
        dependencies = []
        _dependencies = d.pop("dependencies")
        for dependencies_item_data in _dependencies:
            dependencies_item = TaskDependencyResponse.from_dict(dependencies_item_data)

            dependencies.append(dependencies_item)

        task_dependency_collection_response = cls(
            dependencies=dependencies,
        )

        task_dependency_collection_response.additional_properties = d
        return task_dependency_collection_response

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
