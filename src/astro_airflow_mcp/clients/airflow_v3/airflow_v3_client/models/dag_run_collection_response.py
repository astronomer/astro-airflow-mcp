from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dag_run_response import DAGRunResponse


T = TypeVar("T", bound="DAGRunCollectionResponse")


@_attrs_define
class DAGRunCollectionResponse:
    """DAG Run Collection serializer for responses.

    Attributes:
        dag_runs (list[DAGRunResponse]):
        total_entries (int):
    """

    dag_runs: list[DAGRunResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dag_runs = []
        for dag_runs_item_data in self.dag_runs:
            dag_runs_item = dag_runs_item_data.to_dict()
            dag_runs.append(dag_runs_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_runs": dag_runs,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_run_response import DAGRunResponse

        d = dict(src_dict)
        dag_runs = []
        _dag_runs = d.pop("dag_runs")
        for dag_runs_item_data in _dag_runs:
            dag_runs_item = DAGRunResponse.from_dict(dag_runs_item_data)

            dag_runs.append(dag_runs_item)

        total_entries = d.pop("total_entries")

        dag_run_collection_response = cls(
            dag_runs=dag_runs,
            total_entries=total_entries,
        )

        dag_run_collection_response.additional_properties = d
        return dag_run_collection_response

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
