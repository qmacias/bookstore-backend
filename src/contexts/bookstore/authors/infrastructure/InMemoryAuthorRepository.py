from typing import Dict
from copy import deepcopy
from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from src.contexts.bookstore.authors.domain.AuthorDoesNotExistsUnknown import AuthorDoesNotExistsUnknown
from src.contexts.bookstore.authors.domain.AuthorAlreadyExistsDuplicate import AuthorAlreadyExistsDuplicate


class InMemoryAuthorRepository(AuthorRepository):
    """
        Although it is initialised as empty,
        it can contain author entries at runtime.
    """
    __authors: Dict[str, Author] = {}

    def __init__(self, logger: Logger) -> None:
        self.__logger = logger

    def save(self, author: Author) -> None:
        for existing_author in self.__authors.values():
            if existing_author.id == author.id:
                raise AuthorAlreadyExistsDuplicate(f"duplicate registry: '{author.id.value}'")

        self.__authors[author.id.value] = deepcopy(author)

        self.__logger.info(self.__authors)

    def find(self, author_id: AuthorId) -> Author:
        try:
            return deepcopy(self.__authors[author_id.value])
        except KeyError as e:
            raise AuthorDoesNotExistsUnknown(f'unknown registry: {str(e)}') from e

    def delete(self, author_id: AuthorId) -> None:
        del self.__authors[author_id.value]

        self.__logger.info(self.__authors)
