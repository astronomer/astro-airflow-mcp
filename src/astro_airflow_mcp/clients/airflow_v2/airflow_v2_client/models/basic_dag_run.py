from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dag_state import DagState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicDAGRun")


@_attrs_define
class BasicDAGRun:
    """
    Attributes:
        run_id (str | Unset): Run ID.
        dag_id (str | Unset):
        logical_date (datetime.datetime | Unset): The logical date (previously called execution date). This is the time
            or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*
        start_date (datetime.datetime | None | Unset): The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.
        end_date (datetime.datetime | None | Unset):
        data_interval_start (datetime.datetime | None | Unset):
        data_interval_end (datetime.datetime | None | Unset):
        state (DagState | Unset): DAG State.

            *Changed in version 2.1.3*&#58; 'queued' is added as a possible value.
    """

    run_id: str | Unset = UNSET
    dag_id: str | Unset = UNSET
    logical_date: datetime.datetime | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    data_interval_start: datetime.datetime | None | Unset = UNSET
    data_interval_end: datetime.datetime | None | Unset = UNSET
    state: DagState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        dag_id = self.dag_id

        logical_date: str | Unset = UNSET
        if not isinstance(self.logical_date, Unset):
            logical_date = self.logical_date.isoformat()

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        data_interval_start: None | str | Unset
        if isinstance(self.data_interval_start, Unset):
            data_interval_start = UNSET
        elif isinstance(self.data_interval_start, datetime.datetime):
            data_interval_start = self.data_interval_start.isoformat()
        else:
            data_interval_start = self.data_interval_start

        data_interval_end: None | str | Unset
        if isinstance(self.data_interval_end, Unset):
            data_interval_end = UNSET
        elif isinstance(self.data_interval_end, datetime.datetime):
            data_interval_end = self.data_interval_end.isoformat()
        else:
            data_interval_end = self.data_interval_end

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if logical_date is not UNSET:
            field_dict["logical_date"] = logical_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if data_interval_start is not UNSET:
            field_dict["data_interval_start"] = data_interval_start
        if data_interval_end is not UNSET:
            field_dict["data_interval_end"] = data_interval_end
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id", UNSET)

        dag_id = d.pop("dag_id", UNSET)

        _logical_date = d.pop("logical_date", UNSET)
        logical_date: datetime.datetime | Unset
        if isinstance(_logical_date, Unset):
            logical_date = UNSET
        else:
            logical_date = isoparse(_logical_date)

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_data_interval_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_interval_start_type_0 = isoparse(data)

                return data_interval_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        data_interval_start = _parse_data_interval_start(d.pop("data_interval_start", UNSET))

        def _parse_data_interval_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_interval_end_type_0 = isoparse(data)

                return data_interval_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        data_interval_end = _parse_data_interval_end(d.pop("data_interval_end", UNSET))

        _state = d.pop("state", UNSET)
        state: DagState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DagState(_state)

        basic_dag_run = cls(
            run_id=run_id,
            dag_id=dag_id,
            logical_date=logical_date,
            start_date=start_date,
            end_date=end_date,
            data_interval_start=data_interval_start,
            data_interval_end=data_interval_end,
            state=state,
        )

        basic_dag_run.additional_properties = d
        return basic_dag_run

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
