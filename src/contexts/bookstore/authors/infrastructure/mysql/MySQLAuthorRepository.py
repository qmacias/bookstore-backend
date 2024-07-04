from logging import Logger
from typing import Sequence
from contextlib import contextmanager
from mysql.connector.errors import Error
from mysql.connector.pooling import MySQLConnectionPool

from src.contexts.bookstore.authors.domain.Author import Author
from src.contexts.bookstore.authors.domain.AuthorDoesNotExistsUnknown import AuthorDoesNotExistsUnknown
from src.contexts.bookstore.authors.domain.AuthorId import AuthorId
from src.contexts.bookstore.authors.domain.AuthorName import AuthorName
from src.contexts.bookstore.authors.domain.AuthorNameAlreadyExistsIntegrity import AuthorNameAlreadyExistsIntegrity
from src.contexts.bookstore.authors.domain.AuthorRepository import AuthorRepository
from src.contexts.bookstore.authors.infrastructure.mysql.MySQLAuthorEnviron import MySQLAuthorEnviron


class MySQLAuthorRepository(AuthorRepository):
    def __init__(self, environ: MySQLAuthorEnviron, logger: Logger) -> None:
        self.__pool = MySQLConnectionPool(
            host=environ.host,
            user=environ.user,
            password=environ.password,
            database=environ.database,
            pool_name=environ.pool_name,
            pool_size=environ.pool_size,
        )
        self.__logger = logger

    @contextmanager
    def get_connection(self):
        connection = self.__pool.get_connection()
        try:
            yield connection
        finally:
            connection.close()

    @contextmanager
    def get_cursor(self, connection):
        cursor = connection.cursor(dictionary=True)
        try:
            yield cursor
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()

    def find(self, author_id: AuthorId) -> Author:
        with self.get_connection() as connection:
            with self.get_cursor(connection) as cursor:
                cursor.execute("""
                    SELECT BIN_TO_UUID(id, true) AS id, name
                    FROM authors WHERE id = UUID_TO_BIN(%s, true)
                """, (author_id.value,))

                row = cursor.fetchone()

        if row is None:
            raise AuthorDoesNotExistsUnknown(f"unknown registry: '{author_id.value}'")

        self.__logger.info(f'Retrieved author: {row}')

        return Author.from_primitives(row)

    def find_all(self) -> Sequence[Author]:
        with self.get_connection() as connection:
            with self.get_cursor(connection) as cursor:
                cursor.execute("""
                    SELECT BIN_TO_UUID(id, true) AS id, name
                    FROM authors
                """)

                rows = cursor.fetchall()

        self.__logger.info(f'Retrieved {len(rows)} author/s: {rows}')

        return [Author.from_primitives(row) for row in rows]

    def save(self, author: Author) -> None:
        try:
            with self.get_connection() as connection:
                with self.get_cursor(connection) as cursor:
                    cursor.execute("""
                        INSERT INTO authors (id, name)
                        VALUES (UUID_TO_BIN(%s, true), %s)
                    """, (author.id.value, author.name.value,))

            self.__logger.info(f"Created author with id: '{author.id.value}'")
        except Error as e:
            raise AuthorNameAlreadyExistsIntegrity(str(e))

    def update(self, author: Author) -> None:
        with self.get_connection() as connection:
            with self.get_cursor(connection) as cursor:
                cursor.execute("""
                    UPDATE authors SET name = %s
                    WHERE id = UUID_TO_BIN(%s, true)
                """, (author.name.value, author.id.value,))

        self.__logger.info(f"Updated author with id: '{author.id.value}'")

    def delete(self, author_id: AuthorId) -> None:
        with self.get_connection() as connection:
            with self.get_cursor(connection) as cursor:
                cursor.execute("""
                    DELETE FROM authors
                    WHERE id = UUID_TO_BIN(%s, true)
                """, (author_id.value,))

        self.__logger.info(f"Deleted author with id: '{author_id.value}'")
