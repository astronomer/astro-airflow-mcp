from enum import Enum


class GetDagSourceAccept(str, Enum):
    APPLICATIONJSON = "application/json"
    TEXTPLAIN = "text/plain"
    VALUE_2 = "*/*"

    def __str__(self) -> str:
        return str(self.value)
