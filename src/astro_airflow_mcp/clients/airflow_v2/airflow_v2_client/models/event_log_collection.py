from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_log import EventLog


T = TypeVar("T", bound="EventLogCollection")


@_attrs_define
class EventLogCollection:
    """Collection of event logs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            event_logs (list[EventLog] | Unset):
    """

    total_entries: int | Unset = UNSET
    event_logs: list[EventLog] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        event_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.event_logs, Unset):
            event_logs = []
            for event_logs_item_data in self.event_logs:
                event_logs_item = event_logs_item_data.to_dict()
                event_logs.append(event_logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if event_logs is not UNSET:
            field_dict["event_logs"] = event_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_log import EventLog

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _event_logs = d.pop("event_logs", UNSET)
        event_logs: list[EventLog] | Unset = UNSET
        if _event_logs is not UNSET:
            event_logs = []
            for event_logs_item_data in _event_logs:
                event_logs_item = EventLog.from_dict(event_logs_item_data)

                event_logs.append(event_logs_item)

        event_log_collection = cls(
            total_entries=total_entries,
            event_logs=event_logs,
        )

        event_log_collection.additional_properties = d
        return event_log_collection

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
