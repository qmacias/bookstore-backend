from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorAlreadyExists import AuthorAlreadyExists
from src.contexts.bookstore.authors.domain.AuthorAlreadyExistsDuplicate import AuthorAlreadyExistsDuplicate
from src.contexts.bookstore.authors.domain.AuthorIdNotValid import AuthorIdNotValid
from src.contexts.bookstore.authors.domain.AuthorIdNotValidFormat import AuthorIdNotValidFormat
from src.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid
from src.contexts.bookstore.authors.domain.AuthorNameNotValidPattern import AuthorNameNotValidPattern
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorCreator:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def create(self, id: str, name: str) -> None:
        try:
            author = Author.create(id, name)

            self.__repository.save(author)
        except AuthorIdNotValidFormat as e:
            self.__logger.error(e)

            raise AuthorIdNotValid(id)
        except AuthorNameNotValidPattern as e:
            self.__logger.error(e)

            raise AuthorNameNotValid(name)
        except AuthorAlreadyExistsDuplicate as e:
            self.__logger.error(e)

            raise AuthorAlreadyExists(id)
