from logging import Logger
from types import MappingProxyType

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from src.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists
from src.contexts.bookstore.authors.domain.AuthorDoesNotExistsUnknown import AuthorDoesNotExistsUnknown

from src.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from src.contexts.bookstore.authors.domain.AuthorIdNotValidFormat import AuthorIdNotValidFormat


class AuthorSearcher:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__finder = AuthorFinder(repository)
        self.__logger = logger

    def search(self, id: str) -> MappingProxyType:
        try:
            author: Author = self.__finder(id)

            return author.to_primitives()
        except AuthorIdNotValidFormat as e:
            self.__logger.error(e)

            raise AuthorIdNotValid(id)
        except AuthorDoesNotExistsUnknown as e:
            self.__logger.error(e)

            raise AuthorDoesNotExists(id)
