class AuthorIdNotValid(Exception):
    def __init__(self, author_id: str) -> None:
        super().__init__(f"Author id '{author_id}' not valid.")
