from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queued_event_response import QueuedEventResponse


T = TypeVar("T", bound="QueuedEventCollectionResponse")


@_attrs_define
class QueuedEventCollectionResponse:
    """Queued Event Collection serializer for responses.

    Attributes:
        queued_events (list[QueuedEventResponse]):
        total_entries (int):
    """

    queued_events: list[QueuedEventResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queued_events = []
        for queued_events_item_data in self.queued_events:
            queued_events_item = queued_events_item_data.to_dict()
            queued_events.append(queued_events_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queued_events": queued_events,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queued_event_response import QueuedEventResponse

        d = dict(src_dict)
        queued_events = []
        _queued_events = d.pop("queued_events")
        for queued_events_item_data in _queued_events:
            queued_events_item = QueuedEventResponse.from_dict(queued_events_item_data)

            queued_events.append(queued_events_item)

        total_entries = d.pop("total_entries")

        queued_event_collection_response = cls(
            queued_events=queued_events,
            total_entries=total_entries,
        )

        queued_event_collection_response.additional_properties = d
        return queued_event_collection_response

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
