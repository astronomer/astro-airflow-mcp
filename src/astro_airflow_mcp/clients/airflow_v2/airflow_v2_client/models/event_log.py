from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventLog")


@_attrs_define
class EventLog:
    """Log of user operations via CLI or Web UI.

    Attributes:
        event_log_id (int | Unset): The event log ID
        when (datetime.datetime | Unset): The time when these events happened.
        dag_id (None | str | Unset): The DAG ID
        task_id (None | str | Unset): The Task ID
        run_id (None | str | Unset): The DAG Run ID
        event (str | Unset): A key describing the type of event.
        execution_date (datetime.datetime | None | Unset): When the event was dispatched for an object having
            execution_date, the value of this field.
        owner (str | Unset): Name of the user who triggered these events a.
        extra (None | str | Unset): Other information that was not included in the other fields, e.g. the complete CLI
            command.
    """

    event_log_id: int | Unset = UNSET
    when: datetime.datetime | Unset = UNSET
    dag_id: None | str | Unset = UNSET
    task_id: None | str | Unset = UNSET
    run_id: None | str | Unset = UNSET
    event: str | Unset = UNSET
    execution_date: datetime.datetime | None | Unset = UNSET
    owner: str | Unset = UNSET
    extra: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_log_id = self.event_log_id

        when: str | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        dag_id: None | str | Unset
        if isinstance(self.dag_id, Unset):
            dag_id = UNSET
        else:
            dag_id = self.dag_id

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        run_id: None | str | Unset
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        event = self.event

        execution_date: None | str | Unset
        if isinstance(self.execution_date, Unset):
            execution_date = UNSET
        elif isinstance(self.execution_date, datetime.datetime):
            execution_date = self.execution_date.isoformat()
        else:
            execution_date = self.execution_date

        owner = self.owner

        extra: None | str | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        else:
            extra = self.extra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_log_id is not UNSET:
            field_dict["event_log_id"] = event_log_id
        if when is not UNSET:
            field_dict["when"] = when
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if event is not UNSET:
            field_dict["event"] = event
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_log_id = d.pop("event_log_id", UNSET)

        _when = d.pop("when", UNSET)
        when: datetime.datetime | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        def _parse_dag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_id = _parse_dag_id(d.pop("dag_id", UNSET))

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        def _parse_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        event = d.pop("event", UNSET)

        def _parse_execution_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_date_type_0 = isoparse(data)

                return execution_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        execution_date = _parse_execution_date(d.pop("execution_date", UNSET))

        owner = d.pop("owner", UNSET)

        def _parse_extra(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        event_log = cls(
            event_log_id=event_log_id,
            when=when,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            event=event,
            execution_date=execution_date,
            owner=owner,
            extra=extra,
        )

        event_log.additional_properties = d
        return event_log

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
