from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_alias_response import AssetAliasResponse
    from ..models.asset_response_extra_type_0 import AssetResponseExtraType0
    from ..models.dag_schedule_asset_reference import DagScheduleAssetReference
    from ..models.last_asset_event_response import LastAssetEventResponse
    from ..models.task_inlet_asset_reference import TaskInletAssetReference
    from ..models.task_outlet_asset_reference import TaskOutletAssetReference


T = TypeVar("T", bound="AssetResponse")


@_attrs_define
class AssetResponse:
    """Asset serializer for responses.

    Attributes:
        id (int):
        name (str):
        uri (str):
        group (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        scheduled_dags (list[DagScheduleAssetReference]):
        producing_tasks (list[TaskOutletAssetReference]):
        consuming_tasks (list[TaskInletAssetReference]):
        aliases (list[AssetAliasResponse]):
        extra (AssetResponseExtraType0 | None | Unset):
        last_asset_event (LastAssetEventResponse | None | Unset):
    """

    id: int
    name: str
    uri: str
    group: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    scheduled_dags: list[DagScheduleAssetReference]
    producing_tasks: list[TaskOutletAssetReference]
    consuming_tasks: list[TaskInletAssetReference]
    aliases: list[AssetAliasResponse]
    extra: AssetResponseExtraType0 | None | Unset = UNSET
    last_asset_event: LastAssetEventResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_response_extra_type_0 import AssetResponseExtraType0
        from ..models.last_asset_event_response import LastAssetEventResponse

        id = self.id

        name = self.name

        uri = self.uri

        group = self.group

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        scheduled_dags = []
        for scheduled_dags_item_data in self.scheduled_dags:
            scheduled_dags_item = scheduled_dags_item_data.to_dict()
            scheduled_dags.append(scheduled_dags_item)

        producing_tasks = []
        for producing_tasks_item_data in self.producing_tasks:
            producing_tasks_item = producing_tasks_item_data.to_dict()
            producing_tasks.append(producing_tasks_item)

        consuming_tasks = []
        for consuming_tasks_item_data in self.consuming_tasks:
            consuming_tasks_item = consuming_tasks_item_data.to_dict()
            consuming_tasks.append(consuming_tasks_item)

        aliases = []
        for aliases_item_data in self.aliases:
            aliases_item = aliases_item_data.to_dict()
            aliases.append(aliases_item)

        extra: dict[str, Any] | None | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, AssetResponseExtraType0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        last_asset_event: dict[str, Any] | None | Unset
        if isinstance(self.last_asset_event, Unset):
            last_asset_event = UNSET
        elif isinstance(self.last_asset_event, LastAssetEventResponse):
            last_asset_event = self.last_asset_event.to_dict()
        else:
            last_asset_event = self.last_asset_event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "uri": uri,
                "group": group,
                "created_at": created_at,
                "updated_at": updated_at,
                "scheduled_dags": scheduled_dags,
                "producing_tasks": producing_tasks,
                "consuming_tasks": consuming_tasks,
                "aliases": aliases,
            }
        )
        if extra is not UNSET:
            field_dict["extra"] = extra
        if last_asset_event is not UNSET:
            field_dict["last_asset_event"] = last_asset_event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_alias_response import AssetAliasResponse
        from ..models.asset_response_extra_type_0 import AssetResponseExtraType0
        from ..models.dag_schedule_asset_reference import DagScheduleAssetReference
        from ..models.last_asset_event_response import LastAssetEventResponse
        from ..models.task_inlet_asset_reference import TaskInletAssetReference
        from ..models.task_outlet_asset_reference import TaskOutletAssetReference

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        uri = d.pop("uri")

        group = d.pop("group")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        scheduled_dags = []
        _scheduled_dags = d.pop("scheduled_dags")
        for scheduled_dags_item_data in _scheduled_dags:
            scheduled_dags_item = DagScheduleAssetReference.from_dict(scheduled_dags_item_data)

            scheduled_dags.append(scheduled_dags_item)

        producing_tasks = []
        _producing_tasks = d.pop("producing_tasks")
        for producing_tasks_item_data in _producing_tasks:
            producing_tasks_item = TaskOutletAssetReference.from_dict(producing_tasks_item_data)

            producing_tasks.append(producing_tasks_item)

        consuming_tasks = []
        _consuming_tasks = d.pop("consuming_tasks")
        for consuming_tasks_item_data in _consuming_tasks:
            consuming_tasks_item = TaskInletAssetReference.from_dict(consuming_tasks_item_data)

            consuming_tasks.append(consuming_tasks_item)

        aliases = []
        _aliases = d.pop("aliases")
        for aliases_item_data in _aliases:
            aliases_item = AssetAliasResponse.from_dict(aliases_item_data)

            aliases.append(aliases_item)

        def _parse_extra(data: object) -> AssetResponseExtraType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0 = AssetResponseExtraType0.from_dict(data)

                return extra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetResponseExtraType0 | None | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_last_asset_event(data: object) -> LastAssetEventResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_asset_event_type_0 = LastAssetEventResponse.from_dict(data)

                return last_asset_event_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LastAssetEventResponse | None | Unset, data)

        last_asset_event = _parse_last_asset_event(d.pop("last_asset_event", UNSET))

        asset_response = cls(
            id=id,
            name=name,
            uri=uri,
            group=group,
            created_at=created_at,
            updated_at=updated_at,
            scheduled_dags=scheduled_dags,
            producing_tasks=producing_tasks,
            consuming_tasks=consuming_tasks,
            aliases=aliases,
            extra=extra,
            last_asset_event=last_asset_event,
        )

        asset_response.additional_properties = d
        return asset_response

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
