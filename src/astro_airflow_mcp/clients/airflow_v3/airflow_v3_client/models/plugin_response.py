from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_builder_menu_item_response import AppBuilderMenuItemResponse
    from ..models.app_builder_view_response import AppBuilderViewResponse
    from ..models.external_view_response import ExternalViewResponse
    from ..models.fast_api_app_response import FastAPIAppResponse
    from ..models.fast_api_root_middleware_response import FastAPIRootMiddlewareResponse
    from ..models.react_app_response import ReactAppResponse


T = TypeVar("T", bound="PluginResponse")


@_attrs_define
class PluginResponse:
    """Plugin serializer.

    Attributes:
        name (str):
        macros (list[str]):
        flask_blueprints (list[str]):
        fastapi_apps (list[FastAPIAppResponse]):
        fastapi_root_middlewares (list[FastAPIRootMiddlewareResponse]):
        external_views (list[ExternalViewResponse]): Aggregate all external views. Both 'external_views' and
            'appbuilder_menu_items' are included here.
        react_apps (list[ReactAppResponse]):
        appbuilder_views (list[AppBuilderViewResponse]):
        appbuilder_menu_items (list[AppBuilderMenuItemResponse]):
        global_operator_extra_links (list[str]):
        operator_extra_links (list[str]):
        source (str):
        listeners (list[str]):
        timetables (list[str]):
    """

    name: str
    macros: list[str]
    flask_blueprints: list[str]
    fastapi_apps: list[FastAPIAppResponse]
    fastapi_root_middlewares: list[FastAPIRootMiddlewareResponse]
    external_views: list[ExternalViewResponse]
    react_apps: list[ReactAppResponse]
    appbuilder_views: list[AppBuilderViewResponse]
    appbuilder_menu_items: list[AppBuilderMenuItemResponse]
    global_operator_extra_links: list[str]
    operator_extra_links: list[str]
    source: str
    listeners: list[str]
    timetables: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        macros = self.macros

        flask_blueprints = self.flask_blueprints

        fastapi_apps = []
        for fastapi_apps_item_data in self.fastapi_apps:
            fastapi_apps_item = fastapi_apps_item_data.to_dict()
            fastapi_apps.append(fastapi_apps_item)

        fastapi_root_middlewares = []
        for fastapi_root_middlewares_item_data in self.fastapi_root_middlewares:
            fastapi_root_middlewares_item = fastapi_root_middlewares_item_data.to_dict()
            fastapi_root_middlewares.append(fastapi_root_middlewares_item)

        external_views = []
        for external_views_item_data in self.external_views:
            external_views_item = external_views_item_data.to_dict()
            external_views.append(external_views_item)

        react_apps = []
        for react_apps_item_data in self.react_apps:
            react_apps_item = react_apps_item_data.to_dict()
            react_apps.append(react_apps_item)

        appbuilder_views = []
        for appbuilder_views_item_data in self.appbuilder_views:
            appbuilder_views_item = appbuilder_views_item_data.to_dict()
            appbuilder_views.append(appbuilder_views_item)

        appbuilder_menu_items = []
        for appbuilder_menu_items_item_data in self.appbuilder_menu_items:
            appbuilder_menu_items_item = appbuilder_menu_items_item_data.to_dict()
            appbuilder_menu_items.append(appbuilder_menu_items_item)

        global_operator_extra_links = self.global_operator_extra_links

        operator_extra_links = self.operator_extra_links

        source = self.source

        listeners = self.listeners

        timetables = self.timetables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "macros": macros,
                "flask_blueprints": flask_blueprints,
                "fastapi_apps": fastapi_apps,
                "fastapi_root_middlewares": fastapi_root_middlewares,
                "external_views": external_views,
                "react_apps": react_apps,
                "appbuilder_views": appbuilder_views,
                "appbuilder_menu_items": appbuilder_menu_items,
                "global_operator_extra_links": global_operator_extra_links,
                "operator_extra_links": operator_extra_links,
                "source": source,
                "listeners": listeners,
                "timetables": timetables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_builder_menu_item_response import AppBuilderMenuItemResponse
        from ..models.app_builder_view_response import AppBuilderViewResponse
        from ..models.external_view_response import ExternalViewResponse
        from ..models.fast_api_app_response import FastAPIAppResponse
        from ..models.fast_api_root_middleware_response import FastAPIRootMiddlewareResponse
        from ..models.react_app_response import ReactAppResponse

        d = dict(src_dict)
        name = d.pop("name")

        macros = cast(list[str], d.pop("macros"))

        flask_blueprints = cast(list[str], d.pop("flask_blueprints"))

        fastapi_apps = []
        _fastapi_apps = d.pop("fastapi_apps")
        for fastapi_apps_item_data in _fastapi_apps:
            fastapi_apps_item = FastAPIAppResponse.from_dict(fastapi_apps_item_data)

            fastapi_apps.append(fastapi_apps_item)

        fastapi_root_middlewares = []
        _fastapi_root_middlewares = d.pop("fastapi_root_middlewares")
        for fastapi_root_middlewares_item_data in _fastapi_root_middlewares:
            fastapi_root_middlewares_item = FastAPIRootMiddlewareResponse.from_dict(fastapi_root_middlewares_item_data)

            fastapi_root_middlewares.append(fastapi_root_middlewares_item)

        external_views = []
        _external_views = d.pop("external_views")
        for external_views_item_data in _external_views:
            external_views_item = ExternalViewResponse.from_dict(external_views_item_data)

            external_views.append(external_views_item)

        react_apps = []
        _react_apps = d.pop("react_apps")
        for react_apps_item_data in _react_apps:
            react_apps_item = ReactAppResponse.from_dict(react_apps_item_data)

            react_apps.append(react_apps_item)

        appbuilder_views = []
        _appbuilder_views = d.pop("appbuilder_views")
        for appbuilder_views_item_data in _appbuilder_views:
            appbuilder_views_item = AppBuilderViewResponse.from_dict(appbuilder_views_item_data)

            appbuilder_views.append(appbuilder_views_item)

        appbuilder_menu_items = []
        _appbuilder_menu_items = d.pop("appbuilder_menu_items")
        for appbuilder_menu_items_item_data in _appbuilder_menu_items:
            appbuilder_menu_items_item = AppBuilderMenuItemResponse.from_dict(appbuilder_menu_items_item_data)

            appbuilder_menu_items.append(appbuilder_menu_items_item)

        global_operator_extra_links = cast(list[str], d.pop("global_operator_extra_links"))

        operator_extra_links = cast(list[str], d.pop("operator_extra_links"))

        source = d.pop("source")

        listeners = cast(list[str], d.pop("listeners"))

        timetables = cast(list[str], d.pop("timetables"))

        plugin_response = cls(
            name=name,
            macros=macros,
            flask_blueprints=flask_blueprints,
            fastapi_apps=fastapi_apps,
            fastapi_root_middlewares=fastapi_root_middlewares,
            external_views=external_views,
            react_apps=react_apps,
            appbuilder_views=appbuilder_views,
            appbuilder_menu_items=appbuilder_menu_items,
            global_operator_extra_links=global_operator_extra_links,
            operator_extra_links=operator_extra_links,
            source=source,
            listeners=listeners,
            timetables=timetables,
        )

        plugin_response.additional_properties = d
        return plugin_response

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
