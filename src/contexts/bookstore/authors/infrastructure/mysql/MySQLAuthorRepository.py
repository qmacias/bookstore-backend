from logging import Logger
from mysql import connector
from typing import Sequence

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from src.contexts.bookstore.authors.infrastructure.mysql.MySQLAuthorEnviron import MySQLAuthorEnviron


class MySQLAuthorRepository(AuthorRepository):
    def __init__(self, environ: MySQLAuthorEnviron, logger: Logger) -> None:
        self.__db = connector.connect(
            host=environ.host,
            user=environ.user,
            password=environ.password,
            database=environ.database,
        )
        self.__logger = logger

    def find_all(self) -> Sequence[Author]:
        cursor = self.__db.cursor(dictionary=True)

        cursor.execute('''
            SELECT BIN_TO_UUID(id, true) AS id, name FROM authors
        ''')

        records = cursor.fetchall()

        self.__logger.info(records)

        cursor.close()

        authors = [Author.create(id=row['id'], name=row['name']) for row in records]

        return authors

    def save(self, author: Author) -> None:
        cursor = self.__db.cursor()

        cursor.execute('''
            INSERT INTO authors (id, name)
            VALUES (UUID_TO_BIN(%s, true), %s)
        ''', (author.id.value, author.name.value,))

        self.__db.commit()

        cursor.close()

    def update(self, author: Author) -> None:
        cursor = self.__db.cursor()

        cursor.execute('''
            UPDATE authors SET name = %s
            WHERE id = UUID_TO_BIN(%s, true)
        ''', (author.name.value, author.id.value,))

        self.__db.commit()

        cursor.close()

    def find(self, author_id: AuthorId) -> Author:
        cursor = self.__db.cursor(dictionary=True)

        cursor.execute('''
            SELECT BIN_TO_UUID(id, true) AS id, name
            FROM authors WHERE id = UUID_TO_BIN(%s, true)
        ''', (author_id.value,))

        row = cursor.fetchone()

        self.__logger.info(row)

        cursor.close()

        author = Author.create(id=row['id'], name=row['name'])

        return author

    def delete(self, author_id: AuthorId) -> None:
        cursor = self.__db.cursor()

        cursor.execute('''
            DELETE FROM authors WHERE id = UUID_TO_BIN(%s, true)
        ''', (author_id.value,))

        self.__db.commit()

        cursor.close()
