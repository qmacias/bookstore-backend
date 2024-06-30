from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorDoesNotExists import AuthorDoesNotExists
from src.contexts.bookstore.authors.domain.AuthorDoesNotExistsUnknown import AuthorDoesNotExistsUnknown
from src.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from src.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from src.contexts.bookstore.authors.domain.AuthorIdNotValidFormat import AuthorIdNotValidFormat
from src.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid
from src.contexts.bookstore.authors.domain.AuthorNameNotValidPattern import AuthorNameNotValidPattern
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorModifier:

    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__finder = AuthorFinder(repository)
        self.__logger = logger

    def modify(self, id: str, name: str) -> None:
        try:
            author: Author = self.__finder(id)

            author.name = name

            self.__repository.update(author)
        except AuthorIdNotValidFormat as e:
            self.__logger.error(e)

            raise AuthorIdNotValid(id)
        except AuthorNameNotValidPattern as e:
            self.__logger.error(e)

            raise AuthorNameNotValid(name)
        except AuthorDoesNotExistsUnknown as e:
            self.__logger.error(e)

            raise AuthorDoesNotExists(id)
