from abc import ABC, abstractmethod


class Wrappee(ABC):
    @abstractmethod
    def print(self):
        pass


class PrintableString(Wrappee):
    def __init__(self, string: str):
        self._base = string

    def print(self):
        return self._base
