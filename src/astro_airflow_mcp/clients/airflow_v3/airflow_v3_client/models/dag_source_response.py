from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DAGSourceResponse")


@_attrs_define
class DAGSourceResponse:
    """DAG Source serializer for responses.

    Attributes:
        content (None | str):
        dag_id (str):
        version_number (int | None):
        dag_display_name (str):
    """

    content: None | str
    dag_id: str
    version_number: int | None
    dag_display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str
        content = self.content

        dag_id = self.dag_id

        version_number: int | None
        version_number = self.version_number

        dag_display_name = self.dag_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "dag_id": dag_id,
                "version_number": version_number,
                "dag_display_name": dag_display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        dag_id = d.pop("dag_id")

        def _parse_version_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        version_number = _parse_version_number(d.pop("version_number"))

        dag_display_name = d.pop("dag_display_name")

        dag_source_response = cls(
            content=content,
            dag_id=dag_id,
            version_number=version_number,
            dag_display_name=dag_display_name,
        )

        dag_source_response.additional_properties = d
        return dag_source_response

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
