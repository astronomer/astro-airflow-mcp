from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DAGRunClearBody")


@_attrs_define
class DAGRunClearBody:
    """DAG Run serializer for clear endpoint body.

    Attributes:
        dry_run (bool | Unset):  Default: True.
        only_failed (bool | Unset):  Default: False.
        run_on_latest_version (bool | Unset): (Experimental) Run on the latest bundle version of the Dag after clearing
            the Dag Run. Default: False.
    """

    dry_run: bool | Unset = True
    only_failed: bool | Unset = False
    run_on_latest_version: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        only_failed = self.only_failed

        run_on_latest_version = self.run_on_latest_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if only_failed is not UNSET:
            field_dict["only_failed"] = only_failed
        if run_on_latest_version is not UNSET:
            field_dict["run_on_latest_version"] = run_on_latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        only_failed = d.pop("only_failed", UNSET)

        run_on_latest_version = d.pop("run_on_latest_version", UNSET)

        dag_run_clear_body = cls(
            dry_run=dry_run,
            only_failed=only_failed,
            run_on_latest_version=run_on_latest_version,
        )

        return dag_run_clear_body
