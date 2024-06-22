class AuthorNameDoesNotMatch(Exception):

    def __init__(self, error: str) -> None:
        super().__init__('AuthorNameDoesNotMatch: {0}'.format(error))
