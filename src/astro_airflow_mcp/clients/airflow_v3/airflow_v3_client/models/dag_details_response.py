from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dag_details_response_asset_expression_type_0 import DAGDetailsResponseAssetExpressionType0
    from ..models.dag_details_response_default_args_type_0 import DAGDetailsResponseDefaultArgsType0
    from ..models.dag_details_response_owner_links_type_0 import DAGDetailsResponseOwnerLinksType0
    from ..models.dag_details_response_params_type_0 import DAGDetailsResponseParamsType0
    from ..models.dag_tag_response import DagTagResponse
    from ..models.dag_version_response import DagVersionResponse


T = TypeVar("T", bound="DAGDetailsResponse")


@_attrs_define
class DAGDetailsResponse:
    """Specific serializer for DAG Details responses.

    Attributes:
        dag_id (str):
        dag_display_name (str):
        is_paused (bool):
        is_stale (bool):
        last_parsed_time (datetime.datetime | None):
        last_parse_duration (float | None):
        last_expired (datetime.datetime | None):
        bundle_name (None | str):
        bundle_version (None | str):
        relative_fileloc (None | str):
        fileloc (str):
        description (None | str):
        timetable_summary (None | str):
        timetable_description (None | str):
        tags (list[DagTagResponse]):
        max_active_tasks (int):
        max_active_runs (int | None):
        max_consecutive_failed_dag_runs (int):
        has_task_concurrency_limits (bool):
        has_import_errors (bool):
        next_dagrun_logical_date (datetime.datetime | None):
        next_dagrun_data_interval_start (datetime.datetime | None):
        next_dagrun_data_interval_end (datetime.datetime | None):
        next_dagrun_run_after (datetime.datetime | None):
        owners (list[str]):
        catchup (bool):
        dag_run_timeout (None | str):
        asset_expression (DAGDetailsResponseAssetExpressionType0 | None):
        doc_md (None | str):
        start_date (datetime.datetime | None):
        end_date (datetime.datetime | None):
        is_paused_upon_creation (bool | None):
        params (DAGDetailsResponseParamsType0 | None):
        render_template_as_native_obj (bool):
        template_search_path (list[str] | None):
        timezone (None | str):
        last_parsed (datetime.datetime | None):
        default_args (DAGDetailsResponseDefaultArgsType0 | None):
        file_token (str): Return file token.
        concurrency (int): Return max_active_tasks as concurrency.

            Deprecated: Use max_active_tasks instead.
        latest_dag_version (DagVersionResponse | None): Return the latest DagVersion.
        owner_links (DAGDetailsResponseOwnerLinksType0 | None | Unset):
        is_favorite (bool | Unset):  Default: False.
    """

    dag_id: str
    dag_display_name: str
    is_paused: bool
    is_stale: bool
    last_parsed_time: datetime.datetime | None
    last_parse_duration: float | None
    last_expired: datetime.datetime | None
    bundle_name: None | str
    bundle_version: None | str
    relative_fileloc: None | str
    fileloc: str
    description: None | str
    timetable_summary: None | str
    timetable_description: None | str
    tags: list[DagTagResponse]
    max_active_tasks: int
    max_active_runs: int | None
    max_consecutive_failed_dag_runs: int
    has_task_concurrency_limits: bool
    has_import_errors: bool
    next_dagrun_logical_date: datetime.datetime | None
    next_dagrun_data_interval_start: datetime.datetime | None
    next_dagrun_data_interval_end: datetime.datetime | None
    next_dagrun_run_after: datetime.datetime | None
    owners: list[str]
    catchup: bool
    dag_run_timeout: None | str
    asset_expression: DAGDetailsResponseAssetExpressionType0 | None
    doc_md: None | str
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    is_paused_upon_creation: bool | None
    params: DAGDetailsResponseParamsType0 | None
    render_template_as_native_obj: bool
    template_search_path: list[str] | None
    timezone: None | str
    last_parsed: datetime.datetime | None
    default_args: DAGDetailsResponseDefaultArgsType0 | None
    file_token: str
    concurrency: int
    latest_dag_version: DagVersionResponse | None
    owner_links: DAGDetailsResponseOwnerLinksType0 | None | Unset = UNSET
    is_favorite: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dag_details_response_asset_expression_type_0 import DAGDetailsResponseAssetExpressionType0
        from ..models.dag_details_response_default_args_type_0 import DAGDetailsResponseDefaultArgsType0
        from ..models.dag_details_response_owner_links_type_0 import DAGDetailsResponseOwnerLinksType0
        from ..models.dag_details_response_params_type_0 import DAGDetailsResponseParamsType0
        from ..models.dag_version_response import DagVersionResponse

        dag_id = self.dag_id

        dag_display_name = self.dag_display_name

        is_paused = self.is_paused

        is_stale = self.is_stale

        last_parsed_time: None | str
        if isinstance(self.last_parsed_time, datetime.datetime):
            last_parsed_time = self.last_parsed_time.isoformat()
        else:
            last_parsed_time = self.last_parsed_time

        last_parse_duration: float | None
        last_parse_duration = self.last_parse_duration

        last_expired: None | str
        if isinstance(self.last_expired, datetime.datetime):
            last_expired = self.last_expired.isoformat()
        else:
            last_expired = self.last_expired

        bundle_name: None | str
        bundle_name = self.bundle_name

        bundle_version: None | str
        bundle_version = self.bundle_version

        relative_fileloc: None | str
        relative_fileloc = self.relative_fileloc

        fileloc = self.fileloc

        description: None | str
        description = self.description

        timetable_summary: None | str
        timetable_summary = self.timetable_summary

        timetable_description: None | str
        timetable_description = self.timetable_description

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        max_active_tasks = self.max_active_tasks

        max_active_runs: int | None
        max_active_runs = self.max_active_runs

        max_consecutive_failed_dag_runs = self.max_consecutive_failed_dag_runs

        has_task_concurrency_limits = self.has_task_concurrency_limits

        has_import_errors = self.has_import_errors

        next_dagrun_logical_date: None | str
        if isinstance(self.next_dagrun_logical_date, datetime.datetime):
            next_dagrun_logical_date = self.next_dagrun_logical_date.isoformat()
        else:
            next_dagrun_logical_date = self.next_dagrun_logical_date

        next_dagrun_data_interval_start: None | str
        if isinstance(self.next_dagrun_data_interval_start, datetime.datetime):
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start.isoformat()
        else:
            next_dagrun_data_interval_start = self.next_dagrun_data_interval_start

        next_dagrun_data_interval_end: None | str
        if isinstance(self.next_dagrun_data_interval_end, datetime.datetime):
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end.isoformat()
        else:
            next_dagrun_data_interval_end = self.next_dagrun_data_interval_end

        next_dagrun_run_after: None | str
        if isinstance(self.next_dagrun_run_after, datetime.datetime):
            next_dagrun_run_after = self.next_dagrun_run_after.isoformat()
        else:
            next_dagrun_run_after = self.next_dagrun_run_after

        owners = self.owners

        catchup = self.catchup

        dag_run_timeout: None | str
        dag_run_timeout = self.dag_run_timeout

        asset_expression: dict[str, Any] | None
        if isinstance(self.asset_expression, DAGDetailsResponseAssetExpressionType0):
            asset_expression = self.asset_expression.to_dict()
        else:
            asset_expression = self.asset_expression

        doc_md: None | str
        doc_md = self.doc_md

        start_date: None | str
        if isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str
        if isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        is_paused_upon_creation: bool | None
        is_paused_upon_creation = self.is_paused_upon_creation

        params: dict[str, Any] | None
        if isinstance(self.params, DAGDetailsResponseParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        render_template_as_native_obj = self.render_template_as_native_obj

        template_search_path: list[str] | None
        if isinstance(self.template_search_path, list):
            template_search_path = self.template_search_path

        else:
            template_search_path = self.template_search_path

        timezone: None | str
        timezone = self.timezone

        last_parsed: None | str
        if isinstance(self.last_parsed, datetime.datetime):
            last_parsed = self.last_parsed.isoformat()
        else:
            last_parsed = self.last_parsed

        default_args: dict[str, Any] | None
        if isinstance(self.default_args, DAGDetailsResponseDefaultArgsType0):
            default_args = self.default_args.to_dict()
        else:
            default_args = self.default_args

        file_token = self.file_token

        concurrency = self.concurrency

        latest_dag_version: dict[str, Any] | None
        if isinstance(self.latest_dag_version, DagVersionResponse):
            latest_dag_version = self.latest_dag_version.to_dict()
        else:
            latest_dag_version = self.latest_dag_version

        owner_links: dict[str, Any] | None | Unset
        if isinstance(self.owner_links, Unset):
            owner_links = UNSET
        elif isinstance(self.owner_links, DAGDetailsResponseOwnerLinksType0):
            owner_links = self.owner_links.to_dict()
        else:
            owner_links = self.owner_links

        is_favorite = self.is_favorite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dag_id": dag_id,
                "dag_display_name": dag_display_name,
                "is_paused": is_paused,
                "is_stale": is_stale,
                "last_parsed_time": last_parsed_time,
                "last_parse_duration": last_parse_duration,
                "last_expired": last_expired,
                "bundle_name": bundle_name,
                "bundle_version": bundle_version,
                "relative_fileloc": relative_fileloc,
                "fileloc": fileloc,
                "description": description,
                "timetable_summary": timetable_summary,
                "timetable_description": timetable_description,
                "tags": tags,
                "max_active_tasks": max_active_tasks,
                "max_active_runs": max_active_runs,
                "max_consecutive_failed_dag_runs": max_consecutive_failed_dag_runs,
                "has_task_concurrency_limits": has_task_concurrency_limits,
                "has_import_errors": has_import_errors,
                "next_dagrun_logical_date": next_dagrun_logical_date,
                "next_dagrun_data_interval_start": next_dagrun_data_interval_start,
                "next_dagrun_data_interval_end": next_dagrun_data_interval_end,
                "next_dagrun_run_after": next_dagrun_run_after,
                "owners": owners,
                "catchup": catchup,
                "dag_run_timeout": dag_run_timeout,
                "asset_expression": asset_expression,
                "doc_md": doc_md,
                "start_date": start_date,
                "end_date": end_date,
                "is_paused_upon_creation": is_paused_upon_creation,
                "params": params,
                "render_template_as_native_obj": render_template_as_native_obj,
                "template_search_path": template_search_path,
                "timezone": timezone,
                "last_parsed": last_parsed,
                "default_args": default_args,
                "file_token": file_token,
                "concurrency": concurrency,
                "latest_dag_version": latest_dag_version,
            }
        )
        if owner_links is not UNSET:
            field_dict["owner_links"] = owner_links
        if is_favorite is not UNSET:
            field_dict["is_favorite"] = is_favorite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dag_details_response_asset_expression_type_0 import DAGDetailsResponseAssetExpressionType0
        from ..models.dag_details_response_default_args_type_0 import DAGDetailsResponseDefaultArgsType0
        from ..models.dag_details_response_owner_links_type_0 import DAGDetailsResponseOwnerLinksType0
        from ..models.dag_details_response_params_type_0 import DAGDetailsResponseParamsType0
        from ..models.dag_tag_response import DagTagResponse
        from ..models.dag_version_response import DagVersionResponse

        d = dict(src_dict)
        dag_id = d.pop("dag_id")

        dag_display_name = d.pop("dag_display_name")

        is_paused = d.pop("is_paused")

        is_stale = d.pop("is_stale")

        def _parse_last_parsed_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_time_type_0 = isoparse(data)

                return last_parsed_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_parsed_time = _parse_last_parsed_time(d.pop("last_parsed_time"))

        def _parse_last_parse_duration(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        last_parse_duration = _parse_last_parse_duration(d.pop("last_parse_duration"))

        def _parse_last_expired(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_expired_type_0 = isoparse(data)

                return last_expired_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_expired = _parse_last_expired(d.pop("last_expired"))

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

        def _parse_relative_fileloc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relative_fileloc = _parse_relative_fileloc(d.pop("relative_fileloc"))

        fileloc = d.pop("fileloc")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_timetable_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timetable_summary = _parse_timetable_summary(d.pop("timetable_summary"))

        def _parse_timetable_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timetable_description = _parse_timetable_description(d.pop("timetable_description"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DagTagResponse.from_dict(tags_item_data)

            tags.append(tags_item)

        max_active_tasks = d.pop("max_active_tasks")

        def _parse_max_active_runs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_active_runs = _parse_max_active_runs(d.pop("max_active_runs"))

        max_consecutive_failed_dag_runs = d.pop("max_consecutive_failed_dag_runs")

        has_task_concurrency_limits = d.pop("has_task_concurrency_limits")

        has_import_errors = d.pop("has_import_errors")

        def _parse_next_dagrun_logical_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_logical_date_type_0 = isoparse(data)

                return next_dagrun_logical_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_logical_date = _parse_next_dagrun_logical_date(d.pop("next_dagrun_logical_date"))

        def _parse_next_dagrun_data_interval_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_start_type_0 = isoparse(data)

                return next_dagrun_data_interval_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_data_interval_start = _parse_next_dagrun_data_interval_start(
            d.pop("next_dagrun_data_interval_start")
        )

        def _parse_next_dagrun_data_interval_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_data_interval_end_type_0 = isoparse(data)

                return next_dagrun_data_interval_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_data_interval_end = _parse_next_dagrun_data_interval_end(d.pop("next_dagrun_data_interval_end"))

        def _parse_next_dagrun_run_after(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_dagrun_run_after_type_0 = isoparse(data)

                return next_dagrun_run_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_dagrun_run_after = _parse_next_dagrun_run_after(d.pop("next_dagrun_run_after"))

        owners = cast(list[str], d.pop("owners"))

        catchup = d.pop("catchup")

        def _parse_dag_run_timeout(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dag_run_timeout = _parse_dag_run_timeout(d.pop("dag_run_timeout"))

        def _parse_asset_expression(data: object) -> DAGDetailsResponseAssetExpressionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_expression_type_0 = DAGDetailsResponseAssetExpressionType0.from_dict(data)

                return asset_expression_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGDetailsResponseAssetExpressionType0 | None, data)

        asset_expression = _parse_asset_expression(d.pop("asset_expression"))

        def _parse_doc_md(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        doc_md = _parse_doc_md(d.pop("doc_md"))

        def _parse_start_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_end_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_date = _parse_end_date(d.pop("end_date"))

        def _parse_is_paused_upon_creation(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_paused_upon_creation = _parse_is_paused_upon_creation(d.pop("is_paused_upon_creation"))

        def _parse_params(data: object) -> DAGDetailsResponseParamsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = DAGDetailsResponseParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGDetailsResponseParamsType0 | None, data)

        params = _parse_params(d.pop("params"))

        render_template_as_native_obj = d.pop("render_template_as_native_obj")

        def _parse_template_search_path(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                template_search_path_type_0 = cast(list[str], data)

                return template_search_path_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        template_search_path = _parse_template_search_path(d.pop("template_search_path"))

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        def _parse_last_parsed(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_parsed_type_0 = isoparse(data)

                return last_parsed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_parsed = _parse_last_parsed(d.pop("last_parsed"))

        def _parse_default_args(data: object) -> DAGDetailsResponseDefaultArgsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_args_type_0 = DAGDetailsResponseDefaultArgsType0.from_dict(data)

                return default_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGDetailsResponseDefaultArgsType0 | None, data)

        default_args = _parse_default_args(d.pop("default_args"))

        file_token = d.pop("file_token")

        concurrency = d.pop("concurrency")

        def _parse_latest_dag_version(data: object) -> DagVersionResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_dag_version_type_0 = DagVersionResponse.from_dict(data)

                return latest_dag_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DagVersionResponse | None, data)

        latest_dag_version = _parse_latest_dag_version(d.pop("latest_dag_version"))

        def _parse_owner_links(data: object) -> DAGDetailsResponseOwnerLinksType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_links_type_0 = DAGDetailsResponseOwnerLinksType0.from_dict(data)

                return owner_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DAGDetailsResponseOwnerLinksType0 | None | Unset, data)

        owner_links = _parse_owner_links(d.pop("owner_links", UNSET))

        is_favorite = d.pop("is_favorite", UNSET)

        dag_details_response = cls(
            dag_id=dag_id,
            dag_display_name=dag_display_name,
            is_paused=is_paused,
            is_stale=is_stale,
            last_parsed_time=last_parsed_time,
            last_parse_duration=last_parse_duration,
            last_expired=last_expired,
            bundle_name=bundle_name,
            bundle_version=bundle_version,
            relative_fileloc=relative_fileloc,
            fileloc=fileloc,
            description=description,
            timetable_summary=timetable_summary,
            timetable_description=timetable_description,
            tags=tags,
            max_active_tasks=max_active_tasks,
            max_active_runs=max_active_runs,
            max_consecutive_failed_dag_runs=max_consecutive_failed_dag_runs,
            has_task_concurrency_limits=has_task_concurrency_limits,
            has_import_errors=has_import_errors,
            next_dagrun_logical_date=next_dagrun_logical_date,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_run_after=next_dagrun_run_after,
            owners=owners,
            catchup=catchup,
            dag_run_timeout=dag_run_timeout,
            asset_expression=asset_expression,
            doc_md=doc_md,
            start_date=start_date,
            end_date=end_date,
            is_paused_upon_creation=is_paused_upon_creation,
            params=params,
            render_template_as_native_obj=render_template_as_native_obj,
            template_search_path=template_search_path,
            timezone=timezone,
            last_parsed=last_parsed,
            default_args=default_args,
            file_token=file_token,
            concurrency=concurrency,
            latest_dag_version=latest_dag_version,
            owner_links=owner_links,
            is_favorite=is_favorite,
        )

        dag_details_response.additional_properties = d
        return dag_details_response

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
