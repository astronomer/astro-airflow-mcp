from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_log_response import EventLogResponse


T = TypeVar("T", bound="EventLogCollectionResponse")


@_attrs_define
class EventLogCollectionResponse:
    """Event Log Collection Response.

    Attributes:
        event_logs (list[EventLogResponse]):
        total_entries (int):
    """

    event_logs: list[EventLogResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_logs = []
        for event_logs_item_data in self.event_logs:
            event_logs_item = event_logs_item_data.to_dict()
            event_logs.append(event_logs_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_logs": event_logs,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_log_response import EventLogResponse

        d = dict(src_dict)
        event_logs = []
        _event_logs = d.pop("event_logs")
        for event_logs_item_data in _event_logs:
            event_logs_item = EventLogResponse.from_dict(event_logs_item_data)

            event_logs.append(event_logs_item)

        total_entries = d.pop("total_entries")

        event_log_collection_response = cls(
            event_logs=event_logs,
            total_entries=total_entries,
        )

        event_log_collection_response.additional_properties = d
        return event_log_collection_response

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
