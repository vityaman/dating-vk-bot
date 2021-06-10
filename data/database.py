import config
import psycopg2

from bot.bot_environment import BotEnvironment
from data.user import User
from utils import MetaSingleton


def set_to_str(st: set, sep='|'):
    res = ''
    for e in st:
        res += str(e) + sep
    return res[:-1].replace("'", "")


def str_to_set(string: str, type_cast, sep='|') -> set:
    res = set()
    for e in string.split(sep):
        if e != '':
            res.add(type_cast(e))
    return res


def db_row_to_user(db_row: tuple):
    return User(vk_id=db_row[0],
                environment=BotEnvironment.USER_MAIN_MENU,
                name=db_row[1],
                age=db_row[2],
                about=db_row[3],
                interests=str_to_set(db_row[4], type_cast=str),
                photo=db_row[5])


class Database(metaclass=MetaSingleton):
    USERS_TABLE = "users"

    def __init__(self):
        self.database = psycopg2.connect(config.DATABASE_URL, sslmode='require')
        self.cursor = self.database.cursor()

        self._initialize_if_first_create()

    def _initialize_if_first_create(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.USERS_TABLE} ("
            f"id INTEGER PRIMARY KEY, "
            f"name TEXT, "
            f"age INTEGER, "
            f"about TEXT, "
            f"interests TEXT, "
            f"photo TEXT);"
        )
        self.database.commit()

    def insert_user(self, user: User):
        self.cursor.execute(
            f"INSERT INTO {self.USERS_TABLE} "
            f"(id, name, age, about, interests, photo) "
            f"VALUES ({user.id}, '{user.name}', {user.age}, "
            f"'{user.about}', '{set_to_str(user.interests)}', '{user.photo}');"
        )
        self.database.commit()

    def update_user(self, user: User):
        self.cursor.execute(
            f"UPDATE {self.USERS_TABLE} "
            f"SET name =       '{user.name}', "
            f"    age =         {user.age}, "
            f"    about =      '{user.about}', "
            f"    interests =  '{set_to_str(user.interests)}', "
            f"    photo =      '{user.photo}'"
            f"WHERE id = {user.id};"
        )
        self.database.commit()

    def delete_user_by_id(self, _id: int):
        self.cursor.execute(
            f"DELETE FROM {self.USERS_TABLE} WHERE id = {_id}"
        )
        self.database.commit()

    def get_user_by_id(self, _id: int) -> User:
        self.cursor.execute(
            f"SELECT * FROM {self.USERS_TABLE} WHERE id = {_id}"
        )
        user = self.cursor.fetchone()
        if user:
            return db_row_to_user(user)
        raise self.NoSuchUserException("No such user in table!")

    def all_users(self):
        self.cursor.execute(f"SELECT * FROM {self.USERS_TABLE}")
        for row in self.cursor.fetchall():
            yield db_row_to_user(row)

    class NoSuchUserException(Exception):
        pass

    def close(self):
        self.cursor.close()
        self.database.commit()
        self.database.close()
