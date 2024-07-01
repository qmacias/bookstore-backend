from logging import Logger

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorFinder import AuthorFinder
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorRemover:
    def __init__(self, repository: AuthorRepository, logger: Logger) -> None:
        self.__repository = repository
        self.__finder = AuthorFinder(repository, logger)

    def remove(self, id: str) -> None:
        author: Author = self.__finder(id)

        self.__repository.delete(author.id)
