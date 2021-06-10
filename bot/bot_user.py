from bot.bot_environment import BotEnvironment


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


class BotUser:
    def __init__(self, vk_id: int, environment: BotEnvironment):
        self.id = vk_id
        self.env_vars = EnvironmentVariables()

        self._environments_stack = []
        self._environments_stack.append(environment)

    def go_to(self, environment):
        self._environments_stack.append(environment)

    def go_back(self):
        self._environments_stack.pop()

    def get_keyboard(self):
        return self.get_environment().value[1]

    def get_environment(self):
        return self._environments_stack[-1]
