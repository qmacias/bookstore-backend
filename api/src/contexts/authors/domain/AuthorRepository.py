from abc import ABC, abstractmethod

from api.src.contexts.authors.domain.Author import Author


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author: Author) -> None:
        raise NotImplementedError('Must be implemented.')
