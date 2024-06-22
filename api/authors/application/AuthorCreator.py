import logging

from api.authors.domain.Author import Author
from api.authors.domain.AuthorIdIsBadlyFormed import AuthorIdIsBadlyFormed
from api.authors.domain.AuthorNameDoesNotMatch import AuthorNameDoesNotMatch
from api.authors.domain.AuthorRepository import AuthorRepository
from api.authors.domain.InvalidAuthorId import InvalidAuthorId
from api.authors.domain.InvalidAuthorName import InvalidAuthorName


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
