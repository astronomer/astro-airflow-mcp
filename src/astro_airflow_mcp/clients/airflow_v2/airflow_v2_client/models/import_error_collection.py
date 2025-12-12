from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_error import ImportError_


T = TypeVar("T", bound="ImportErrorCollection")


@_attrs_define
class ImportErrorCollection:
    """Collection of import errors.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            import_errors (list[ImportError_] | Unset):
    """

    total_entries: int | Unset = UNSET
    import_errors: list[ImportError_] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        import_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.import_errors, Unset):
            import_errors = []
            for import_errors_item_data in self.import_errors:
                import_errors_item = import_errors_item_data.to_dict()
                import_errors.append(import_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if import_errors is not UNSET:
            field_dict["import_errors"] = import_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_error import ImportError_

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _import_errors = d.pop("import_errors", UNSET)
        import_errors: list[ImportError_] | Unset = UNSET
        if _import_errors is not UNSET:
            import_errors = []
            for import_errors_item_data in _import_errors:
                import_errors_item = ImportError_.from_dict(import_errors_item_data)

                import_errors.append(import_errors_item)

        import_error_collection = cls(
            total_entries=total_entries,
            import_errors=import_errors,
        )

        import_error_collection.additional_properties = d
        return import_error_collection

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
