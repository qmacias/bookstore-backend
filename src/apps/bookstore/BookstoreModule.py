from logging import Logger
from injector import Module, singleton, provider, Injector

from src.apps.bookstore.config_logger import config_logger

from src.contexts.bookstore.authors.application.AuthorCreator import AuthorCreator
from src.contexts.bookstore.authors.application.AuthorModifier import AuthorModifier
from src.contexts.bookstore.authors.application.AuthorRemover import AuthorRemover
from src.contexts.bookstore.authors.application.AuthorSearcher import AuthorSearcher
from src.contexts.bookstore.authors.application.AuthorsSearcher import AuthorsSearcher
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from src.contexts.bookstore.authors.infrastructure.InMemoryAuthorRepository import InMemoryAuthorRepository


class BookstoreModule(Module):

    @singleton
    @provider
    def logger(self) -> Logger:
        return config_logger(__name__)

    @singleton
    @provider
    def author_repository(self, logger: Logger) -> AuthorRepository:
        return InMemoryAuthorRepository(logger)

    @provider
    def author_creator(self, repository: AuthorRepository, logger: Logger) -> AuthorCreator:
        return AuthorCreator(repository, logger)

    @provider
    def author_modifier(self, repository: AuthorRepository, logger: Logger) -> AuthorModifier:
        return AuthorModifier(repository, logger)

    @provider
    def author_remover(self, repository: AuthorRepository, logger: Logger) -> AuthorRemover:
        return AuthorRemover(repository, logger)

    @provider
    def author_searcher(self, repository: AuthorRepository, logger: Logger) -> AuthorSearcher:
        return AuthorSearcher(repository, logger)

    @provider
    def authors_searcher(self, repository: AuthorRepository, logger: Logger) -> AuthorsSearcher:
        return AuthorsSearcher(repository, logger)


container = Injector([BookstoreModule], auto_bind=True)
