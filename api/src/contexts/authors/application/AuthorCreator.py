from api.src.contexts.authors.domain.Author import Author
from api.src.contexts.authors.domain.AuthorRepository import AuthorRepository


class AuthorCreator:

    def __init__(self, repository: AuthorRepository) -> None:
        self.__repository = repository

    def create(self, id: str, name: str) -> None:
        author = Author.create(id, name)

        self.__repository.save(author)
