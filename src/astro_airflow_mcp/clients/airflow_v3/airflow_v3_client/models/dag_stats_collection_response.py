from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dag_stats_response import DagStatsResponse


T = TypeVar("T", bound="DagStatsCollectionResponse")


@_attrs_define
class DagStatsCollectionResponse:
    """DAG Stats Collection serializer for responses.

    Attributes:
        dags (list[DagStatsResponse]):
        total_entries (int):
    """

    dags: list[DagStatsResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dags = []
        for dags_item_data in self.dags:
            dags_item = dags_item_data.to_dict()
            dags.append(dags_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dags": dags,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_stats_response import DagStatsResponse

        d = dict(src_dict)
        dags = []
        _dags = d.pop("dags")
        for dags_item_data in _dags:
            dags_item = DagStatsResponse.from_dict(dags_item_data)

            dags.append(dags_item)

        total_entries = d.pop("total_entries")

        dag_stats_collection_response = cls(
            dags=dags,
            total_entries=total_entries,
        )

        dag_stats_collection_response.additional_properties = d
        return dag_stats_collection_response

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
