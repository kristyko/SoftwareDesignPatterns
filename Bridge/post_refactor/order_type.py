from abc import ABC, abstractmethod


class OrderType(ABC):
    @abstractmethod
    def prepare_cup(self):
        pass

    @abstractmethod
    def where(self) -> str:
        pass


class TakeIn(OrderType):
    def prepare_cup(self):
        print("Get cup ready...")

    def where(self) -> str:
        return "inside"


class TakeOut(OrderType):
    def prepare_cup(self):
        print("Get paper cup ready...")

    def where(self) -> str:
        return "on the go"
