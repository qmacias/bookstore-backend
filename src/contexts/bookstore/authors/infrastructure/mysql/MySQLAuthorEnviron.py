from src.contexts.bookstore.shared.infrastructure.EnvironLector import EnvironLector
from src.contexts.bookstore.shared.infrastructure.EnvironVariable import EnvironVariable


class MySQLAuthorEnviron:
    def __init__(self, host, user, password, database, pool_name, pool_size) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._pool_name = pool_name
        self._pool_size = pool_size

    @staticmethod
    def create() -> 'MySQLAuthorEnviron':
        environ = MySQLAuthorEnviron(
            host=EnvironLector.get(EnvironVariable.MYSQL_HOST),
            user=EnvironLector.get(EnvironVariable.MYSQL_USER),
            password=EnvironLector.get(EnvironVariable.MYSQL_PASSWORD),
            database=EnvironLector.get(EnvironVariable.MYSQL_DATABASE),
            pool_name=EnvironLector.get(EnvironVariable.MYSQL_POOL_NAME),
            pool_size=EnvironLector.get(EnvironVariable.MYSQL_POOL_SIZE, parser=int)
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

    @property
    def pool_name(self) -> str:
        return self._pool_name

    @property
    def pool_size(self) -> int:
        return self._pool_size
