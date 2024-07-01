from os import getenv
from typing import Any

from src.contexts.bookstore.shared.infrastructure.EnvironVariable import EnvironVariable


class EnvironLector:

    @staticmethod
    def get(var: EnvironVariable, parser: Any = None) -> Any:
        value = getenv(key=var.value)

        if parser is not None and value is not None:
            value = parser(value)

        return value
