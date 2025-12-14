from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DagVersionResponse")


@_attrs_define
class DagVersionResponse:
    """Dag Version serializer for responses.

    Attributes:
        id (UUID):
        version_number (int):
        dag_id (str):
        bundle_name (None | str):
        bundle_version (None | str):
        created_at (datetime.datetime):
        dag_display_name (str):
        bundle_url (None | str):
    """

    id: UUID
    version_number: int
    dag_id: str
    bundle_name: None | str
    bundle_version: None | str
    created_at: datetime.datetime
    dag_display_name: str
    bundle_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        version_number = self.version_number

        dag_id = self.dag_id

        bundle_name: None | str
        bundle_name = self.bundle_name

        bundle_version: None | str
        bundle_version = self.bundle_version

        created_at = self.created_at.isoformat()

        dag_display_name = self.dag_display_name

        bundle_url: None | str
        bundle_url = self.bundle_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version_number": version_number,
                "dag_id": dag_id,
                "bundle_name": bundle_name,
                "bundle_version": bundle_version,
                "created_at": created_at,
                "dag_display_name": dag_display_name,
                "bundle_url": bundle_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        version_number = d.pop("version_number")

        dag_id = d.pop("dag_id")

        def _parse_bundle_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_name = _parse_bundle_name(d.pop("bundle_name"))

        def _parse_bundle_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_version = _parse_bundle_version(d.pop("bundle_version"))

        created_at = isoparse(d.pop("created_at"))

        dag_display_name = d.pop("dag_display_name")

        def _parse_bundle_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bundle_url = _parse_bundle_url(d.pop("bundle_url"))

        dag_version_response = cls(
            id=id,
            version_number=version_number,
            dag_id=dag_id,
            bundle_name=bundle_name,
            bundle_version=bundle_version,
            created_at=created_at,
            dag_display_name=dag_display_name,
            bundle_url=bundle_url,
        )

        dag_version_response.additional_properties = d
        return dag_version_response

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
