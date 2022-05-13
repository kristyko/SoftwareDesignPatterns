from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from beverage_additions import BeverageAddition


class Beverage(ABC):
    def __init__(self, sugar: int = 0, additions: List[BeverageAddition] = None):
        self._sugar = sugar
        self._additions: List[BeverageAddition] = additions

    @property
    def additions_names(self):
        return " ".join([addition.name for addition in self._additions])

    @property
    def additions_cost(self):
        return sum(addition.add_cost() for addition in self._additions)

    @abstractmethod
    def prepare(self):
        for addition in self._additions:
            addition.add()
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class Chocolate(Beverage):
    def drink(self):
        print(f"Drink {self.additions_names} chocolate!")

    def prepare(self):
        print("Put some cacao...")
        super(Chocolate, self).prepare()

    def cost(self):
        return 15 + self.additions_cost


class Coffee(Beverage):
    def drink(self):
        print(f"Drink {self.additions_names} coffee!")

    def prepare(self):
        print("Put some coffee...")
        super(Coffee, self).prepare()

    def cost(self):
        return 10 + self.additions_cost


class Tea(Beverage):
    def drink(self):
        print(f"Drink {self.additions_names} tea!")

    def prepare(self):
        print("Put some tea...")
        super(Tea, self).prepare()

    def cost(self):
        return 7 + self.additions_cost
