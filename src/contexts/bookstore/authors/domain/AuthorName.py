from re import match
from typing import final

from src.contexts.bookstore.authors.domain.AuthorNameNotValidType import AuthorNameNotValidType
from src.contexts.bookstore.authors.domain.AuthorNameNotValidPattern import AuthorNameNotValidPattern


@final
class AuthorName(object):
    __REGEX = r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$'

    def __init__(self, value: str) -> None:
        try:
            self._value = value.strip()
        except AttributeError as e:
            raise AuthorNameNotValidType(str(e))

        self.__ensure_valid_author_name()

    def __ensure_valid_author_name(self) -> None:
        if not match(self.__REGEX, self._value):
            raise AuthorNameNotValidPattern(f"no pattern for '{self._value}'")

    @property
    def value(self) -> str:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthorName):
            return self._value == other.value
        return False

    def __repr__(self) -> str:
        return f"<AuthorName: '{self.value}'>"
