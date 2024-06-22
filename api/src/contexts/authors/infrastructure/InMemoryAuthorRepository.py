from copy import deepcopy

from api.src.contexts.authors.domain.Author import Author
from api.src.contexts.authors.domain.AuthorRepository import AuthorRepository
from api.src.contexts.authors.infrastructure.AuthorCollection import AuthorCollection


class InMemoryAuthorRepository(AuthorRepository):
    __authors = deepcopy(AuthorCollection)

    def save(self, author: Author) -> None:
        self.__authors[author.id] = deepcopy(author)
