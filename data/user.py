from enum import IntEnum


class User:
    class Environment(IntEnum):
        BEGINNING = 0
        SETTINGS = 1
        SETTINGS_NAME = 2
        SETTINGS_AGE = 3
        SETTINGS_ABOUT = 4
        SETTINGS_INTERESTS = 5
        SETTINGS_PHOTO = 6
        MAIN_MENU = 7
        SEARCHING_FRIEND = 8
        SEARCHING_CHAT = 9
        CHATTING = 10

    class Interest(IntEnum):
        PROGRAMMING = 0
        ENGLISH_TALKING = 1
        LITERATURE = 2
        MATH = 3
        POLITICS = 4
        PHOTOGRAPHY = 5
        PAINTING = 6
        ECONOMICS = 7
        HISTORY = 8
        SPORT = 9
        MUSIC = 10

        def __str__(self):
            name = self.name.lower().replace('_', ' ')
            name = name[0].upper() + name[1:]
            return name

        @staticmethod
        def contains(num: int):
            return num in User.Interest._member_map_.values()

        @staticmethod
        def presentation() -> str:
            res = ''
            for i in map(int, User.Interest):
                res += str(i) + ': ' + str(User.Interest(i)) + '\n'
            return res

        @staticmethod
        def get_string_list(interests) -> str:
            res = ''
            for interest in interests:
                res += str(User.Interest(interest)) + ', '
            return res[:-2]

    class EnvironmentVariables:
        # v.var_name = value
        def add(self, var_name: str, value=None):
            self.__dict__ += {var_name: value}

        # del v.var_name
        def remove(self, var_name: str):
            self.__dict__.pop(var_name)

        def clear(self):
            self.__dict__.clear()

        def __repr__(self):
            return repr(self.__dict__)

    def __init__(self, _id: int, env_type: Environment = None,
                 name: str = None, age: int = None, about: str = None,
                 interests: set = None, photo: str = None, fan_ids: set = None):

        self.id = _id

        self.name = name
        self.age = age
        self.about = about
        self.interests = interests if interests is not None else set()  # TODO: ternary operator is bad
        self.photo = photo
        self.env_type = env_type

        # Environment variables specified for Environment type
        self.env_vars = User.EnvironmentVariables()

        # TODO: maybe save it somewhere?
        self.liked_user_ids = set()

        # set<int> ids of users who liked this object
        if fan_ids is None:
            fan_ids = set()
        self.fan_ids = fan_ids

    def clear_env_vars(self):
        self.env_vars = dict()

    def like(self, user):
        # TODO: who is responsible for liking people
        # TODO: User or DatingBot?
        user.fan_ids.add(self.id)

    def account_info(self):
        return f"\n{self.name}, {self.age}\n\n" \
               f"\"{self.about}\"\n\n" \
               f"Interests:\n" \
               f"{str(User.Interest.get_string_list(self.interests))}\n"

    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.env_type}, {self.env_vars})"
