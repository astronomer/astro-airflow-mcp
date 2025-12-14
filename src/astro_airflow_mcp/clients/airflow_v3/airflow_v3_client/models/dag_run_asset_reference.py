from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="DagRunAssetReference")


@_attrs_define
class DagRunAssetReference:
    """DAGRun serializer for asset responses.

    Attributes:
        run_id (str):
        dag_id (str):
        logical_date (datetime.datetime | None):
        start_date (datetime.datetime):
        end_date (datetime.datetime | None):
        state (str):
        data_interval_start (datetime.datetime | None):
        data_interval_end (datetime.datetime | None):
    """

    run_id: str
    dag_id: str
    logical_date: datetime.datetime | None
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    state: str
    data_interval_start: datetime.datetime | None
    data_interval_end: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        dag_id = self.dag_id

        logical_date: None | str
        if isinstance(self.logical_date, datetime.datetime):
            logical_date = self.logical_date.isoformat()
        else:
            logical_date = self.logical_date

        start_date = self.start_date.isoformat()

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        state = self.state

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "run_id": run_id,
                "dag_id": dag_id,
                "logical_date": logical_date,
                "start_date": start_date,
                "end_date": end_date,
                "state": state,
                "data_interval_start": data_interval_start,
                "data_interval_end": data_interval_end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

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

        start_date = isoparse(d.pop("start_date"))

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

        state = d.pop("state")

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

        dag_run_asset_reference = cls(
            run_id=run_id,
            dag_id=dag_id,
            logical_date=logical_date,
            start_date=start_date,
            end_date=end_date,
            state=state,
            data_interval_start=data_interval_start,
            data_interval_end=data_interval_end,
        )

        return dag_run_asset_reference
