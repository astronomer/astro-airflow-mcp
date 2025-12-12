from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_import_error_response import PluginImportErrorResponse


T = TypeVar("T", bound="PluginImportErrorCollectionResponse")


@_attrs_define
class PluginImportErrorCollectionResponse:
    """Plugin Import Error Collection serializer.

    Attributes:
        import_errors (list[PluginImportErrorResponse]):
        total_entries (int):
    """

    import_errors: list[PluginImportErrorResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_errors = []
        for import_errors_item_data in self.import_errors:
            import_errors_item = import_errors_item_data.to_dict()
            import_errors.append(import_errors_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_errors": import_errors,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_import_error_response import PluginImportErrorResponse

        d = dict(src_dict)
        import_errors = []
        _import_errors = d.pop("import_errors")
        for import_errors_item_data in _import_errors:
            import_errors_item = PluginImportErrorResponse.from_dict(import_errors_item_data)

            import_errors.append(import_errors_item)

        total_entries = d.pop("total_entries")

        plugin_import_error_collection_response = cls(
            import_errors=import_errors,
            total_entries=total_entries,
        )

        plugin_import_error_collection_response.additional_properties = d
        return plugin_import_error_collection_response

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
