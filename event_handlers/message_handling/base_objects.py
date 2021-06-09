from bot.dating_bot import DatingBot


def static_singleton(klass):
    return klass()


class MessageHandler:
    def __init__(self):
        self.callback_environments = {}
        self.input_environments = {}

    def callback_environment(self, name):
        def decorator(klass):
            self.callback_environments[name] = static_singleton(klass)
            return self.callback_environments[name]
        return decorator

    def input_environment(self, name):
        def decorator(klass):
            self.input_environments[name] = static_singleton(klass)
            return self.input_environments[name]
        return decorator

    def handle(self, bot: DatingBot, message):
        raise NotImplementedError()

    def initialize(self):
        raise NotImplementedError()


class CallbackEnvironment:
    def __init__(self):
        self.callback_methods = {}

    def initialize_methods(self):
        raise NotImplementedError()

    def callback_method(self, name):
        def decorator(method):
            self.callback_methods[name] = method
            return method
        return decorator


class InputEnvironment:
    def input(self, bot, user, bundle):
        raise NotImplementedError()
