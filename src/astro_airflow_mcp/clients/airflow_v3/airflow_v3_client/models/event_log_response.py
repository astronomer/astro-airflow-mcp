from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventLogResponse")


@_attrs_define
class EventLogResponse:
    """Event Log Response.

    Attributes:
        event_log_id (int):
        when (datetime.datetime):
        dag_id (None | str):
        task_id (None | str):
        run_id (None | str):
        map_index (int | None):
        try_number (int | None):
        event (str):
        logical_date (datetime.datetime | None):
        owner (None | str):
        extra (None | str):
        dag_display_name (None | str | Unset):
        task_display_name (None | str | Unset):
    """

    event_log_id: int
    when: datetime.datetime
    dag_id: None | str
    task_id: None | str
    run_id: None | str
    map_index: int | None
    try_number: int | None
    event: str
    logical_date: datetime.datetime | None
    owner: None | str
    extra: None | str
    dag_display_name: None | str | Unset = UNSET
    task_display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_log_id = self.event_log_id

        when = self.when.isoformat()

        dag_id: None | str
        dag_id = self.dag_id

        task_id: None | str
        task_id = self.task_id

        run_id: None | str
        run_id = self.run_id

        map_index: int | None
        map_index = self.map_index

        try_number: int | None
        try_number = self.try_number

        event = self.event

        logical_date: None | str
        if isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        owner: None | str
        owner = self.owner

        extra: None | str
        extra = self.extra

        dag_display_name: None | str | Unset
        if isinstance(self.dag_display_name, Unset):
            dag_display_name = UNSET
        else:
            dag_display_name = self.dag_display_name

        task_display_name: None | str | Unset
        if isinstance(self.task_display_name, Unset):
            task_display_name = UNSET
        else:
            task_display_name = self.task_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_log_id": event_log_id,
                "when": when,
                "dag_id": dag_id,
                "task_id": task_id,
                "run_id": run_id,
                "map_index": map_index,
                "try_number": try_number,
                "event": event,
                "logical_date": logical_date,
                "owner": owner,
                "extra": extra,
            }
        )
        if dag_display_name is not UNSET:
            field_dict["dag_display_name"] = dag_display_name
        if task_display_name is not UNSET:
            field_dict["task_display_name"] = task_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_log_id = d.pop("event_log_id")

        when = isoparse(d.pop("when"))

        def _parse_dag_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dag_id = _parse_dag_id(d.pop("dag_id"))

        def _parse_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_id = _parse_task_id(d.pop("task_id"))

        def _parse_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        run_id = _parse_run_id(d.pop("run_id"))

        def _parse_map_index(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        map_index = _parse_map_index(d.pop("map_index"))

        def _parse_try_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        try_number = _parse_try_number(d.pop("try_number"))

        event = d.pop("event")

        def _parse_logical_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_type_0 = isoparse(data)

                return logical_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        logical_date = _parse_logical_date(d.pop("logical_date"))

        def _parse_owner(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        owner = _parse_owner(d.pop("owner"))

        def _parse_extra(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        extra = _parse_extra(d.pop("extra"))

        def _parse_dag_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_display_name = _parse_dag_display_name(d.pop("dag_display_name", UNSET))

        def _parse_task_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_display_name = _parse_task_display_name(d.pop("task_display_name", UNSET))

        event_log_response = cls(
            event_log_id=event_log_id,
            when=when,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            event=event,
            logical_date=logical_date,
            owner=owner,
            extra=extra,
            dag_display_name=dag_display_name,
            task_display_name=task_display_name,
        )

        event_log_response.additional_properties = d
        return event_log_response

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
