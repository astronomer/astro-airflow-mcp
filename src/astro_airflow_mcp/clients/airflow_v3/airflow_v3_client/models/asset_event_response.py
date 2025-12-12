from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_event_response_extra_type_0 import AssetEventResponseExtraType0
    from ..models.dag_run_asset_reference import DagRunAssetReference


T = TypeVar("T", bound="AssetEventResponse")


@_attrs_define
class AssetEventResponse:
    """Asset event serializer for responses.

    Attributes:
        id (int):
        asset_id (int):
        source_map_index (int):
        created_dagruns (list[DagRunAssetReference]):
        timestamp (datetime.datetime):
        uri (None | str | Unset):
        name (None | str | Unset):
        group (None | str | Unset):
        extra (AssetEventResponseExtraType0 | None | Unset):
        source_task_id (None | str | Unset):
        source_dag_id (None | str | Unset):
        source_run_id (None | str | Unset):
    """

    id: int
    asset_id: int
    source_map_index: int
    created_dagruns: list[DagRunAssetReference]
    timestamp: datetime.datetime
    uri: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    group: None | str | Unset = UNSET
    extra: AssetEventResponseExtraType0 | None | Unset = UNSET
    source_task_id: None | str | Unset = UNSET
    source_dag_id: None | str | Unset = UNSET
    source_run_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_event_response_extra_type_0 import AssetEventResponseExtraType0

        id = self.id

        asset_id = self.asset_id

        source_map_index = self.source_map_index

        created_dagruns = []
        for created_dagruns_item_data in self.created_dagruns:
            created_dagruns_item = created_dagruns_item_data.to_dict()
            created_dagruns.append(created_dagruns_item)

        timestamp = self.timestamp.isoformat()

        uri: None | str | Unset
        if isinstance(self.uri, Unset):
            uri = UNSET
        else:
            uri = self.uri

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        extra: dict[str, Any] | None | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, AssetEventResponseExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        source_task_id: None | str | Unset
        if isinstance(self.source_task_id, Unset):
            source_task_id = UNSET
        else:
            source_task_id = self.source_task_id

        source_dag_id: None | str | Unset
        if isinstance(self.source_dag_id, Unset):
            source_dag_id = UNSET
        else:
            source_dag_id = self.source_dag_id

        source_run_id: None | str | Unset
        if isinstance(self.source_run_id, Unset):
            source_run_id = UNSET
        else:
            source_run_id = self.source_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "asset_id": asset_id,
                "source_map_index": source_map_index,
                "created_dagruns": created_dagruns,
                "timestamp": timestamp,
            }
        )
        if uri is not UNSET:
            field_dict["uri"] = uri
        if name is not UNSET:
            field_dict["name"] = name
        if group is not UNSET:
            field_dict["group"] = group
        if extra is not UNSET:
            field_dict["extra"] = extra
        if source_task_id is not UNSET:
            field_dict["source_task_id"] = source_task_id
        if source_dag_id is not UNSET:
            field_dict["source_dag_id"] = source_dag_id
        if source_run_id is not UNSET:
            field_dict["source_run_id"] = source_run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_event_response_extra_type_0 import AssetEventResponseExtraType0
        from ..models.dag_run_asset_reference import DagRunAssetReference

        d = dict(src_dict)
        id = d.pop("id")

        asset_id = d.pop("asset_id")

        source_map_index = d.pop("source_map_index")

        created_dagruns = []
        _created_dagruns = d.pop("created_dagruns")
        for created_dagruns_item_data in _created_dagruns:
            created_dagruns_item = DagRunAssetReference.from_dict(created_dagruns_item_data)

            created_dagruns.append(created_dagruns_item)

        timestamp = isoparse(d.pop("timestamp"))

        def _parse_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri = _parse_uri(d.pop("uri", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_extra(data: object) -> AssetEventResponseExtraType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = AssetEventResponseExtraType0.from_dict(data)

                return extra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetEventResponseExtraType0 | None | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_source_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_task_id = _parse_source_task_id(d.pop("source_task_id", UNSET))

        def _parse_source_dag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_dag_id = _parse_source_dag_id(d.pop("source_dag_id", UNSET))

        def _parse_source_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_run_id = _parse_source_run_id(d.pop("source_run_id", UNSET))

        asset_event_response = cls(
            id=id,
            asset_id=asset_id,
            source_map_index=source_map_index,
            created_dagruns=created_dagruns,
            timestamp=timestamp,
            uri=uri,
            name=name,
            group=group,
            extra=extra,
            source_task_id=source_task_id,
            source_dag_id=source_dag_id,
            source_run_id=source_run_id,
        )

        asset_event_response.additional_properties = d
        return asset_event_response

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
