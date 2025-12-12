from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag import DAG


T = TypeVar("T", bound="DAGCollection")


@_attrs_define
class DAGCollection:
    """Collection of DAGs.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.

        Attributes:
            total_entries (int | Unset): Count of total objects in the current result set before pagination parameters
                (limit, offset) are applied.
            dags (list[DAG] | Unset):
    """

    total_entries: int | Unset = UNSET
    dags: list[DAG] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_entries = self.total_entries

        dags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dags, Unset):
            dags = []
            for dags_item_data in self.dags:
                dags_item = dags_item_data.to_dict()
                dags.append(dags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if dags is not UNSET:
            field_dict["dags"] = dags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag import DAG

        d = dict(src_dict)
        total_entries = d.pop("total_entries", UNSET)

        _dags = d.pop("dags", UNSET)
        dags: list[DAG] | Unset = UNSET
        if _dags is not UNSET:
            dags = []
            for dags_item_data in _dags:
                dags_item = DAG.from_dict(dags_item_data)

                dags.append(dags_item)

        dag_collection = cls(
            total_entries=total_entries,
            dags=dags,
        )

        dag_collection.additional_properties = d
        return dag_collection

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
