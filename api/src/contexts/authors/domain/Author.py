class Author:
    @staticmethod
    def create(id: str, name: str) -> 'Author':
        author = Author(id, name)

        return author

    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return hash((self._id, self._name))

    def __eq__(self, other: 'Author') -> bool:
        return self._id == other.id and self._name == other.name

    def __repr__(self) -> str:
        return '<Author: id={0}, name{1}>'.format(self._id, self._name)
