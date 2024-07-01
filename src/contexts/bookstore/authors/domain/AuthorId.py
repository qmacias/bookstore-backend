from uuid import UUID
from typing import final

from src.contexts.bookstore.authors.domain.AuthorIdNotValidFormat import AuthorIdNotValidFormat


@final
class AuthorId(object):
    def __init__(self, value: str) -> None:
        self._value = value.strip()
        self.__ensure_valid_author_id()

    def __ensure_valid_author_id(self) -> None:
        try:
            UUID(self._value, version=4)
        except ValueError as e:
            raise AuthorIdNotValidFormat(str(e)) from e

    @property
    def value(self) -> str:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthorId):
            return self._value == other.value
        return False

    def __repr__(self) -> str:
        return f"<AuthorId: '{self.value}'>"
