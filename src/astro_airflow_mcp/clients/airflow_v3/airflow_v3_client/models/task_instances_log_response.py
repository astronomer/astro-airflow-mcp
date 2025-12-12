from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.structured_log_message import StructuredLogMessage


T = TypeVar("T", bound="TaskInstancesLogResponse")


@_attrs_define
class TaskInstancesLogResponse:
    """Log serializer for responses.

    Attributes:
        content (list[str] | list[StructuredLogMessage]):
        continuation_token (None | str):
    """

    content: list[str] | list[StructuredLogMessage]
    continuation_token: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | list[str]
        if isinstance(self.content, list):
            content = []
            for content_type_0_item_data in self.content:
                content_type_0_item = content_type_0_item_data.to_dict()
                content.append(content_type_0_item)

        else:
            content = self.content

        continuation_token: None | str
        continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "continuation_token": continuation_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_log_message import StructuredLogMessage

        d = dict(src_dict)

        def _parse_content(data: object) -> list[str] | list[StructuredLogMessage]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_0 = []
                _content_type_0 = data
                for content_type_0_item_data in _content_type_0:
                    content_type_0_item = StructuredLogMessage.from_dict(content_type_0_item_data)

                    content_type_0.append(content_type_0_item)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            content_type_1 = cast(list[str], data)

            return content_type_1

        content = _parse_content(d.pop("content"))

        def _parse_continuation_token(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token"))

        task_instances_log_response = cls(
            content=content,
            continuation_token=continuation_token,
        )

        task_instances_log_response.additional_properties = d
        return task_instances_log_response

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
