from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DAGPatchBody")


@_attrs_define
class DAGPatchBody:
    """Dag Serializer for updatable bodies.

    Attributes:
        is_paused (bool):
    """

    is_paused: bool

    def to_dict(self) -> dict[str, Any]:
        is_paused = self.is_paused

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "is_paused": is_paused,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_paused = d.pop("is_paused")

        dag_patch_body = cls(
            is_paused=is_paused,
        )

        return dag_patch_body
