from logging import Logger
from types import MappingProxyType

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorSearcher:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__finder = AuthorFinder(repository, logger)

    def search(self, id: str) -> MappingProxyType:
        author: Author = self.__finder(id)

        return author.to_primitives()
