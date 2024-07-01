from src.contexts.bookstore.shared.infrastructure.EnvironLector import EnvironLector
from src.contexts.bookstore.shared.infrastructure.EnvironVariable import EnvironVariable


class MySQLAuthorEnviron:
    def __init__(self, host, user, password, database) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._database = database

    @staticmethod
    def create() -> 'MySQLAuthorEnviron':
        environ = MySQLAuthorEnviron(
            host=EnvironLector.get(EnvironVariable.MYSQL_HOST),
            user=EnvironLector.get(EnvironVariable.MYSQL_USER),
            password=EnvironLector.get(EnvironVariable.MYSQL_PASSWORD),
            database=EnvironLector.get(EnvironVariable.MYSQL_DATABASE),
        )

        return environ

    @property
    def host(self) -> str:
        return self._host

    @property
    def user(self) -> str:
        return self._user

    @property
    def password(self) -> str:
        return self._password

    @property
    def database(self) -> str:
        return self._database
