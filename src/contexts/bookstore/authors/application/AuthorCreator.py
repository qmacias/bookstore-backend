from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorAlreadyExists import AuthorAlreadyExists
from src.contexts.bookstore.authors.domain.AuthorAlreadyExistsDuplicate import AuthorAlreadyExistsDuplicate
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorName import AuthorName
from src.contexts.bookstore.authors.domain.AuthorNameAlreadyExists import AuthorNameAlreadyExists
from src.contexts.bookstore.authors.domain.AuthorNameAlreadyExistsIntegrity import AuthorNameAlreadyExistsIntegrity
from src.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid
from src.contexts.bookstore.authors.domain.AuthorNameNotValidPattern import AuthorNameNotValidPattern
from src.contexts.bookstore.authors.domain.AuthorNameNotValidType import AuthorNameNotValidType
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorCreator:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def create(self, name: str) -> None:
        author = None
        try:
            try:
                author_id = AuthorId.new()
                author_name = AuthorName(name)

                author = Author.create(author_id, author_name)
            except (AuthorNameNotValidType, AuthorNameNotValidPattern) as e:
                self.__logger.error(e)

                raise AuthorNameNotValid(name)

            self.__repository.save(author)
        except AuthorAlreadyExistsDuplicate as e:
            self.__logger.error(e)

            raise AuthorAlreadyExists(author.id.value)
        except AuthorNameAlreadyExistsIntegrity as e:
            self.__logger.error(e)

            raise AuthorNameAlreadyExists(name)
