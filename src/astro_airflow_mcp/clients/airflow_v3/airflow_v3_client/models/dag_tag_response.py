from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DagTagResponse")


@_attrs_define
class DagTagResponse:
    """DAG Tag serializer for responses.

    Attributes:
        name (str):
        dag_id (str):
        dag_display_name (str):
    """

    name: str
    dag_id: str
    dag_display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dag_id": dag_id,
                "dag_display_name": dag_display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        dag_id = d.pop("dag_id")

        dag_display_name = d.pop("dag_display_name")

        dag_tag_response = cls(
            name=name,
            dag_id=dag_id,
            dag_display_name=dag_display_name,
        )

        dag_tag_response.additional_properties = d
        return dag_tag_response

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
