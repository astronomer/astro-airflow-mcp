from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.task_instance_state import TaskInstanceState
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskInstancesBatchBody")


@_attrs_define
class TaskInstancesBatchBody:
    """Task Instance body for get batch.

    Attributes:
        dag_ids (list[str] | None | Unset):
        dag_run_ids (list[str] | None | Unset):
        task_ids (list[str] | None | Unset):
        state (list[None | TaskInstanceState] | None | Unset):
        run_after_gte (datetime.datetime | None | Unset):
        run_after_gt (datetime.datetime | None | Unset):
        run_after_lte (datetime.datetime | None | Unset):
        run_after_lt (datetime.datetime | None | Unset):
        logical_date_gte (datetime.datetime | None | Unset):
        logical_date_gt (datetime.datetime | None | Unset):
        logical_date_lte (datetime.datetime | None | Unset):
        logical_date_lt (datetime.datetime | None | Unset):
        start_date_gte (datetime.datetime | None | Unset):
        start_date_gt (datetime.datetime | None | Unset):
        start_date_lte (datetime.datetime | None | Unset):
        start_date_lt (datetime.datetime | None | Unset):
        end_date_gte (datetime.datetime | None | Unset):
        end_date_gt (datetime.datetime | None | Unset):
        end_date_lte (datetime.datetime | None | Unset):
        end_date_lt (datetime.datetime | None | Unset):
        duration_gte (float | None | Unset):
        duration_gt (float | None | Unset):
        duration_lte (float | None | Unset):
        duration_lt (float | None | Unset):
        pool (list[str] | None | Unset):
        queue (list[str] | None | Unset):
        executor (list[str] | None | Unset):
        page_offset (int | Unset):  Default: 0.
        page_limit (int | Unset):  Default: 100.
        order_by (None | str | Unset):
    """

    dag_ids: list[str] | None | Unset = UNSET
    dag_run_ids: list[str] | None | Unset = UNSET
    task_ids: list[str] | None | Unset = UNSET
    state: list[None | TaskInstanceState] | None | Unset = UNSET
    run_after_gte: datetime.datetime | None | Unset = UNSET
    run_after_gt: datetime.datetime | None | Unset = UNSET
    run_after_lte: datetime.datetime | None | Unset = UNSET
    run_after_lt: datetime.datetime | None | Unset = UNSET
    logical_date_gte: datetime.datetime | None | Unset = UNSET
    logical_date_gt: datetime.datetime | None | Unset = UNSET
    logical_date_lte: datetime.datetime | None | Unset = UNSET
    logical_date_lt: datetime.datetime | None | Unset = UNSET
    start_date_gte: datetime.datetime | None | Unset = UNSET
    start_date_gt: datetime.datetime | None | Unset = UNSET
    start_date_lte: datetime.datetime | None | Unset = UNSET
    start_date_lt: datetime.datetime | None | Unset = UNSET
    end_date_gte: datetime.datetime | None | Unset = UNSET
    end_date_gt: datetime.datetime | None | Unset = UNSET
    end_date_lte: datetime.datetime | None | Unset = UNSET
    end_date_lt: datetime.datetime | None | Unset = UNSET
    duration_gte: float | None | Unset = UNSET
    duration_gt: float | None | Unset = UNSET
    duration_lte: float | None | Unset = UNSET
    duration_lt: float | None | Unset = UNSET
    pool: list[str] | None | Unset = UNSET
    queue: list[str] | None | Unset = UNSET
    executor: list[str] | None | Unset = UNSET
    page_offset: int | Unset = 0
    page_limit: int | Unset = 100
    order_by: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dag_ids: list[str] | None | Unset
        if isinstance(self.dag_ids, Unset):
            dag_ids = UNSET
        elif isinstance(self.dag_ids, list):
            dag_ids = self.dag_ids

        else:
            dag_ids = self.dag_ids

        dag_run_ids: list[str] | None | Unset
        if isinstance(self.dag_run_ids, Unset):
            dag_run_ids = UNSET
        elif isinstance(self.dag_run_ids, list):
            dag_run_ids = self.dag_run_ids

        else:
            dag_run_ids = self.dag_run_ids

        task_ids: list[str] | None | Unset
        if isinstance(self.task_ids, Unset):
            task_ids = UNSET
        elif isinstance(self.task_ids, list):
            task_ids = self.task_ids

        else:
            task_ids = self.task_ids

        state: list[None | str] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, list):
            state = []
            for state_type_0_item_data in self.state:
                state_type_0_item: None | str
                if isinstance(state_type_0_item_data, TaskInstanceState):
                    state_type_0_item = state_type_0_item_data.value
                else:
                    state_type_0_item = state_type_0_item_data
                state.append(state_type_0_item)

        else:
            state = self.state

        run_after_gte: None | str | Unset
        if isinstance(self.run_after_gte, Unset):
            run_after_gte = UNSET
        elif isinstance(self.run_after_gte, datetime.datetime):
            run_after_gte = self.run_after_gte.isoformat()
        else:
            run_after_gte = self.run_after_gte

        run_after_gt: None | str | Unset
        if isinstance(self.run_after_gt, Unset):
            run_after_gt = UNSET
        elif isinstance(self.run_after_gt, datetime.datetime):
            run_after_gt = self.run_after_gt.isoformat()
        else:
            run_after_gt = self.run_after_gt

        run_after_lte: None | str | Unset
        if isinstance(self.run_after_lte, Unset):
            run_after_lte = UNSET
        elif isinstance(self.run_after_lte, datetime.datetime):
            run_after_lte = self.run_after_lte.isoformat()
        else:
            run_after_lte = self.run_after_lte

        run_after_lt: None | str | Unset
        if isinstance(self.run_after_lt, Unset):
            run_after_lt = UNSET
        elif isinstance(self.run_after_lt, datetime.datetime):
            run_after_lt = self.run_after_lt.isoformat()
        else:
            run_after_lt = self.run_after_lt

        logical_date_gte: None | str | Unset
        if isinstance(self.logical_date_gte, Unset):
            logical_date_gte = UNSET
        elif isinstance(self.logical_date_gte, datetime.datetime):
            logical_date_gte = self.logical_date_gte.isoformat()
        else:
            logical_date_gte = self.logical_date_gte

        logical_date_gt: None | str | Unset
        if isinstance(self.logical_date_gt, Unset):
            logical_date_gt = UNSET
        elif isinstance(self.logical_date_gt, datetime.datetime):
            logical_date_gt = self.logical_date_gt.isoformat()
        else:
            logical_date_gt = self.logical_date_gt

        logical_date_lte: None | str | Unset
        if isinstance(self.logical_date_lte, Unset):
            logical_date_lte = UNSET
        elif isinstance(self.logical_date_lte, datetime.datetime):
            logical_date_lte = self.logical_date_lte.isoformat()
        else:
            logical_date_lte = self.logical_date_lte

        logical_date_lt: None | str | Unset
        if isinstance(self.logical_date_lt, Unset):
            logical_date_lt = UNSET
        elif isinstance(self.logical_date_lt, datetime.datetime):
            logical_date_lt = self.logical_date_lt.isoformat()
        else:
            logical_date_lt = self.logical_date_lt

        start_date_gte: None | str | Unset
        if isinstance(self.start_date_gte, Unset):
            start_date_gte = UNSET
        elif isinstance(self.start_date_gte, datetime.datetime):
            start_date_gte = self.start_date_gte.isoformat()
        else:
            start_date_gte = self.start_date_gte

        start_date_gt: None | str | Unset
        if isinstance(self.start_date_gt, Unset):
            start_date_gt = UNSET
        elif isinstance(self.start_date_gt, datetime.datetime):
            start_date_gt = self.start_date_gt.isoformat()
        else:
            start_date_gt = self.start_date_gt

        start_date_lte: None | str | Unset
        if isinstance(self.start_date_lte, Unset):
            start_date_lte = UNSET
        elif isinstance(self.start_date_lte, datetime.datetime):
            start_date_lte = self.start_date_lte.isoformat()
        else:
            start_date_lte = self.start_date_lte

        start_date_lt: None | str | Unset
        if isinstance(self.start_date_lt, Unset):
            start_date_lt = UNSET
        elif isinstance(self.start_date_lt, datetime.datetime):
            start_date_lt = self.start_date_lt.isoformat()
        else:
            start_date_lt = self.start_date_lt

        end_date_gte: None | str | Unset
        if isinstance(self.end_date_gte, Unset):
            end_date_gte = UNSET
        elif isinstance(self.end_date_gte, datetime.datetime):
            end_date_gte = self.end_date_gte.isoformat()
        else:
            end_date_gte = self.end_date_gte

        end_date_gt: None | str | Unset
        if isinstance(self.end_date_gt, Unset):
            end_date_gt = UNSET
        elif isinstance(self.end_date_gt, datetime.datetime):
            end_date_gt = self.end_date_gt.isoformat()
        else:
            end_date_gt = self.end_date_gt

        end_date_lte: None | str | Unset
        if isinstance(self.end_date_lte, Unset):
            end_date_lte = UNSET
        elif isinstance(self.end_date_lte, datetime.datetime):
            end_date_lte = self.end_date_lte.isoformat()
        else:
            end_date_lte = self.end_date_lte

        end_date_lt: None | str | Unset
        if isinstance(self.end_date_lt, Unset):
            end_date_lt = UNSET
        elif isinstance(self.end_date_lt, datetime.datetime):
            end_date_lt = self.end_date_lt.isoformat()
        else:
            end_date_lt = self.end_date_lt

        duration_gte: float | None | Unset
        if isinstance(self.duration_gte, Unset):
            duration_gte = UNSET
        else:
            duration_gte = self.duration_gte

        duration_gt: float | None | Unset
        if isinstance(self.duration_gt, Unset):
            duration_gt = UNSET
        else:
            duration_gt = self.duration_gt

        duration_lte: float | None | Unset
        if isinstance(self.duration_lte, Unset):
            duration_lte = UNSET
        else:
            duration_lte = self.duration_lte

        duration_lt: float | None | Unset
        if isinstance(self.duration_lt, Unset):
            duration_lt = UNSET
        else:
            duration_lt = self.duration_lt

        pool: list[str] | None | Unset
        if isinstance(self.pool, Unset):
            pool = UNSET
        elif isinstance(self.pool, list):
            pool = self.pool

        else:
            pool = self.pool

        queue: list[str] | None | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        elif isinstance(self.queue, list):
            queue = self.queue

        else:
            queue = self.queue

        executor: list[str] | None | Unset
        if isinstance(self.executor, Unset):
            executor = UNSET
        elif isinstance(self.executor, list):
            executor = self.executor

        else:
            executor = self.executor

        page_offset = self.page_offset

        page_limit = self.page_limit

        order_by: None | str | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        else:
            order_by = self.order_by

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dag_ids is not UNSET:
            field_dict["dag_ids"] = dag_ids
        if dag_run_ids is not UNSET:
            field_dict["dag_run_ids"] = dag_run_ids
        if task_ids is not UNSET:
            field_dict["task_ids"] = task_ids
        if state is not UNSET:
            field_dict["state"] = state
        if run_after_gte is not UNSET:
            field_dict["run_after_gte"] = run_after_gte
        if run_after_gt is not UNSET:
            field_dict["run_after_gt"] = run_after_gt
        if run_after_lte is not UNSET:
            field_dict["run_after_lte"] = run_after_lte
        if run_after_lt is not UNSET:
            field_dict["run_after_lt"] = run_after_lt
        if logical_date_gte is not UNSET:
            field_dict["logical_date_gte"] = logical_date_gte
        if logical_date_gt is not UNSET:
            field_dict["logical_date_gt"] = logical_date_gt
        if logical_date_lte is not UNSET:
            field_dict["logical_date_lte"] = logical_date_lte
        if logical_date_lt is not UNSET:
            field_dict["logical_date_lt"] = logical_date_lt
        if start_date_gte is not UNSET:
            field_dict["start_date_gte"] = start_date_gte
        if start_date_gt is not UNSET:
            field_dict["start_date_gt"] = start_date_gt
        if start_date_lte is not UNSET:
            field_dict["start_date_lte"] = start_date_lte
        if start_date_lt is not UNSET:
            field_dict["start_date_lt"] = start_date_lt
        if end_date_gte is not UNSET:
            field_dict["end_date_gte"] = end_date_gte
        if end_date_gt is not UNSET:
            field_dict["end_date_gt"] = end_date_gt
        if end_date_lte is not UNSET:
            field_dict["end_date_lte"] = end_date_lte
        if end_date_lt is not UNSET:
            field_dict["end_date_lt"] = end_date_lt
        if duration_gte is not UNSET:
            field_dict["duration_gte"] = duration_gte
        if duration_gt is not UNSET:
            field_dict["duration_gt"] = duration_gt
        if duration_lte is not UNSET:
            field_dict["duration_lte"] = duration_lte
        if duration_lt is not UNSET:
            field_dict["duration_lt"] = duration_lt
        if pool is not UNSET:
            field_dict["pool"] = pool
        if queue is not UNSET:
            field_dict["queue"] = queue
        if executor is not UNSET:
            field_dict["executor"] = executor
        if page_offset is not UNSET:
            field_dict["page_offset"] = page_offset
        if page_limit is not UNSET:
            field_dict["page_limit"] = page_limit
        if order_by is not UNSET:
            field_dict["order_by"] = order_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dag_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dag_ids_type_0 = cast(list[str], data)

                return dag_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dag_ids = _parse_dag_ids(d.pop("dag_ids", UNSET))

        def _parse_dag_run_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dag_run_ids_type_0 = cast(list[str], data)

                return dag_run_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dag_run_ids = _parse_dag_run_ids(d.pop("dag_run_ids", UNSET))

        def _parse_task_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                task_ids_type_0 = cast(list[str], data)

                return task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        task_ids = _parse_task_ids(d.pop("task_ids", UNSET))

        def _parse_state(data: object) -> list[None | TaskInstanceState] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                state_type_0 = []
                _state_type_0 = data
                for state_type_0_item_data in _state_type_0:

                    def _parse_state_type_0_item(data: object) -> None | TaskInstanceState:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            state_type_0_item_type_0 = TaskInstanceState(data)

                            return state_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | TaskInstanceState, data)

                    state_type_0_item = _parse_state_type_0_item(state_type_0_item_data)

                    state_type_0.append(state_type_0_item)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | TaskInstanceState] | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_run_after_gte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_after_gte_type_0 = isoparse(data)

                return run_after_gte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        run_after_gte = _parse_run_after_gte(d.pop("run_after_gte", UNSET))

        def _parse_run_after_gt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_after_gt_type_0 = isoparse(data)

                return run_after_gt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        run_after_gt = _parse_run_after_gt(d.pop("run_after_gt", UNSET))

        def _parse_run_after_lte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_after_lte_type_0 = isoparse(data)

                return run_after_lte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        run_after_lte = _parse_run_after_lte(d.pop("run_after_lte", UNSET))

        def _parse_run_after_lt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                run_after_lt_type_0 = isoparse(data)

                return run_after_lt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        run_after_lt = _parse_run_after_lt(d.pop("run_after_lt", UNSET))

        def _parse_logical_date_gte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_gte_type_0 = isoparse(data)

                return logical_date_gte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        logical_date_gte = _parse_logical_date_gte(d.pop("logical_date_gte", UNSET))

        def _parse_logical_date_gt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_gt_type_0 = isoparse(data)

                return logical_date_gt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        logical_date_gt = _parse_logical_date_gt(d.pop("logical_date_gt", UNSET))

        def _parse_logical_date_lte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_lte_type_0 = isoparse(data)

                return logical_date_lte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        logical_date_lte = _parse_logical_date_lte(d.pop("logical_date_lte", UNSET))

        def _parse_logical_date_lt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logical_date_lt_type_0 = isoparse(data)

                return logical_date_lt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        logical_date_lt = _parse_logical_date_lt(d.pop("logical_date_lt", UNSET))

        def _parse_start_date_gte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_gte_type_0 = isoparse(data)

                return start_date_gte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date_gte = _parse_start_date_gte(d.pop("start_date_gte", UNSET))

        def _parse_start_date_gt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_gt_type_0 = isoparse(data)

                return start_date_gt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date_gt = _parse_start_date_gt(d.pop("start_date_gt", UNSET))

        def _parse_start_date_lte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_lte_type_0 = isoparse(data)

                return start_date_lte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date_lte = _parse_start_date_lte(d.pop("start_date_lte", UNSET))

        def _parse_start_date_lt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_lt_type_0 = isoparse(data)

                return start_date_lt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date_lt = _parse_start_date_lt(d.pop("start_date_lt", UNSET))

        def _parse_end_date_gte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_gte_type_0 = isoparse(data)

                return end_date_gte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date_gte = _parse_end_date_gte(d.pop("end_date_gte", UNSET))

        def _parse_end_date_gt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_gt_type_0 = isoparse(data)

                return end_date_gt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date_gt = _parse_end_date_gt(d.pop("end_date_gt", UNSET))

        def _parse_end_date_lte(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_lte_type_0 = isoparse(data)

                return end_date_lte_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date_lte = _parse_end_date_lte(d.pop("end_date_lte", UNSET))

        def _parse_end_date_lt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_lt_type_0 = isoparse(data)

                return end_date_lt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date_lt = _parse_end_date_lt(d.pop("end_date_lt", UNSET))

        def _parse_duration_gte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_gte = _parse_duration_gte(d.pop("duration_gte", UNSET))

        def _parse_duration_gt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_gt = _parse_duration_gt(d.pop("duration_gt", UNSET))

        def _parse_duration_lte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_lte = _parse_duration_lte(d.pop("duration_lte", UNSET))

        def _parse_duration_lt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_lt = _parse_duration_lt(d.pop("duration_lt", UNSET))

        def _parse_pool(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pool_type_0 = cast(list[str], data)

                return pool_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        pool = _parse_pool(d.pop("pool", UNSET))

        def _parse_queue(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                queue_type_0 = cast(list[str], data)

                return queue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_executor(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                executor_type_0 = cast(list[str], data)

                return executor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        executor = _parse_executor(d.pop("executor", UNSET))

        page_offset = d.pop("page_offset", UNSET)

        page_limit = d.pop("page_limit", UNSET)

        def _parse_order_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        task_instances_batch_body = cls(
            dag_ids=dag_ids,
            dag_run_ids=dag_run_ids,
            task_ids=task_ids,
            state=state,
            run_after_gte=run_after_gte,
            run_after_gt=run_after_gt,
            run_after_lte=run_after_lte,
            run_after_lt=run_after_lt,
            logical_date_gte=logical_date_gte,
            logical_date_gt=logical_date_gt,
            logical_date_lte=logical_date_lte,
            logical_date_lt=logical_date_lt,
            start_date_gte=start_date_gte,
            start_date_gt=start_date_gt,
            start_date_lte=start_date_lte,
            start_date_lt=start_date_lt,
            end_date_gte=end_date_gte,
            end_date_gt=end_date_gt,
            end_date_lte=end_date_lte,
            end_date_lt=end_date_lt,
            duration_gte=duration_gte,
            duration_gt=duration_gt,
            duration_lte=duration_lte,
            duration_lt=duration_lt,
            pool=pool,
            queue=queue,
            executor=executor,
            page_offset=page_offset,
            page_limit=page_limit,
            order_by=order_by,
        )

        return task_instances_batch_body
