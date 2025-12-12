from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_collection_item import PluginCollectionItem


T = TypeVar("T", bound="PluginCollection")


@_attrs_define
class PluginCollection:
    """A collection of plugin.

    *New in version 2.1.0*

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            plugins (list[PluginCollectionItem] | Unset):
    """

    total_entries: int | Unset = UNSET
    plugins: list[PluginCollectionItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        plugins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = []
            for plugins_item_data in self.plugins:
                plugins_item = plugins_item_data.to_dict()
                plugins.append(plugins_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if plugins is not UNSET:
            field_dict["plugins"] = plugins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_collection_item import PluginCollectionItem

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _plugins = d.pop("plugins", UNSET)
        plugins: list[PluginCollectionItem] | Unset = UNSET
        if _plugins is not UNSET:
            plugins = []
            for plugins_item_data in _plugins:
                plugins_item = PluginCollectionItem.from_dict(plugins_item_data)

                plugins.append(plugins_item)

        plugin_collection = cls(
            total_entries=total_entries,
            plugins=plugins,
        )

        plugin_collection.additional_properties = d
        return plugin_collection

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
