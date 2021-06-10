from enum import Enum
from bot.bot_user import BotUser
from bot.bot_environment import BotEnvironment


class User(BotUser):
    class Interest(Enum):
        COMPUTER_SCIENCE = 'a'
        ENGLISH_TALKING = 'b'
        LITERATURE = 'c'
        MATH = 'd'
        POLITICS = 'e'
        PHOTOGRAPHY = 'f'
        PAINTING = 'g'
        ECONOMICS = 'h'
        HISTORY = 'i'
        SPORT = 'j'
        MUSIC = 'k'
        GAMING = 'l'
        MEDICINE = 'm'
        HANDMADE = 'n'
        LOVE = 'o'

        def __str__(self):
            name = self.name.lower().replace('_', ' ')
            name = name[0].upper() + name[1:]
            return name

        @staticmethod
        def contains(char: str):
            return char in (i.value for i in User.Interest)

        @staticmethod
        def presentation() -> str:
            res = ''
            for interest in User.Interest:
                res += interest.value + ': ' + str(interest) + '\n'
            return res

        @staticmethod
        def get_string_list(interests) -> str:
            res = ''
            for interest in interests:
                res += str(User.Interest(interest)) + ', '
            return res[:-2]

    def __init__(self, vk_id: int, environment: BotEnvironment = None,
                 name: str = None, age: int = None,
                 about: str = None, interests: set = None,
                 photo: str = None,
                 fan_ids: set = None):

        super().__init__(vk_id, environment)
        self.id = vk_id

        self.name = name
        self.age = age
        self.about = about
        self.interests = interests if interests is not None else set()  # TODO: ternary operator is bad
        self.photo = photo

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
        return f"User({self.id}, {self.name}, {self.get_keyboard()}, {self.env_vars})"
