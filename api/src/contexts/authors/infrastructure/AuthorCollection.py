from typing import TypedDict, Dict

from api.src.contexts.authors.domain.Author import Author


class AuthorDetails(TypedDict):
    pass


'''
    Although it is initialised as empty,
    it can contain author entries at runtime.
'''
AuthorCollection: Dict[str, Author] = AuthorDetails()
