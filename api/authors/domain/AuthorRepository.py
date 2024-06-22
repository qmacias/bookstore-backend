from abc import ABC, abstractmethod

from api.authors.domain.Author import Author


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author: Author) -> None:
        raise NotImplementedError('Must be implemented.')
