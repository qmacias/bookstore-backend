class AuthorIdInvalid(Exception):
    def __init__(self, author_id: str) -> None:
        super().__init__(f"Invalid author id '{author_id}'")
