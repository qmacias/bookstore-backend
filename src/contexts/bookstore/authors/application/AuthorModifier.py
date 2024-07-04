from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from src.contexts.bookstore.authors.domain.AuthorNameNotValid import AuthorNameNotValid
from src.contexts.bookstore.authors.domain.AuthorNameNotValidPattern import AuthorNameNotValidPattern
from src.contexts.bookstore.authors.domain.AuthorNameNotValidType import AuthorNameNotValidType
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorModifier:

    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__finder = AuthorFinder(repository, logger)
        self.__logger = logger

    def modify(self, id: str, name: str) -> None:
        author: Author = self.__finder(id)

        try:
            author.name = name

            self.__repository.update(author)
        except (AuthorNameNotValidType, AuthorNameNotValidPattern) as e:
            self.__logger.error(e)

            raise AuthorNameNotValid(name)
