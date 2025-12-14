from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dry_run_backfill_response import DryRunBackfillResponse


T = TypeVar("T", bound="DryRunBackfillCollectionResponse")


@_attrs_define
class DryRunBackfillCollectionResponse:
    """Backfill collection serializer for responses in dry-run mode.

    Attributes:
        backfills (list[DryRunBackfillResponse]):
        total_entries (int):
    """

    backfills: list[DryRunBackfillResponse]
    total_entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backfills = []
        for backfills_item_data in self.backfills:
            backfills_item = backfills_item_data.to_dict()
            backfills.append(backfills_item)

        total_entries = self.total_entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backfills": backfills,
                "total_entries": total_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dry_run_backfill_response import DryRunBackfillResponse

        d = dict(src_dict)
        backfills = []
        _backfills = d.pop("backfills")
        for backfills_item_data in _backfills:
            backfills_item = DryRunBackfillResponse.from_dict(backfills_item_data)

            backfills.append(backfills_item)

        total_entries = d.pop("total_entries")

        dry_run_backfill_collection_response = cls(
            backfills=backfills,
            total_entries=total_entries,
        )

        dry_run_backfill_collection_response.additional_properties = d
        return dry_run_backfill_collection_response

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
