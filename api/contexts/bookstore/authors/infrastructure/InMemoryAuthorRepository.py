from typing import Dict
from copy import deepcopy
from logging import Logger

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorId import AuthorId
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from api.contexts.bookstore.authors.domain.AuthorLookUpFailed import AuthorLookUpFailed
from api.contexts.bookstore.authors.domain.AuthorLookUpConflict import AuthorLookUpConflict


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
                raise AuthorLookUpConflict(f"author lookup conflict: '{author.id.value}'")

        self.__authors[author.id.value] = deepcopy(author)

        self.__logger.info(self.__authors)

    def find(self, author_id: AuthorId) -> Author:
        try:
            return deepcopy(self.__authors[author_id.value])
        except KeyError as e:
            raise AuthorLookUpFailed(f'author lookup failed: {str(e)}') from e

    def delete(self, author_id: AuthorId) -> None:
        del self.__authors[author_id.value]

        self.__logger.info(self.__authors)
