from re import match
from typing import final

from api.src.contexts.authors.domain.AuthorNameDoesNotMatch import AuthorNameDoesNotMatch


@final
class AuthorName(object):
    _REGEX = r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$'

    def __init__(self, value: str) -> None:
        self._value = value
        self.__ensure_valid_name()

    def __ensure_valid_name(self) -> None:
        try:
            self.__is_matching()
        except AssertionError:
            raise AuthorNameDoesNotMatch(
                "No matches for '{0}'".format(self._value)
            )

    def __is_matching(self) -> None:
        assert match(self._REGEX, self._value) is not None

    @property
    def value(self) -> str:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other: 'AuthorName') -> bool:
        return self._value == other.value

    def __repr__(self) -> str:
        return '<AuthorName: value={0}>'.format(self.value)
