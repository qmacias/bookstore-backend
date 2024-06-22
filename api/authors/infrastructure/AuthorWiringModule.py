from injector import Module, singleton, provider, Injector
from logging import Logger, getLogger, DEBUG, Formatter, StreamHandler

from api.authors.application.AuthorCreator import AuthorCreator
from api.authors.domain.AuthorRepository import AuthorRepository
from api.authors.infrastructure.InMemoryAuthorRepository import InMemoryAuthorRepository


class AuthorWiringModule(Module):

    @singleton
    @provider
    def logger(self) -> Logger:
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)

        formatter = Formatter('%(levelname)s:%(message)s')

        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

        return logger

    @singleton
    @provider
    def author_repository(self, logger: Logger) -> AuthorRepository:
        return InMemoryAuthorRepository(logger)

    @provider
    def author_creator(self, repository: AuthorRepository, logger: Logger) -> AuthorCreator:
        return AuthorCreator(repository, logger)


container = Injector([AuthorWiringModule], auto_bind=True)
