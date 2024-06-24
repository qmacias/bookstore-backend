from injector import Module, singleton, provider, Injector
from logging import Logger, getLogger, DEBUG, Formatter, StreamHandler

from api.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator
from api.contexts.bookstore.authors.application.AuthorRemover import AuthorRemover
from api.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher

from api.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from api.contexts.bookstore.authors.infrastructure.InMemoryAuthorRepository import InMemoryAuthorRepository


class BookstoreModule(Module):

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

    @provider
    def author_remover(self, repository: AuthorRepository, logger: Logger) -> AuthorRemover:
        return AuthorRemover(repository, logger)

    @provider
    def author_searcher(self, repository: AuthorRepository, logger: Logger) -> AuthorSearcher:
        return AuthorSearcher(repository, logger)


container = Injector([BookstoreModule], auto_bind=True)
