from copy import deepcopy
from logging import Logger

from api.authors.domain.Author import Author
from api.authors.domain.AuthorRepository import AuthorRepository
from api.authors.infrastructure.AuthorCollection import AuthorCollection


class InMemoryAuthorRepository(AuthorRepository):
    __authors = deepcopy(AuthorCollection)

    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def save(self, author: Author) -> None:
        self.__authors[author.id] = deepcopy(author)

        self.logger.info(self.__authors)
