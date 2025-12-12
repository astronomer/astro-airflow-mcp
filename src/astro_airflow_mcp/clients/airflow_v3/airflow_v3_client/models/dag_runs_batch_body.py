from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.dag_run_state import DagRunState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DAGRunsBatchBody")


@_attrs_define
class DAGRunsBatchBody:
    """List DAG Runs body for batch endpoint.

    Attributes:
        order_by (None | str | Unset):
        page_offset (int | Unset):  Default: 0.
        page_limit (int | Unset):  Default: 100.
        dag_ids (list[str] | None | Unset):
        states (list[DagRunState | None] | None | Unset):
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
    """

    order_by: None | str | Unset = UNSET
    page_offset: int | Unset = 0
    page_limit: int | Unset = 100
    dag_ids: list[str] | None | Unset = UNSET
    states: list[DagRunState | None] | None | Unset = UNSET
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

    def to_dict(self) -> dict[str, Any]:
        order_by: None | str | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        else:
            order_by = self.order_by

        page_offset = self.page_offset

        page_limit = self.page_limit

        dag_ids: list[str] | None | Unset
        if isinstance(self.dag_ids, Unset):
            dag_ids = UNSET
        elif isinstance(self.dag_ids, list):
            dag_ids = self.dag_ids

        else:
            dag_ids = self.dag_ids

        states: list[None | str] | None | Unset
        if isinstance(self.states, Unset):
            states = UNSET
        elif isinstance(self.states, list):
            states = []
            for states_type_0_item_data in self.states:
                states_type_0_item: None | str
                if isinstance(states_type_0_item_data, DagRunState):
                    states_type_0_item = states_type_0_item_data.value
                else:
                    states_type_0_item = states_type_0_item_data
                states.append(states_type_0_item)

        else:
            states = self.states

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if page_offset is not UNSET:
            field_dict["page_offset"] = page_offset
        if page_limit is not UNSET:
            field_dict["page_limit"] = page_limit
        if dag_ids is not UNSET:
            field_dict["dag_ids"] = dag_ids
        if states is not UNSET:
            field_dict["states"] = states
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_order_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        page_offset = d.pop("page_offset", UNSET)

        page_limit = d.pop("page_limit", UNSET)

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

        def _parse_states(data: object) -> list[DagRunState | None] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                states_type_0 = []
                _states_type_0 = data
                for states_type_0_item_data in _states_type_0:

                    def _parse_states_type_0_item(data: object) -> DagRunState | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            states_type_0_item_type_0 = DagRunState(data)

                            return states_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(DagRunState | None, data)

                    states_type_0_item = _parse_states_type_0_item(states_type_0_item_data)

                    states_type_0.append(states_type_0_item)

                return states_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DagRunState | None] | None | Unset, data)

        states = _parse_states(d.pop("states", UNSET))

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

        dag_runs_batch_body = cls(
            order_by=order_by,
            page_offset=page_offset,
            page_limit=page_limit,
            dag_ids=dag_ids,
            states=states,
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
        )

        return dag_runs_batch_body
