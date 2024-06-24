from logging import Logger
from types import MappingProxyType

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from api.contexts.bookstore.authors.domain.AuthorDoesNotExist import AuthorDoesNotExist
from api.contexts.bookstore.authors.domain.AuthorLookUpFailed import AuthorLookUpFailed

from api.contexts.bookstore.authors.domain.AuthorIdInvalid import AuthorIdInvalid
from api.contexts.bookstore.authors.domain.AuthorIdInvalidFormat import AuthorIdInvalidFormat


class AuthorSearcher:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__finder = AuthorFinder(repository)
        self.__logger = logger

    def search(self, id: str) -> MappingProxyType:
        try:
            author: Author = self.__finder(id)

            return author.to_primitives()
        except AuthorIdInvalidFormat as e:
            self.__logger.error(e)

            raise AuthorIdInvalid(id)
        except AuthorLookUpFailed as e:
            self.__logger.error(e)

            raise AuthorDoesNotExist(id)
