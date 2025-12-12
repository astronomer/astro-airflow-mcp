from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_alias_response import AssetAliasResponse


T = TypeVar("T", bound="AssetAliasCollectionResponse")


@_attrs_define
class AssetAliasCollectionResponse:
    """Asset alias collection response.

    Attributes:
        asset_aliases (list[AssetAliasResponse]):
        total_entries (int):
    """

    asset_aliases: list[AssetAliasResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_aliases = []
        for asset_aliases_item_data in self.asset_aliases:
            asset_aliases_item = asset_aliases_item_data.to_dict()
            asset_aliases.append(asset_aliases_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_aliases": asset_aliases,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_alias_response import AssetAliasResponse

        d = dict(src_dict)
        asset_aliases = []
        _asset_aliases = d.pop("asset_aliases")
        for asset_aliases_item_data in _asset_aliases:
            asset_aliases_item = AssetAliasResponse.from_dict(asset_aliases_item_data)

            asset_aliases.append(asset_aliases_item)

        total_entries = d.pop("total_entries")

        asset_alias_collection_response = cls(
            asset_aliases=asset_aliases,
            total_entries=total_entries,
        )

        asset_alias_collection_response.additional_properties = d
        return asset_alias_collection_response

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
