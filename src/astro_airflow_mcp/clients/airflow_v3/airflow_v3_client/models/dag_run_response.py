from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dag_run_state import DagRunState
from ..models.dag_run_triggered_by_type import DagRunTriggeredByType
from ..models.dag_run_type import DagRunType

if TYPE_CHECKING:
    from ..models.dag_run_response_conf_type_0 import DAGRunResponseConfType0
    from ..models.dag_version_response import DagVersionResponse


T = TypeVar("T", bound="DAGRunResponse")


@_attrs_define
class DAGRunResponse:
    """DAG Run serializer for responses.

    Attributes:
        dag_run_id (str):
        dag_id (str):
        logical_date (datetime.datetime | None):
        queued_at (datetime.datetime | None):
        start_date (datetime.datetime | None):
        end_date (datetime.datetime | None):
        duration (float | None):
        data_interval_start (datetime.datetime | None):
        data_interval_end (datetime.datetime | None):
        run_after (datetime.datetime):
        last_scheduling_decision (datetime.datetime | None):
        run_type (DagRunType): Class with DagRun types.
        state (DagRunState): All possible states that a DagRun can be in.

            These are "shared" with TaskInstanceState in some parts of the code,
            so please ensure that their values always match the ones with the
            same name in TaskInstanceState.
        triggered_by (DagRunTriggeredByType | None):
        triggering_user_name (None | str):
        conf (DAGRunResponseConfType0 | None):
        note (None | str):
        dag_versions (list[DagVersionResponse]):
        bundle_version (None | str):
        dag_display_name (str):
    """

    dag_run_id: str
    dag_id: str
    logical_date: datetime.datetime | None
    queued_at: datetime.datetime | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    duration: float | None
    data_interval_start: datetime.datetime | None
    data_interval_end: datetime.datetime | None
    run_after: datetime.datetime
    last_scheduling_decision: datetime.datetime | None
    run_type: DagRunType
    state: DagRunState
    triggered_by: DagRunTriggeredByType | None
    triggering_user_name: None | str
    conf: DAGRunResponseConfType0 | None
    note: None | str
    dag_versions: list[DagVersionResponse]
    bundle_version: None | str
    dag_display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dag_run_response_conf_type_0 import DAGRunResponseConfType0

        dag_run_id = self.dag_run_id

        dag_id = self.dag_id

        logical_date: None | str
        if isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        queued_at: None | str
        if isinstance(self.queued_at, datetime.datetime):
            queued_at = self.queued_at.isoformat()
        else:
            queued_at = self.queued_at

        start_date: None | str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        duration: float | None
        duration = self.duration

        data_interval_start: None | str
        if isinstance(self.data_interval_start, datetime.datetime):
            data_interval_start = self.data_interval_start.isoformat()
        else:
            data_interval_start = self.data_interval_start

        data_interval_end: None | str
        if isinstance(self.data_interval_end, datetime.datetime):
            data_interval_end = self.data_interval_end.isoformat()
        else:
            data_interval_end = self.data_interval_end

        run_after = self.run_after.isoformat()

        last_scheduling_decision: None | str
        if isinstance(self.last_scheduling_decision, datetime.datetime):
            last_scheduling_decision = self.last_scheduling_decision.isoformat()
        else:
            last_scheduling_decision = self.last_scheduling_decision

        run_type = self.run_type.value

        state = self.state.value

        triggered_by: None | str
        if isinstance(self.triggered_by, DagRunTriggeredByType):
            triggered_by = self.triggered_by.value
        else:
            triggered_by = self.triggered_by

        triggering_user_name: None | str
        triggering_user_name = self.triggering_user_name

        conf: dict[str, Any] | None
        if isinstance(self.conf, DAGRunResponseConfType0):
            conf = self.conf.to_dict()
        else:
            conf = self.conf

        note: None | str
        note = self.note

        dag_versions = []
        for dag_versions_item_data in self.dag_versions:
            dag_versions_item = dag_versions_item_data.to_dict()
            dag_versions.append(dag_versions_item)

        bundle_version: None | str
        bundle_version = self.bundle_version

        dag_display_name = self.dag_display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_run_id": dag_run_id,
                "dag_id": dag_id,
                "logical_date": logical_date,
                "queued_at": queued_at,
                "start_date": start_date,
                "end_date": end_date,
                "duration": duration,
                "data_interval_start": data_interval_start,
                "data_interval_end": data_interval_end,
                "run_after": run_after,
                "last_scheduling_decision": last_scheduling_decision,
                "run_type": run_type,
                "state": state,
                "triggered_by": triggered_by,
                "triggering_user_name": triggering_user_name,
                "conf": conf,
                "note": note,
                "dag_versions": dag_versions,
                "bundle_version": bundle_version,
                "dag_display_name": dag_display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_run_response_conf_type_0 import DAGRunResponseConfType0
        from ..models.dag_version_response import DagVersionResponse

        d = dict(src_dict)
        dag_run_id = d.pop("dag_run_id")

        dag_id = d.pop("dag_id")

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

        def _parse_queued_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                queued_at_type_0 = isoparse(data)

                return queued_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        queued_at = _parse_queued_at(d.pop("queued_at"))

        def _parse_start_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_end_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_date = _parse_end_date(d.pop("end_date"))

        def _parse_duration(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        duration = _parse_duration(d.pop("duration"))

        def _parse_data_interval_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_interval_start_type_0 = isoparse(data)

                return data_interval_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        data_interval_start = _parse_data_interval_start(d.pop("data_interval_start"))

        def _parse_data_interval_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_interval_end_type_0 = isoparse(data)

                return data_interval_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        data_interval_end = _parse_data_interval_end(d.pop("data_interval_end"))

        run_after = isoparse(d.pop("run_after"))

        def _parse_last_scheduling_decision(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_scheduling_decision_type_0 = isoparse(data)

                return last_scheduling_decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_scheduling_decision = _parse_last_scheduling_decision(d.pop("last_scheduling_decision"))

        run_type = DagRunType(d.pop("run_type"))

        state = DagRunState(d.pop("state"))

        def _parse_triggered_by(data: object) -> DagRunTriggeredByType | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                triggered_by_type_0 = DagRunTriggeredByType(data)

                return triggered_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DagRunTriggeredByType | None, data)

        triggered_by = _parse_triggered_by(d.pop("triggered_by"))

        def _parse_triggering_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        triggering_user_name = _parse_triggering_user_name(d.pop("triggering_user_name"))

        def _parse_conf(data: object) -> DAGRunResponseConfType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conf_type_0 = DAGRunResponseConfType0.from_dict(data)

                return conf_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGRunResponseConfType0 | None, data)

        conf = _parse_conf(d.pop("conf"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        dag_versions = []
        _dag_versions = d.pop("dag_versions")
        for dag_versions_item_data in _dag_versions:
            dag_versions_item = DagVersionResponse.from_dict(dag_versions_item_data)

            dag_versions.append(dag_versions_item)

        def _parse_bundle_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_version = _parse_bundle_version(d.pop("bundle_version"))

        dag_display_name = d.pop("dag_display_name")

        dag_run_response = cls(
            dag_run_id=dag_run_id,
            dag_id=dag_id,
            logical_date=logical_date,
            queued_at=queued_at,
            start_date=start_date,
            end_date=end_date,
            duration=duration,
            data_interval_start=data_interval_start,
            data_interval_end=data_interval_end,
            run_after=run_after,
            last_scheduling_decision=last_scheduling_decision,
            run_type=run_type,
            state=state,
            triggered_by=triggered_by,
            triggering_user_name=triggering_user_name,
            conf=conf,
            note=note,
            dag_versions=dag_versions,
            bundle_version=bundle_version,
            dag_display_name=dag_display_name,
        )

        dag_run_response.additional_properties = d
        return dag_run_response

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
