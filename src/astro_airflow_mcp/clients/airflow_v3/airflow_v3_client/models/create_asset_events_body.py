from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extra import Extra


T = TypeVar("T", bound="CreateAssetEventsBody")


@_attrs_define
class CreateAssetEventsBody:
    """Create asset events request.

    Attributes:
        asset_id (int):
        extra (Extra | Unset):
    """

    asset_id: int
    extra: Extra | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra, Unset):
            extra = self.extra.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if extra is not UNSET:
            field_dict["extra"] = extra

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extra import Extra

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        _extra = d.pop("extra", UNSET)
        extra: Extra | Unset
        if isinstance(_extra, Unset):
            extra = UNSET
        else:
            extra = Extra.from_dict(_extra)

        create_asset_events_body = cls(
            asset_id=asset_id,
            extra=extra,
        )

        return create_asset_events_body
