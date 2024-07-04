from typing import Any
from types import MappingProxyType

from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorName import AuthorName


class Author:
    def __init__(self, id: AuthorId, name: AuthorName) -> None:
        self._id = id
        self._name = name

    @staticmethod
    def create(id: AuthorId, name: AuthorName) -> 'Author':
        author = Author(id, name)

        return author

    @property
    def id(self) -> AuthorId:
        return self._id

    @property
    def name(self) -> AuthorName:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = AuthorName(value)

    def to_primitives(self) -> MappingProxyType:
        return MappingProxyType({'id': self._id.value, 'name': self._name.value})

    @staticmethod
    def from_primitives(plain_data: Any) -> 'Author':
        return Author(AuthorId(plain_data.get('id')), AuthorName(plain_data.get('name')))

    def __hash__(self) -> int:
        return hash((self._id, self._name))

    def __eq__(self, other) -> bool:
        if isinstance(other, Author):
            return (self._id == other.id
                    and self._name == other.name)
        return False

    def __repr__(self) -> str:
        return f"<Author: {self._id}, {self._name}>"
