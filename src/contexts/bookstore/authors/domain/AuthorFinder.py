from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists
from src.contexts.bookstore.authors.domain.AuthorDoesNotExistsUnknown import AuthorDoesNotExistsUnknown
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from src.contexts.bookstore.authors.domain.AuthorIdNotValidFormat import AuthorIdNotValidFormat
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorFinder:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def __call__(self, id: str) -> Author:
        try:
            try:
                author_id = AuthorId(id)
            except AuthorIdNotValidFormat as e:
                self.__logger.error(e)

                raise AuthorIdNotValid(id)

            return self.__repository.find(author_id)
        except AuthorDoesNotExistsUnknown as e:
            self.__logger.error(e)

            raise AuthorDoesNotExists(id)
