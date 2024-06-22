from injector import Module, singleton, provider, Injector

from api.authors.application.AuthorCreator import AuthorCreator
from api.authors.domain.AuthorRepository import AuthorRepository
from api.authors.infrastructure.InMemoryAuthorRepository import InMemoryAuthorRepository


class AuthorWiringModule(Module):

    @singleton
    @provider
    def author_repository(self) -> AuthorRepository:
        return InMemoryAuthorRepository()

    @provider
    def author_creator(self, repository: AuthorRepository) -> AuthorCreator:
        return AuthorCreator(repository)


container = Injector([AuthorWiringModule], auto_bind=True)
