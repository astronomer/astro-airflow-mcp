from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Provider")


@_attrs_define
class Provider:
    """The provider

    *New in version 2.1.0*

        Attributes:
            package_name (str | Unset): The package name of the provider.
            description (str | Unset): The description of the provider.
            version (str | Unset): The version of the provider.
    """

    package_name: str | Unset = UNSET
    description: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        description = self.description

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_name = d.pop("package_name", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        provider = cls(
            package_name=package_name,
            description=description,
            version=version,
        )

        provider.additional_properties = d
        return provider

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
