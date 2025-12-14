from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassReference")


@_attrs_define
class ClassReference:
    """Class reference

    Attributes:
        module_path (str | Unset):
        class_name (str | Unset):
    """

    module_path: str | Unset = UNSET
    class_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        module_path = self.module_path

        class_name = self.class_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if module_path is not UNSET:
            field_dict["module_path"] = module_path
        if class_name is not UNSET:
            field_dict["class_name"] = class_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        module_path = d.pop("module_path", UNSET)

        class_name = d.pop("class_name", UNSET)

        class_reference = cls(
            module_path=module_path,
            class_name=class_name,
        )

        class_reference.additional_properties = d
        return class_reference

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
