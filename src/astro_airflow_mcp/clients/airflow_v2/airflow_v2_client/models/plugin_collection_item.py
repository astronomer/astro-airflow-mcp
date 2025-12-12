from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_collection_item_appbuilder_menu_items_item_type_0 import (
        PluginCollectionItemAppbuilderMenuItemsItemType0,
    )
    from ..models.plugin_collection_item_appbuilder_views_item_type_0 import (
        PluginCollectionItemAppbuilderViewsItemType0,
    )


T = TypeVar("T", bound="PluginCollectionItem")


@_attrs_define
class PluginCollectionItem:
    """A plugin Item.

    *New in version 2.1.0*

        Attributes:
            name (str | Unset): The name of the plugin
            hooks (list[None | str] | Unset): The plugin hooks
            executors (list[None | str] | Unset): The plugin executors
            macros (list[None | str] | Unset): The plugin macros
            flask_blueprints (list[None | str] | Unset): The flask blueprints
            appbuilder_views (list[None | PluginCollectionItemAppbuilderViewsItemType0] | Unset): The appuilder views
            appbuilder_menu_items (list[None | PluginCollectionItemAppbuilderMenuItemsItemType0] | Unset): The Flask
                Appbuilder menu items
            global_operator_extra_links (list[None | str] | Unset): The global operator extra links
            operator_extra_links (list[None | str] | Unset): Operator extra links
            source (None | str | Unset): The plugin source
            ti_deps (list[str] | Unset): The plugin task instance dependencies
            listeners (list[str] | Unset): The plugin listeners
            timetables (list[str] | Unset): The plugin timetables
    """

    name: str | Unset = UNSET
    hooks: list[None | str] | Unset = UNSET
    executors: list[None | str] | Unset = UNSET
    macros: list[None | str] | Unset = UNSET
    flask_blueprints: list[None | str] | Unset = UNSET
    appbuilder_views: list[None | PluginCollectionItemAppbuilderViewsItemType0] | Unset = UNSET
    appbuilder_menu_items: list[None | PluginCollectionItemAppbuilderMenuItemsItemType0] | Unset = UNSET
    global_operator_extra_links: list[None | str] | Unset = UNSET
    operator_extra_links: list[None | str] | Unset = UNSET
    source: None | str | Unset = UNSET
    ti_deps: list[str] | Unset = UNSET
    listeners: list[str] | Unset = UNSET
    timetables: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_collection_item_appbuilder_menu_items_item_type_0 import (
            PluginCollectionItemAppbuilderMenuItemsItemType0,
        )
        from ..models.plugin_collection_item_appbuilder_views_item_type_0 import (
            PluginCollectionItemAppbuilderViewsItemType0,
        )

        name = self.name

        hooks: list[None | str] | Unset = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = []
            for hooks_item_data in self.hooks:
                hooks_item: None | str
                hooks_item = hooks_item_data
                hooks.append(hooks_item)

        executors: list[None | str] | Unset = UNSET
        if not isinstance(self.executors, Unset):
            executors = []
            for executors_item_data in self.executors:
                executors_item: None | str
                executors_item = executors_item_data
                executors.append(executors_item)

        macros: list[None | str] | Unset = UNSET
        if not isinstance(self.macros, Unset):
            macros = []
            for macros_item_data in self.macros:
                macros_item: None | str
                macros_item = macros_item_data
                macros.append(macros_item)

        flask_blueprints: list[None | str] | Unset = UNSET
        if not isinstance(self.flask_blueprints, Unset):
            flask_blueprints = []
            for flask_blueprints_item_data in self.flask_blueprints:
                flask_blueprints_item: None | str
                flask_blueprints_item = flask_blueprints_item_data
                flask_blueprints.append(flask_blueprints_item)

        appbuilder_views: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.appbuilder_views, Unset):
            appbuilder_views = []
            for appbuilder_views_item_data in self.appbuilder_views:
                appbuilder_views_item: dict[str, Any] | None
                if isinstance(appbuilder_views_item_data, PluginCollectionItemAppbuilderViewsItemType0):
                    appbuilder_views_item = appbuilder_views_item_data.to_dict()
                else:
                    appbuilder_views_item = appbuilder_views_item_data
                appbuilder_views.append(appbuilder_views_item)

        appbuilder_menu_items: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.appbuilder_menu_items, Unset):
            appbuilder_menu_items = []
            for appbuilder_menu_items_item_data in self.appbuilder_menu_items:
                appbuilder_menu_items_item: dict[str, Any] | None
                if isinstance(appbuilder_menu_items_item_data, PluginCollectionItemAppbuilderMenuItemsItemType0):
                    appbuilder_menu_items_item = appbuilder_menu_items_item_data.to_dict()
                else:
                    appbuilder_menu_items_item = appbuilder_menu_items_item_data
                appbuilder_menu_items.append(appbuilder_menu_items_item)

        global_operator_extra_links: list[None | str] | Unset = UNSET
        if not isinstance(self.global_operator_extra_links, Unset):
            global_operator_extra_links = []
            for global_operator_extra_links_item_data in self.global_operator_extra_links:
                global_operator_extra_links_item: None | str
                global_operator_extra_links_item = global_operator_extra_links_item_data
                global_operator_extra_links.append(global_operator_extra_links_item)

        operator_extra_links: list[None | str] | Unset = UNSET
        if not isinstance(self.operator_extra_links, Unset):
            operator_extra_links = []
            for operator_extra_links_item_data in self.operator_extra_links:
                operator_extra_links_item: None | str
                operator_extra_links_item = operator_extra_links_item_data
                operator_extra_links.append(operator_extra_links_item)

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        ti_deps: list[str] | Unset = UNSET
        if not isinstance(self.ti_deps, Unset):
            ti_deps = self.ti_deps

        listeners: list[str] | Unset = UNSET
        if not isinstance(self.listeners, Unset):
            listeners = self.listeners

        timetables: list[str] | Unset = UNSET
        if not isinstance(self.timetables, Unset):
            timetables = self.timetables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if executors is not UNSET:
            field_dict["executors"] = executors
        if macros is not UNSET:
            field_dict["macros"] = macros
        if flask_blueprints is not UNSET:
            field_dict["flask_blueprints"] = flask_blueprints
        if appbuilder_views is not UNSET:
            field_dict["appbuilder_views"] = appbuilder_views
        if appbuilder_menu_items is not UNSET:
            field_dict["appbuilder_menu_items"] = appbuilder_menu_items
        if global_operator_extra_links is not UNSET:
            field_dict["global_operator_extra_links"] = global_operator_extra_links
        if operator_extra_links is not UNSET:
            field_dict["operator_extra_links"] = operator_extra_links
        if source is not UNSET:
            field_dict["source"] = source
        if ti_deps is not UNSET:
            field_dict["ti_deps"] = ti_deps
        if listeners is not UNSET:
            field_dict["listeners"] = listeners
        if timetables is not UNSET:
            field_dict["timetables"] = timetables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_collection_item_appbuilder_menu_items_item_type_0 import (
            PluginCollectionItemAppbuilderMenuItemsItemType0,
        )
        from ..models.plugin_collection_item_appbuilder_views_item_type_0 import (
            PluginCollectionItemAppbuilderViewsItemType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _hooks = d.pop("hooks", UNSET)
        hooks: list[None | str] | Unset = UNSET
        if _hooks is not UNSET:
            hooks = []
            for hooks_item_data in _hooks:

                def _parse_hooks_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                hooks_item = _parse_hooks_item(hooks_item_data)

                hooks.append(hooks_item)

        _executors = d.pop("executors", UNSET)
        executors: list[None | str] | Unset = UNSET
        if _executors is not UNSET:
            executors = []
            for executors_item_data in _executors:

                def _parse_executors_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                executors_item = _parse_executors_item(executors_item_data)

                executors.append(executors_item)

        _macros = d.pop("macros", UNSET)
        macros: list[None | str] | Unset = UNSET
        if _macros is not UNSET:
            macros = []
            for macros_item_data in _macros:

                def _parse_macros_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                macros_item = _parse_macros_item(macros_item_data)

                macros.append(macros_item)

        _flask_blueprints = d.pop("flask_blueprints", UNSET)
        flask_blueprints: list[None | str] | Unset = UNSET
        if _flask_blueprints is not UNSET:
            flask_blueprints = []
            for flask_blueprints_item_data in _flask_blueprints:

                def _parse_flask_blueprints_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                flask_blueprints_item = _parse_flask_blueprints_item(flask_blueprints_item_data)

                flask_blueprints.append(flask_blueprints_item)

        _appbuilder_views = d.pop("appbuilder_views", UNSET)
        appbuilder_views: list[None | PluginCollectionItemAppbuilderViewsItemType0] | Unset = UNSET
        if _appbuilder_views is not UNSET:
            appbuilder_views = []
            for appbuilder_views_item_data in _appbuilder_views:

                def _parse_appbuilder_views_item(data: object) -> None | PluginCollectionItemAppbuilderViewsItemType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        appbuilder_views_item_type_0 = PluginCollectionItemAppbuilderViewsItemType0.from_dict(data)

                        return appbuilder_views_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | PluginCollectionItemAppbuilderViewsItemType0, data)

                appbuilder_views_item = _parse_appbuilder_views_item(appbuilder_views_item_data)

                appbuilder_views.append(appbuilder_views_item)

        _appbuilder_menu_items = d.pop("appbuilder_menu_items", UNSET)
        appbuilder_menu_items: list[None | PluginCollectionItemAppbuilderMenuItemsItemType0] | Unset = UNSET
        if _appbuilder_menu_items is not UNSET:
            appbuilder_menu_items = []
            for appbuilder_menu_items_item_data in _appbuilder_menu_items:

                def _parse_appbuilder_menu_items_item(
                    data: object,
                ) -> None | PluginCollectionItemAppbuilderMenuItemsItemType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        appbuilder_menu_items_item_type_0 = PluginCollectionItemAppbuilderMenuItemsItemType0.from_dict(
                            data
                        )

                        return appbuilder_menu_items_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | PluginCollectionItemAppbuilderMenuItemsItemType0, data)

                appbuilder_menu_items_item = _parse_appbuilder_menu_items_item(appbuilder_menu_items_item_data)

                appbuilder_menu_items.append(appbuilder_menu_items_item)

        _global_operator_extra_links = d.pop("global_operator_extra_links", UNSET)
        global_operator_extra_links: list[None | str] | Unset = UNSET
        if _global_operator_extra_links is not UNSET:
            global_operator_extra_links = []
            for global_operator_extra_links_item_data in _global_operator_extra_links:

                def _parse_global_operator_extra_links_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                global_operator_extra_links_item = _parse_global_operator_extra_links_item(
                    global_operator_extra_links_item_data
                )

                global_operator_extra_links.append(global_operator_extra_links_item)

        _operator_extra_links = d.pop("operator_extra_links", UNSET)
        operator_extra_links: list[None | str] | Unset = UNSET
        if _operator_extra_links is not UNSET:
            operator_extra_links = []
            for operator_extra_links_item_data in _operator_extra_links:

                def _parse_operator_extra_links_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                operator_extra_links_item = _parse_operator_extra_links_item(operator_extra_links_item_data)

                operator_extra_links.append(operator_extra_links_item)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        ti_deps = cast(list[str], d.pop("ti_deps", UNSET))

        listeners = cast(list[str], d.pop("listeners", UNSET))

        timetables = cast(list[str], d.pop("timetables", UNSET))

        plugin_collection_item = cls(
            name=name,
            hooks=hooks,
            executors=executors,
            macros=macros,
            flask_blueprints=flask_blueprints,
            appbuilder_views=appbuilder_views,
            appbuilder_menu_items=appbuilder_menu_items,
            global_operator_extra_links=global_operator_extra_links,
            operator_extra_links=operator_extra_links,
            source=source,
            ti_deps=ti_deps,
            listeners=listeners,
            timetables=timetables,
        )

        plugin_collection_item.additional_properties = d
        return plugin_collection_item

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
