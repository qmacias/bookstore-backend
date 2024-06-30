from typing import Sequence
from abc import ABC, abstractmethod

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId


class AuthorRepository(ABC):
    @abstractmethod
    def find_all(self) -> Sequence[Author]:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def save(self, author: Author) -> None:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def update(self, author: Author) -> None:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def find(self, author_id: AuthorId) -> Author:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def delete(self, author_id: AuthorId) -> None:
        raise NotImplementedError('Must be implemented.')
