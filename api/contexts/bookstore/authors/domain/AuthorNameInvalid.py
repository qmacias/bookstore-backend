class AuthorNameInvalid(Exception):
    def __init__(self, author_name: str) -> None:
        super().__init__(f"Invalid author name '{author_name}'")
