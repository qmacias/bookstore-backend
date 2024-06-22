import logging

from api.src.contexts.authors.domain.Author import Author
from api.src.contexts.authors.domain.AuthorIdIsBadlyFormed import AuthorIdIsBadlyFormed
from api.src.contexts.authors.domain.AuthorNameDoesNotMatch import AuthorNameDoesNotMatch
from api.src.contexts.authors.domain.AuthorRepository import AuthorRepository
from api.src.contexts.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.src.contexts.authors.domain.InvalidAuthorName import InvalidAuthorName


class AuthorCreator:

    def __init__(self, repository: AuthorRepository) -> None:
        self.__repository = repository

    def create(self, id: str, name: str) -> None:
        try:
            author = Author.create(id, name)

            self.__repository.save(author)
        except AuthorIdIsBadlyFormed as e:
            logging.error(e)
            raise InvalidAuthorId(id)
        except AuthorNameDoesNotMatch as e:
            logging.error(e)
            raise InvalidAuthorName(name)
