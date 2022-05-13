from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def description(self) -> str: pass

    @abstractmethod
    def cost(self) -> float: pass

    def __str__(self):
        return f"Beverage: {self.description()}; ${self.cost()}"


class Espresso(Beverage):
    def description(self) -> str:
        return "Espresso"

    def cost(self) -> float:
        return 0.75


class DarkRoast(Beverage):
    def description(self) -> str:
        return "Dark Roast"

    def cost(self) -> float:
        return 1.


class Decaf(Beverage):
    def description(self) -> str:
        return "Decaf"

    def cost(self) -> float:
        return 0.5
