from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_view_response_destination import ExternalViewResponseDestination
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalViewResponse")


@_attrs_define
class ExternalViewResponse:
    """Serializer for External View Plugin responses.

    Attributes:
        name (str):
        href (str):
        icon (None | str | Unset):
        icon_dark_mode (None | str | Unset):
        url_route (None | str | Unset):
        category (None | str | Unset):
        destination (ExternalViewResponseDestination | Unset):  Default: ExternalViewResponseDestination.NAV.
    """

    name: str
    href: str
    icon: None | str | Unset = UNSET
    icon_dark_mode: None | str | Unset = UNSET
    url_route: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    destination: ExternalViewResponseDestination | Unset = ExternalViewResponseDestination.NAV
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        href = self.href

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        icon_dark_mode: None | str | Unset
        if isinstance(self.icon_dark_mode, Unset):
            icon_dark_mode = UNSET
        else:
            icon_dark_mode = self.icon_dark_mode

        url_route: None | str | Unset
        if isinstance(self.url_route, Unset):
            url_route = UNSET
        else:
            url_route = self.url_route

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        destination: str | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "href": href,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_dark_mode is not UNSET:
            field_dict["icon_dark_mode"] = icon_dark_mode
        if url_route is not UNSET:
            field_dict["url_route"] = url_route
        if category is not UNSET:
            field_dict["category"] = category
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        href = d.pop("href")

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_icon_dark_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_dark_mode = _parse_icon_dark_mode(d.pop("icon_dark_mode", UNSET))

        def _parse_url_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_route = _parse_url_route(d.pop("url_route", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        _destination = d.pop("destination", UNSET)
        destination: ExternalViewResponseDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = ExternalViewResponseDestination(_destination)

        external_view_response = cls(
            name=name,
            href=href,
            icon=icon,
            icon_dark_mode=icon_dark_mode,
            url_route=url_route,
            category=category,
            destination=destination,
        )

        external_view_response.additional_properties = d
        return external_view_response

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
