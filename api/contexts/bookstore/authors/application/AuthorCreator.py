from logging import Logger

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository

from api.contexts.bookstore.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.contexts.bookstore.authors.domain.AuthorIdInvalidFormat import AuthorIdInvalidFormat

from api.contexts.bookstore.authors.domain.InvalidAuthorName import InvalidAuthorName
from api.contexts.bookstore.authors.domain.AuthorNameInvalidPattern import AuthorNameInvalidPattern


class AuthorCreator:

    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def create(self, id: str, name: str) -> None:
        try:
            author = Author.create(id, name)

            self.__repository.save(author)
        except AuthorIdInvalidFormat as e:
            self.__logger.error(e)

            raise InvalidAuthorId(id)
        except AuthorNameInvalidPattern as e:
            self.__logger.error(e)

            raise InvalidAuthorName(name)
