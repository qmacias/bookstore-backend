from uuid import UUID
from typing import final

from api.src.contexts.authors.domain.AuthorIdIsBadlyFormed import AuthorIdIsBadlyFormed


@final
class AuthorId(object):

    def __init__(self, value: str) -> None:
        self._value = value
        self.__ensure_valid_id()

    def __ensure_valid_id(self) -> None:
        try:
            UUID(self._value, version=4)
        except ValueError as e:
            raise AuthorIdIsBadlyFormed(str(e)) from e

    @property
    def value(self) -> str:
        return self._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __eq__(self, other: 'AuthorId') -> bool:
        return self._value == other.value

    def __repr__(self) -> str:
        return '<AuthorId: value={0}>'.format(self.value)
