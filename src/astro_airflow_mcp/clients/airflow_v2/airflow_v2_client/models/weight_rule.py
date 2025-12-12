from enum import Enum


class WeightRule(str, Enum):
    ABSOLUTE = "absolute"
    DOWNSTREAM = "downstream"
    UPSTREAM = "upstream"

    def __str__(self) -> str:
        return str(self.value)
