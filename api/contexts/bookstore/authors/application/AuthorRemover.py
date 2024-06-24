from logging import Logger

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from api.contexts.bookstore.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from api.contexts.bookstore.authors.domain.AuthorDoesNotExist import AuthorDoesNotExist
from api.contexts.bookstore.authors.domain.AuthorLookUpFailed import AuthorLookUpFailed
from api.contexts.bookstore.authors.domain.AuthorIdInvalidFormat import AuthorIdInvalidFormat


class AuthorRemover:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__finder = AuthorFinder(repository)
        self.__logger = logger

    def remove(self, id: str) -> None:
        try:
            author: Author = self.__finder(id)

            self.__repository.delete(author.id)
        except AuthorIdInvalidFormat as e:
            self.__logger.error(e)

            raise InvalidAuthorId(id)
        except AuthorLookUpFailed as e:
            self.__logger.error(e)

            raise AuthorDoesNotExist(id)
