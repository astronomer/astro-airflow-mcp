from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportError_")


@_attrs_define
class ImportError_:
    """
    Attributes:
        import_error_id (int | Unset): The import error ID.
        timestamp (str | Unset): The time when this error was created.
        filename (str | Unset): The filename
        stack_trace (str | Unset): The full stackstrace..
    """

    import_error_id: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    filename: str | Unset = UNSET
    stack_trace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_error_id = self.import_error_id

        timestamp = self.timestamp

        filename = self.filename

        stack_trace = self.stack_trace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_error_id is not UNSET:
            field_dict["import_error_id"] = import_error_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if filename is not UNSET:
            field_dict["filename"] = filename
        if stack_trace is not UNSET:
            field_dict["stack_trace"] = stack_trace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        import_error_id = d.pop("import_error_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        filename = d.pop("filename", UNSET)

        stack_trace = d.pop("stack_trace", UNSET)

        import_error = cls(
            import_error_id=import_error_id,
            timestamp=timestamp,
            filename=filename,
            stack_trace=stack_trace,
        )

        import_error.additional_properties = d
        return import_error

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
