from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provider_response import ProviderResponse


T = TypeVar("T", bound="ProviderCollectionResponse")


@_attrs_define
class ProviderCollectionResponse:
    """Provider Collection serializer for responses.

    Attributes:
        providers (list[ProviderResponse]):
        total_entries (int):
    """

    providers: list[ProviderResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_response import ProviderResponse

        d = dict(src_dict)
        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = ProviderResponse.from_dict(providers_item_data)

            providers.append(providers_item)

        total_entries = d.pop("total_entries")

        provider_collection_response = cls(
            providers=providers,
            total_entries=total_entries,
        )

        provider_collection_response.additional_properties = d
        return provider_collection_response

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
