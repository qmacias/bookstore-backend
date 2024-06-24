from abc import ABC, abstractmethod

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.id.AuthorId import AuthorId


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author: Author) -> None:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def find(self, author_id: AuthorId) -> Author:
        raise NotImplementedError('Must be implemented.')

    @abstractmethod
    def delete(self, author_id: AuthorId) -> None:
        raise NotImplementedError('Must be implemented.')
