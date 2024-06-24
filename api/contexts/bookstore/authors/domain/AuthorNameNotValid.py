class AuthorNameNotValid(Exception):
    def __init__(self, author_name: str) -> None:
        super().__init__(f"Author name '{author_name}' not valid.")
