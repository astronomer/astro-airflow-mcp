from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.reprocess_behavior import ReprocessBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_run_conf import DagRunConf


T = TypeVar("T", bound="BackfillPostBody")


@_attrs_define
class BackfillPostBody:
    """Object used for create backfill request.

    Attributes:
        dag_id (str):
        from_date (datetime.datetime):
        to_date (datetime.datetime):
        run_backwards (bool | Unset):  Default: False.
        dag_run_conf (DagRunConf | Unset):
        reprocess_behavior (ReprocessBehavior | Unset): Internal enum for setting reprocess behavior in a backfill.

            :meta private:
        max_active_runs (int | Unset):  Default: 10.
    """

    dag_id: str
    from_date: datetime.datetime
    to_date: datetime.datetime
    run_backwards: bool | Unset = False
    dag_run_conf: DagRunConf | Unset = UNSET
    reprocess_behavior: ReprocessBehavior | Unset = UNSET
    max_active_runs: int | Unset = 10

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        from_date = self.from_date.isoformat()

        to_date = self.to_date.isoformat()

        run_backwards = self.run_backwards

        dag_run_conf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dag_run_conf, Unset):
            dag_run_conf = self.dag_run_conf.to_dict()

        reprocess_behavior: str | Unset = UNSET
        if not isinstance(self.reprocess_behavior, Unset):
            reprocess_behavior = self.reprocess_behavior.value

        max_active_runs = self.max_active_runs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dag_id": dag_id,
                "from_date": from_date,
                "to_date": to_date,
            }
        )
        if run_backwards is not UNSET:
            field_dict["run_backwards"] = run_backwards
        if dag_run_conf is not UNSET:
            field_dict["dag_run_conf"] = dag_run_conf
        if reprocess_behavior is not UNSET:
            field_dict["reprocess_behavior"] = reprocess_behavior
        if max_active_runs is not UNSET:
            field_dict["max_active_runs"] = max_active_runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_run_conf import DagRunConf

        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        from_date = isoparse(d.pop("from_date"))

        to_date = isoparse(d.pop("to_date"))

        run_backwards = d.pop("run_backwards", UNSET)

        _dag_run_conf = d.pop("dag_run_conf", UNSET)
        dag_run_conf: DagRunConf | Unset
        if isinstance(_dag_run_conf, Unset):
            dag_run_conf = UNSET
        else:
            dag_run_conf = DagRunConf.from_dict(_dag_run_conf)

        _reprocess_behavior = d.pop("reprocess_behavior", UNSET)
        reprocess_behavior: ReprocessBehavior | Unset
        if isinstance(_reprocess_behavior, Unset):
            reprocess_behavior = UNSET
        else:
            reprocess_behavior = ReprocessBehavior(_reprocess_behavior)

        max_active_runs = d.pop("max_active_runs", UNSET)

        backfill_post_body = cls(
            dag_id=dag_id,
            from_date=from_date,
            to_date=to_date,
            run_backwards=run_backwards,
            dag_run_conf=dag_run_conf,
            reprocess_behavior=reprocess_behavior,
            max_active_runs=max_active_runs,
        )

        return backfill_post_body
