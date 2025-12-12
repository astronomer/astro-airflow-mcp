from enum import Enum


class DagState(str, Enum):
    FAILED = "failed"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
