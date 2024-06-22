from api.src.contexts.authors.domain.AuthorId import AuthorId
from api.src.contexts.authors.domain.AuthorName import AuthorName


class Author:
    def __init__(self, id: AuthorId, name: AuthorName) -> None:
        self._id = id
        self._name = name

    @staticmethod
    def create(id: str, name: str) -> 'Author':
        return Author(AuthorId(id), AuthorName(name))

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    def change_name(self, value: str) -> None:
        self._name = AuthorName(value)

    def __hash__(self) -> int:
        return hash((self._id, self._name))

    def __eq__(self, other) -> bool:
        if isinstance(other, Author):
            return (self._id == other.id
                    and self._name == other.name)
        return False

    def __repr__(self) -> str:
        return f"<Author: {self._id}, {self._name}>"
