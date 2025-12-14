from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="DagScheduleAssetReference")


@_attrs_define
class DagScheduleAssetReference:
    """DAG schedule reference serializer for assets.

    Attributes:
        dag_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    dag_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        dag_id = self.dag_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dag_id": dag_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        dag_schedule_asset_reference = cls(
            dag_id=dag_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        return dag_schedule_asset_reference
