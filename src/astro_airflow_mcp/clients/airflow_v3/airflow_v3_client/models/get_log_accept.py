from enum import Enum


class GetLogAccept(str, Enum):
    APPLICATIONJSON = "application/json"
    APPLICATIONX_NDJSON = "application/x-ndjson"
    VALUE_2 = "*/*"

    def __str__(self) -> str:
        return str(self.value)
