from enum import Enum


class BulkActionNotOnExistence(str, Enum):
    FAIL = "fail"
    SKIP = "skip"

    def __str__(self) -> str:
        return str(self.value)
