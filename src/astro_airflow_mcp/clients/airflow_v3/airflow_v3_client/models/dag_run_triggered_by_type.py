from enum import Enum


class DagRunTriggeredByType(str, Enum):
    ASSET = "asset"
    BACKFILL = "backfill"
    CLI = "cli"
    OPERATOR = "operator"
    REST_API = "rest_api"
    TEST = "test"
    TIMETABLE = "timetable"
    UI = "ui"

    def __str__(self) -> str:
        return str(self.value)
