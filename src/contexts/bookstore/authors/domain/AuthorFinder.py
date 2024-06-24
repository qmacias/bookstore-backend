from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorFinder:
    def __init__(self, repository: AuthorRepository) -> None:
        self.__repository = repository

    def __call__(self, id: str) -> Author:
        author_id = AuthorId(id)

        return self.__repository.find(author_id)
