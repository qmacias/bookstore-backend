class AuthorIdIsBadlyFormed(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(f"AuthorIdIsBadlyFormed: {error}")
