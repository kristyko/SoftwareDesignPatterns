from printable_string import Wrappee


class Decorator(Wrappee):
    def __init__(self, wrappee: Wrappee):
        self._wrappee = wrappee

    @property
    def wrappee(self):
        return self._wrappee

    def print(self):
        return self._wrappee.print()


class PostCommaDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + ", "


class PostEndlDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + "\n"


class PostExclaimDecorator(Decorator):
    def print(self):
        return self._wrappee.print() + "! "


class PostWordDecorator(Decorator):
    def __init__(self, wrappee: Wrappee, post_word: str):
        super().__init__(wrappee)
        self._post_word = post_word

    def print(self):
        return self._wrappee.print() + self._post_word


class PreWordDecorator(Decorator):
    def __init__(self, wrappee: Wrappee, pre_word: str):
        super().__init__(wrappee)
        self._pre_word = pre_word

    def print(self):
        return self._pre_word + self._wrappee.print()
