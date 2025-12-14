from enum import Enum


class GetConfigValueAccept(str, Enum):
    APPLICATIONJSON = "application/json"
    TEXTPLAIN = "text/plain"
    VALUE_2 = "*/*"

    def __str__(self) -> str:
        return str(self.value)
