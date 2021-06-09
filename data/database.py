import os
import sqlite3
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
    return User(_id=db_row[0],
                env_type=User.Environment.MAIN_MENU,
                name=db_row[1],
                age=db_row[2],
                about=db_row[3],
                interests=str_to_set(db_row[4], type_cast=int),
                photo=db_row[5])


class Database(metaclass=MetaSingleton):
    DATABASE_FILE_NAME = os.path.join(os.path.dirname(__file__), "database")
    USERS_TABLE = "users"

    def __init__(self):
        self.database = sqlite3.connect(self.DATABASE_FILE_NAME)
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

    def __del__(self):
        self.cursor.close()
        self.database.commit()
        self.database.close()

    def insert_user(self, user: User):
        self.cursor.execute(
            f"INSERT INTO {self.USERS_TABLE} "
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

    def insert_or_update_user(self, user: User):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO {self.USERS_TABLE} "
            f"VALUES ({user.id}, '{user.name}', {user.age}, "
            f"'{user.about}', '{set_to_str(user.interests)}', "
            f"'{user.photo}');"
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
        users = self.cursor.fetchall()
        if len(users) == 1:
            return db_row_to_user(users[0])
        raise self.NoSuchUserException("No such user in table!")

    def all_users(self):
        for row in self.cursor.execute(f"SELECT * FROM {self.USERS_TABLE}"):
            yield db_row_to_user(row)

    class NoSuchUserException(Exception):
        pass
