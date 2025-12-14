from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dag_run_run_type import DAGRunRunType
from ..models.dag_state import DagState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_run_conf import DAGRunConf


T = TypeVar("T", bound="DAGRun")


@_attrs_define
class DAGRun:
    """
    Attributes:
        dag_run_id (None | str | Unset): Run ID.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            If not provided, a value will be generated based on execution_date.

            If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.

            This together with DAG_ID are a unique key.
        dag_id (str | Unset):
        logical_date (datetime.datetime | None | Unset): The logical date (previously called execution date). This is
            the time or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*
        execution_date (datetime.datetime | None | Unset): The execution date. This is the same as logical_date, kept
            for backwards compatibility.
            If both this field and logical_date are provided but with different values, the request
            will fail with an BAD_REQUEST error.

            *Changed in version 2.2.0*&#58; Field becomes nullable.

            *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.
        start_date (datetime.datetime | None | Unset): The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.
        end_date (datetime.datetime | None | Unset):
        data_interval_start (datetime.datetime | None | Unset): The beginning of the interval the DAG run covers.
        data_interval_end (datetime.datetime | None | Unset): The end of the interval the DAG run covers.
        last_scheduling_decision (datetime.datetime | None | Unset):
        run_type (DAGRunRunType | Unset):
        state (DagState | Unset): DAG State.

            *Changed in version 2.1.3*&#58; 'queued' is added as a possible value.
        external_trigger (bool | Unset):
        conf (DAGRunConf | Unset): JSON object describing additional configuration parameters.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.
        note (None | str | Unset): Contains manually entered notes by the user about the DagRun.

            *New in version 2.5.0*
    """

    dag_run_id: None | str | Unset = UNSET
    dag_id: str | Unset = UNSET
    logical_date: datetime.datetime | None | Unset = UNSET
    execution_date: datetime.datetime | None | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    data_interval_start: datetime.datetime | None | Unset = UNSET
    data_interval_end: datetime.datetime | None | Unset = UNSET
    last_scheduling_decision: datetime.datetime | None | Unset = UNSET
    run_type: DAGRunRunType | Unset = UNSET
    state: DagState | Unset = UNSET
    external_trigger: bool | Unset = UNSET
    conf: DAGRunConf | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_run_id: None | str | Unset
        if isinstance(self.dag_run_id, Unset):
            dag_run_id = UNSET
        else:
            dag_run_id = self.dag_run_id

        dag_id = self.dag_id

        logical_date: None | str | Unset
        if isinstance(self.logical_date, Unset):
            logical_date = UNSET
        elif isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        execution_date: None | str | Unset
        if isinstance(self.execution_date, Unset):
            execution_date = UNSET
        elif isinstance(self.execution_date, datetime.datetime):
            execution_date = self.execution_date.isoformat()
        else:
            execution_date = self.execution_date

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

        last_scheduling_decision: None | str | Unset
        if isinstance(self.last_scheduling_decision, Unset):
            last_scheduling_decision = UNSET
        elif isinstance(self.last_scheduling_decision, datetime.datetime):
            last_scheduling_decision = self.last_scheduling_decision.isoformat()
        else:
            last_scheduling_decision = self.last_scheduling_decision

        run_type: str | Unset = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        external_trigger = self.external_trigger

        conf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conf, Unset):
            conf = self.conf.to_dict()

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dag_run_id is not UNSET:
            field_dict["dag_run_id"] = dag_run_id
        if dag_id is not UNSET:
            field_dict["dag_id"] = dag_id
        if logical_date is not UNSET:
            field_dict["logical_date"] = logical_date
        if execution_date is not UNSET:
            field_dict["execution_date"] = execution_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if data_interval_start is not UNSET:
            field_dict["data_interval_start"] = data_interval_start
        if data_interval_end is not UNSET:
            field_dict["data_interval_end"] = data_interval_end
        if last_scheduling_decision is not UNSET:
            field_dict["last_scheduling_decision"] = last_scheduling_decision
        if run_type is not UNSET:
            field_dict["run_type"] = run_type
        if state is not UNSET:
            field_dict["state"] = state
        if external_trigger is not UNSET:
            field_dict["external_trigger"] = external_trigger
        if conf is not UNSET:
            field_dict["conf"] = conf
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_run_conf import DAGRunConf

        d = dict(src_dict)

        def _parse_dag_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dag_run_id = _parse_dag_run_id(d.pop("dag_run_id", UNSET))

        dag_id = d.pop("dag_id", UNSET)

        def _parse_logical_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_type_0 = isoparse(data)

                return logical_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        logical_date = _parse_logical_date(d.pop("logical_date", UNSET))

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

        def _parse_last_scheduling_decision(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_scheduling_decision_type_0 = isoparse(data)

                return last_scheduling_decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_scheduling_decision = _parse_last_scheduling_decision(d.pop("last_scheduling_decision", UNSET))

        _run_type = d.pop("run_type", UNSET)
        run_type: DAGRunRunType | Unset
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = DAGRunRunType(_run_type)

        _state = d.pop("state", UNSET)
        state: DagState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DagState(_state)

        external_trigger = d.pop("external_trigger", UNSET)

        _conf = d.pop("conf", UNSET)
        conf: DAGRunConf | Unset
        if isinstance(_conf, Unset):
            conf = UNSET
        else:
            conf = DAGRunConf.from_dict(_conf)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        dag_run = cls(
            dag_run_id=dag_run_id,
            dag_id=dag_id,
            logical_date=logical_date,
            execution_date=execution_date,
            start_date=start_date,
            end_date=end_date,
            data_interval_start=data_interval_start,
            data_interval_end=data_interval_end,
            last_scheduling_decision=last_scheduling_decision,
            run_type=run_type,
            state=state,
            external_trigger=external_trigger,
            conf=conf,
            note=note,
        )

        dag_run.additional_properties = d
        return dag_run

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
