from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ImportErrorResponse")


@_attrs_define
class ImportErrorResponse:
    """Import Error Response.

    Attributes:
        import_error_id (int):
        timestamp (datetime.datetime):
        filename (str):
        bundle_name (None | str):
        stack_trace (str):
    """

    import_error_id: int
    timestamp: datetime.datetime
    filename: str
    bundle_name: None | str
    stack_trace: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_error_id = self.import_error_id

        timestamp = self.timestamp.isoformat()

        filename = self.filename

        bundle_name: None | str
        bundle_name = self.bundle_name

        stack_trace = self.stack_trace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_error_id": import_error_id,
                "timestamp": timestamp,
                "filename": filename,
                "bundle_name": bundle_name,
                "stack_trace": stack_trace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        import_error_id = d.pop("import_error_id")

        timestamp = isoparse(d.pop("timestamp"))

        filename = d.pop("filename")

        def _parse_bundle_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_name = _parse_bundle_name(d.pop("bundle_name"))

        stack_trace = d.pop("stack_trace")

        import_error_response = cls(
            import_error_id=import_error_id,
            timestamp=timestamp,
            filename=filename,
            bundle_name=bundle_name,
            stack_trace=stack_trace,
        )

        import_error_response.additional_properties = d
        return import_error_response

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
