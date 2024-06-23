from api.contexts.bookstore.authors.domain.Author import Author
from api.contexts.bookstore.authors.domain.AuthorId import AuthorId
from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository


class AuthorFinder:
    def __init__(self, repository: AuthorRepository) -> None:
        self.__repository = repository

    def __call__(self, author_id: AuthorId) -> Author:
        return self.__repository.find(author_id)
