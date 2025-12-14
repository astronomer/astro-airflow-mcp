from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_run import DAGRun


T = TypeVar("T", bound="DAGRunCollection")


@_attrs_define
class DAGRunCollection:
    """Collection of DAG runs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            dag_runs (list[DAGRun] | Unset):
    """

    total_entries: int | Unset = UNSET
    dag_runs: list[DAGRun] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        dag_runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dag_runs, Unset):
            dag_runs = []
            for dag_runs_item_data in self.dag_runs:
                dag_runs_item = dag_runs_item_data.to_dict()
                dag_runs.append(dag_runs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if dag_runs is not UNSET:
            field_dict["dag_runs"] = dag_runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_run import DAGRun

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _dag_runs = d.pop("dag_runs", UNSET)
        dag_runs: list[DAGRun] | Unset = UNSET
        if _dag_runs is not UNSET:
            dag_runs = []
            for dag_runs_item_data in _dag_runs:
                dag_runs_item = DAGRun.from_dict(dag_runs_item_data)

                dag_runs.append(dag_runs_item)

        dag_run_collection = cls(
            total_entries=total_entries,
            dag_runs=dag_runs,
        )

        dag_run_collection.additional_properties = d
        return dag_run_collection

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
