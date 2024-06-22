class AuthorIdIsBadlyFormed(Exception):
    def __init__(self, error: str) -> None:
        super().__init__('AuthorIdIsBadlyFormed: {0}'.format(error))
