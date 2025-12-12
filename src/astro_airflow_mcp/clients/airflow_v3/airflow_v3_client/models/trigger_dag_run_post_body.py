from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_dag_run_post_body_conf_type_0 import TriggerDAGRunPostBodyConfType0


T = TypeVar("T", bound="TriggerDAGRunPostBody")


@_attrs_define
class TriggerDAGRunPostBody:
    """Trigger DAG Run Serializer for POST body.

    Attributes:
        logical_date (datetime.datetime | None):
        dag_run_id (None | str | Unset):
        data_interval_start (datetime.datetime | None | Unset):
        data_interval_end (datetime.datetime | None | Unset):
        run_after (datetime.datetime | None | Unset):
        conf (None | TriggerDAGRunPostBodyConfType0 | Unset):
        note (None | str | Unset):
    """

    logical_date: datetime.datetime | None
    dag_run_id: None | str | Unset = UNSET
    data_interval_start: datetime.datetime | None | Unset = UNSET
    data_interval_end: datetime.datetime | None | Unset = UNSET
    run_after: datetime.datetime | None | Unset = UNSET
    conf: None | TriggerDAGRunPostBodyConfType0 | Unset = UNSET
    note: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_dag_run_post_body_conf_type_0 import TriggerDAGRunPostBodyConfType0

        logical_date: None | str
        if isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        dag_run_id: None | str | Unset
        if isinstance(self.dag_run_id, Unset):
            dag_run_id = UNSET
        else:
            dag_run_id = self.dag_run_id

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

        run_after: None | str | Unset
        if isinstance(self.run_after, Unset):
            run_after = UNSET
        elif isinstance(self.run_after, datetime.datetime):
            run_after = self.run_after.isoformat()
        else:
            run_after = self.run_after

        conf: dict[str, Any] | None | Unset
        if isinstance(self.conf, Unset):
            conf = UNSET
        elif isinstance(self.conf, TriggerDAGRunPostBodyConfType0):
            conf = self.conf.to_dict()
        else:
            conf = self.conf

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "logical_date": logical_date,
            }
        )
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if data_interval_start is not UNSET:
            field_dict["data_interval_start"] = data_interval_start
        if data_interval_end is not UNSET:
            field_dict["data_interval_end"] = data_interval_end
        if run_after is not UNSET:
            field_dict["run_after"] = run_after
        if conf is not UNSET:
            field_dict["conf"] = conf
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_dag_run_post_body_conf_type_0 import TriggerDAGRunPostBodyConfType0

        d = dict(src_dict)

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

        def _parse_dag_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_run_id = _parse_dag_run_id(d.pop("dag_run_id", UNSET))

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

        def _parse_run_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_after_type_0 = isoparse(data)

                return run_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        run_after = _parse_run_after(d.pop("run_after", UNSET))

        def _parse_conf(data: object) -> None | TriggerDAGRunPostBodyConfType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conf_type_0 = TriggerDAGRunPostBodyConfType0.from_dict(data)

                return conf_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerDAGRunPostBodyConfType0 | Unset, data)

        conf = _parse_conf(d.pop("conf", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        trigger_dag_run_post_body = cls(
            logical_date=logical_date,
            dag_run_id=dag_run_id,
            data_interval_start=data_interval_start,
            data_interval_end=data_interval_end,
            run_after=run_after,
            conf=conf,
            note=note,
        )

        return trigger_dag_run_post_body
