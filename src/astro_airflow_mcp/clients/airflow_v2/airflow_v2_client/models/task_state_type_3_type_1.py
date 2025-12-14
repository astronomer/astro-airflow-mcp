from enum import Enum


class TaskStateType3Type1(str, Enum):
    DEFERRED = "deferred"
    FAILED = "failed"
    NONE = "none"
    QUEUED = "queued"
    REMOVED = "removed"
    RESTARTING = "restarting"
    RUNNING = "running"
    SCHEDULED = "scheduled"
    SKIPPED = "skipped"
    SUCCESS = "success"
    UPSTREAM_FAILED = "upstream_failed"
    UP_FOR_RESCHEDULE = "up_for_reschedule"
    UP_FOR_RETRY = "up_for_retry"

    def __str__(self) -> str:
        return str(self.value)
