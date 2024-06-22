from logging import Logger

from api.authors.domain.Author import Author
from api.authors.domain.AuthorIdIsBadlyFormed import AuthorIdIsBadlyFormed
from api.authors.domain.AuthorNameDoesNotMatch import AuthorNameDoesNotMatch
from api.authors.domain.AuthorRepository import AuthorRepository
from api.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.authors.domain.InvalidAuthorName import InvalidAuthorName


class AuthorCreator:

    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__logger = logger

    def create(self, id: str, name: str) -> None:
        try:
            author = Author.create(id, name)

            self.__repository.save(author)
        except AuthorIdIsBadlyFormed as e:
            self.__logger.error(e)
            raise InvalidAuthorId(id)
        except AuthorNameDoesNotMatch as e:
            self.__logger.error(e)
            raise InvalidAuthorName(name)
