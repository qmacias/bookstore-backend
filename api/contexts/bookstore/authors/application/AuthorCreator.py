from logging import Logger

from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository

from api.contexts.bookstore.authors.domain.id.AuthorIdNotValid import AuthorIdNotValid
from api.contexts.bookstore.authors.domain.AuthorAlreadyExists import AuthorAlreadyExists
from api.contexts.bookstore.authors.domain.AuthorLookUpConflict import AuthorLookUpConflict
from api.contexts.bookstore.authors.domain.id.AuthorIdNotValidFormat import AuthorIdNotValidFormat

from api.contexts.bookstore.authors.domain.name.AuthorNameNotValid import AuthorNameNotValid
from api.contexts.bookstore.authors.domain.name.AuthorNameNotValidPattern import AuthorNameInvalidPattern


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
        except AuthorNameInvalidPattern as e:
            self.__logger.error(e)

            raise AuthorNameNotValid(name)
        except AuthorLookUpConflict as e:
            self.__logger.error(e)

            raise AuthorAlreadyExists(id)
