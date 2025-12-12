from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider import Provider


T = TypeVar("T", bound="GetProvidersResponse200")


@_attrs_define
class GetProvidersResponse200:
    """
    Attributes:
        providers (list[Provider] | Unset):
        total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
            (limit, offset) are applied.
    """

    providers: list[Provider] | Unset = UNSET
    total_entries: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = []
            for providers_item_data in self.providers:
                providers_item = providers_item_data.to_dict()
                providers.append(providers_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if providers is not UNSET:
            field_dict["providers"] = providers
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider import Provider

        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: list[Provider] | Unset = UNSET
        if _providers is not UNSET:
            providers = []
            for providers_item_data in _providers:
                providers_item = Provider.from_dict(providers_item_data)

                providers.append(providers_item)

        total_entries = d.pop("total_entries", UNSET)

        get_providers_response_200 = cls(
            providers=providers,
            total_entries=total_entries,
        )

        get_providers_response_200.additional_properties = d
        return get_providers_response_200

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
