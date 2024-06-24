class AuthorAlreadyExists(Exception):
    def __init__(self, author_id: str):
        super().__init__(f"Author with id '{author_id}' already exists")
