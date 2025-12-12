from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListDagRunsForm")


@_attrs_define
class ListDagRunsForm:
    """
    Attributes:
        order_by (str | Unset): The name of the field to order the results by. Prefix a field name
            with `-` to reverse the sort order.

            *New in version 2.1.0*
        page_offset (int | Unset): The number of items to skip before starting to collect the result set.
        page_limit (int | Unset): The numbers of items to return. Default: 100.
        dag_ids (list[str] | Unset): Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).
        states (list[str] | Unset): Return objects with specific states.
            The value can be repeated to retrieve multiple matching values (OR condition).
        execution_date_gte (datetime.datetime | Unset): Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte key to receive only the selected period.
        execution_date_lte (datetime.datetime | Unset): Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte key to receive only the selected period.
        start_date_gte (datetime.datetime | Unset): Returns objects greater or equal the specified date.

            This can be combined with start_date_lte key to receive only the selected period.
        start_date_lte (datetime.datetime | Unset): Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period
        end_date_gte (datetime.datetime | Unset): Returns objects greater or equal the specified date.

            This can be combined with end_date_lte parameter to receive only the selected period.
        end_date_lte (datetime.datetime | Unset): Returns objects less than or equal to the specified date.

            This can be combined with end_date_gte parameter to receive only the selected period.
    """

    order_by: str | Unset = UNSET
    page_offset: int | Unset = UNSET
    page_limit: int | Unset = 100
    dag_ids: list[str] | Unset = UNSET
    states: list[str] | Unset = UNSET
    execution_date_gte: datetime.datetime | Unset = UNSET
    execution_date_lte: datetime.datetime | Unset = UNSET
    start_date_gte: datetime.datetime | Unset = UNSET
    start_date_lte: datetime.datetime | Unset = UNSET
    end_date_gte: datetime.datetime | Unset = UNSET
    end_date_lte: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_by = self.order_by

        page_offset = self.page_offset

        page_limit = self.page_limit

        dag_ids: list[str] | Unset = UNSET
        if not isinstance(self.dag_ids, Unset):
            dag_ids = self.dag_ids

        states: list[str] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states

        execution_date_gte: str | Unset = UNSET
        if not isinstance(self.execution_date_gte, Unset):
            execution_date_gte = self.execution_date_gte.isoformat()

        execution_date_lte: str | Unset = UNSET
        if not isinstance(self.execution_date_lte, Unset):
            execution_date_lte = self.execution_date_lte.isoformat()

        start_date_gte: str | Unset = UNSET
        if not isinstance(self.start_date_gte, Unset):
            start_date_gte = self.start_date_gte.isoformat()

        start_date_lte: str | Unset = UNSET
        if not isinstance(self.start_date_lte, Unset):
            start_date_lte = self.start_date_lte.isoformat()

        end_date_gte: str | Unset = UNSET
        if not isinstance(self.end_date_gte, Unset):
            end_date_gte = self.end_date_gte.isoformat()

        end_date_lte: str | Unset = UNSET
        if not isinstance(self.end_date_lte, Unset):
            end_date_lte = self.end_date_lte.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if execution_date_gte is not UNSET:
            field_dict["execution_date_gte"] = execution_date_gte
        if execution_date_lte is not UNSET:
            field_dict["execution_date_lte"] = execution_date_lte
        if start_date_gte is not UNSET:
            field_dict["start_date_gte"] = start_date_gte
        if start_date_lte is not UNSET:
            field_dict["start_date_lte"] = start_date_lte
        if end_date_gte is not UNSET:
            field_dict["end_date_gte"] = end_date_gte
        if end_date_lte is not UNSET:
            field_dict["end_date_lte"] = end_date_lte

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_by = d.pop("order_by", UNSET)

        page_offset = d.pop("page_offset", UNSET)

        page_limit = d.pop("page_limit", UNSET)

        dag_ids = cast(list[str], d.pop("dag_ids", UNSET))

        states = cast(list[str], d.pop("states", UNSET))

        _execution_date_gte = d.pop("execution_date_gte", UNSET)
        execution_date_gte: datetime.datetime | Unset
        if isinstance(_execution_date_gte, Unset):
            execution_date_gte = UNSET
        else:
            execution_date_gte = isoparse(_execution_date_gte)

        _execution_date_lte = d.pop("execution_date_lte", UNSET)
        execution_date_lte: datetime.datetime | Unset
        if isinstance(_execution_date_lte, Unset):
            execution_date_lte = UNSET
        else:
            execution_date_lte = isoparse(_execution_date_lte)

        _start_date_gte = d.pop("start_date_gte", UNSET)
        start_date_gte: datetime.datetime | Unset
        if isinstance(_start_date_gte, Unset):
            start_date_gte = UNSET
        else:
            start_date_gte = isoparse(_start_date_gte)

        _start_date_lte = d.pop("start_date_lte", UNSET)
        start_date_lte: datetime.datetime | Unset
        if isinstance(_start_date_lte, Unset):
            start_date_lte = UNSET
        else:
            start_date_lte = isoparse(_start_date_lte)

        _end_date_gte = d.pop("end_date_gte", UNSET)
        end_date_gte: datetime.datetime | Unset
        if isinstance(_end_date_gte, Unset):
            end_date_gte = UNSET
        else:
            end_date_gte = isoparse(_end_date_gte)

        _end_date_lte = d.pop("end_date_lte", UNSET)
        end_date_lte: datetime.datetime | Unset
        if isinstance(_end_date_lte, Unset):
            end_date_lte = UNSET
        else:
            end_date_lte = isoparse(_end_date_lte)

        list_dag_runs_form = cls(
            order_by=order_by,
            page_offset=page_offset,
            page_limit=page_limit,
            dag_ids=dag_ids,
            states=states,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
        )

        list_dag_runs_form.additional_properties = d
        return list_dag_runs_form

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
