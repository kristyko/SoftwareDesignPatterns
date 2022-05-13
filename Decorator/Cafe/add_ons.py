from beverages import Beverage


class AddOnDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage


class Milk(AddOnDecorator):
    def description(self) -> str:
        return self._beverage.description() + ", milk"

    def cost(self) -> float:
        return self._beverage.cost() + 0.2


class Sugar(AddOnDecorator):
    def __init__(self, beverage: Beverage, amount: int = 1):
        super().__init__(beverage)
        self._amount = amount

    def description(self) -> str:
        return self._beverage.description() + f", sugar x {self._amount}"

    def cost(self) -> float:
        return self._beverage.cost()


class Creme(AddOnDecorator):
    def description(self) -> str:
        return self._beverage.description() + ", creme"

    def cost(self) -> float:
        return self._beverage.cost() + 0.5


class Whip(AddOnDecorator):
    def description(self) -> str:
        return self._beverage.description() + ", whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.4