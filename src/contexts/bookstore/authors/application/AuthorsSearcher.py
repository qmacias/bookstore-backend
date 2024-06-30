from logging import Logger
from typing import Sequence
from types import MappingProxyType

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorsSearcher:

    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def search_all(self) -> Sequence[MappingProxyType]:
        authors: Sequence[Author] = self.__repository.find_all()

        return [author.to_primitives() for author in authors]
