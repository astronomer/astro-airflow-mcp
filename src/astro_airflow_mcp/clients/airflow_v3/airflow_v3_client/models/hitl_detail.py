from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hitl_user import HITLUser
    from ..models.params import Params
    from ..models.params_input import ParamsInput
    from ..models.task_instance_response import TaskInstanceResponse


T = TypeVar("T", bound="HITLDetail")


@_attrs_define
class HITLDetail:
    """Schema for Human-in-the-loop detail.

    Attributes:
        task_instance (TaskInstanceResponse): TaskInstance serializer for responses.
        options (list[str]):
        subject (str):
        created_at (datetime.datetime):
        body (None | str | Unset):
        defaults (list[str] | None | Unset):
        multiple (bool | Unset):  Default: False.
        params (Params | Unset):
        assigned_users (list[HITLUser] | Unset):
        responded_by_user (HITLUser | None | Unset):
        responded_at (datetime.datetime | None | Unset):
        chosen_options (list[str] | None | Unset):
        params_input (ParamsInput | Unset):
        response_received (bool | Unset):  Default: False.
    """

    task_instance: TaskInstanceResponse
    options: list[str]
    subject: str
    created_at: datetime.datetime
    body: None | str | Unset = UNSET
    defaults: list[str] | None | Unset = UNSET
    multiple: bool | Unset = False
    params: Params | Unset = UNSET
    assigned_users: list[HITLUser] | Unset = UNSET
    responded_by_user: HITLUser | None | Unset = UNSET
    responded_at: datetime.datetime | None | Unset = UNSET
    chosen_options: list[str] | None | Unset = UNSET
    params_input: ParamsInput | Unset = UNSET
    response_received: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hitl_user import HITLUser

        task_instance = self.task_instance.to_dict()

        options = self.options

        subject = self.subject

        created_at = self.created_at.isoformat()

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        defaults: list[str] | None | Unset
        if isinstance(self.defaults, Unset):
            defaults = UNSET
        elif isinstance(self.defaults, list):
            defaults = self.defaults

        else:
            defaults = self.defaults

        multiple = self.multiple

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        assigned_users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assigned_users, Unset):
            assigned_users = []
            for assigned_users_item_data in self.assigned_users:
                assigned_users_item = assigned_users_item_data.to_dict()
                assigned_users.append(assigned_users_item)

        responded_by_user: dict[str, Any] | None | Unset
        if isinstance(self.responded_by_user, Unset):
            responded_by_user = UNSET
        elif isinstance(self.responded_by_user, HITLUser):
            responded_by_user = self.responded_by_user.to_dict()
        else:
            responded_by_user = self.responded_by_user

        responded_at: None | str | Unset
        if isinstance(self.responded_at, Unset):
            responded_at = UNSET
        elif isinstance(self.responded_at, datetime.datetime):
            responded_at = self.responded_at.isoformat()
        else:
            responded_at = self.responded_at

        chosen_options: list[str] | None | Unset
        if isinstance(self.chosen_options, Unset):
            chosen_options = UNSET
        elif isinstance(self.chosen_options, list):
            chosen_options = self.chosen_options

        else:
            chosen_options = self.chosen_options

        params_input: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params_input, Unset):
            params_input = self.params_input.to_dict()

        response_received = self.response_received

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_instance": task_instance,
                "options": options,
                "subject": subject,
                "created_at": created_at,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if params is not UNSET:
            field_dict["params"] = params
        if assigned_users is not UNSET:
            field_dict["assigned_users"] = assigned_users
        if responded_by_user is not UNSET:
            field_dict["responded_by_user"] = responded_by_user
        if responded_at is not UNSET:
            field_dict["responded_at"] = responded_at
        if chosen_options is not UNSET:
            field_dict["chosen_options"] = chosen_options
        if params_input is not UNSET:
            field_dict["params_input"] = params_input
        if response_received is not UNSET:
            field_dict["response_received"] = response_received

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hitl_user import HITLUser
        from ..models.params import Params
        from ..models.params_input import ParamsInput
        from ..models.task_instance_response import TaskInstanceResponse

        d = dict(src_dict)
        task_instance = TaskInstanceResponse.from_dict(d.pop("task_instance"))

        options = cast(list[str], d.pop("options"))

        subject = d.pop("subject")

        created_at = isoparse(d.pop("created_at"))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_defaults(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                defaults_type_0 = cast(list[str], data)

                return defaults_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        defaults = _parse_defaults(d.pop("defaults", UNSET))

        multiple = d.pop("multiple", UNSET)

        _params = d.pop("params", UNSET)
        params: Params | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = Params.from_dict(_params)

        _assigned_users = d.pop("assigned_users", UNSET)
        assigned_users: list[HITLUser] | Unset = UNSET
        if _assigned_users is not UNSET:
            assigned_users = []
            for assigned_users_item_data in _assigned_users:
                assigned_users_item = HITLUser.from_dict(assigned_users_item_data)

                assigned_users.append(assigned_users_item)

        def _parse_responded_by_user(data: object) -> HITLUser | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                responded_by_user_type_0 = HITLUser.from_dict(data)

                return responded_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HITLUser | None | Unset, data)

        responded_by_user = _parse_responded_by_user(d.pop("responded_by_user", UNSET))

        def _parse_responded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                responded_at_type_0 = isoparse(data)

                return responded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        responded_at = _parse_responded_at(d.pop("responded_at", UNSET))

        def _parse_chosen_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chosen_options_type_0 = cast(list[str], data)

                return chosen_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        chosen_options = _parse_chosen_options(d.pop("chosen_options", UNSET))

        _params_input = d.pop("params_input", UNSET)
        params_input: ParamsInput | Unset
        if isinstance(_params_input, Unset):
            params_input = UNSET
        else:
            params_input = ParamsInput.from_dict(_params_input)

        response_received = d.pop("response_received", UNSET)

        hitl_detail = cls(
            task_instance=task_instance,
            options=options,
            subject=subject,
            created_at=created_at,
            body=body,
            defaults=defaults,
            multiple=multiple,
            params=params,
            assigned_users=assigned_users,
            responded_by_user=responded_by_user,
            responded_at=responded_at,
            chosen_options=chosen_options,
            params_input=params_input,
            response_received=response_received,
        )

        hitl_detail.additional_properties = d
        return hitl_detail

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
