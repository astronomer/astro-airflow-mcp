from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.variable_response import VariableResponse


T = TypeVar("T", bound="VariableCollectionResponse")


@_attrs_define
class VariableCollectionResponse:
    """Variable Collection serializer for responses.

    Attributes:
        variables (list[VariableResponse]):
        total_entries (int):
    """

    variables: list[VariableResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variables": variables,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable_response import VariableResponse

        d = dict(src_dict)
        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = VariableResponse.from_dict(variables_item_data)

            variables.append(variables_item)

        total_entries = d.pop("total_entries")

        variable_collection_response = cls(
            variables=variables,
            total_entries=total_entries,
        )

        variable_collection_response.additional_properties = d
        return variable_collection_response

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
