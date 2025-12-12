from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pool_response import PoolResponse


T = TypeVar("T", bound="PoolCollectionResponse")


@_attrs_define
class PoolCollectionResponse:
    """Pool Collection serializer for responses.

    Attributes:
        pools (list[PoolResponse]):
        total_entries (int):
    """

    pools: list[PoolResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pools": pools,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_response import PoolResponse

        d = dict(src_dict)
        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = PoolResponse.from_dict(pools_item_data)

            pools.append(pools_item)

        total_entries = d.pop("total_entries")

        pool_collection_response = cls(
            pools=pools,
            total_entries=total_entries,
        )

        pool_collection_response.additional_properties = d
        return pool_collection_response

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
