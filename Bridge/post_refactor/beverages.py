from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from order_type import OrderType, TakeIn
from beverage_additions import BeverageAddition


class Beverage(ABC):
    def __init__(
            self, sugar: int = 0, additions: List[BeverageAddition] = None, order_type: OrderType = TakeIn()
    ):
        self._sugar = sugar
        self._additions = additions
        self._order_type = order_type

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
        print(f"Drink {self.additions_names} chocolate {self._order_type.where()}!")

    def prepare(self):
        self._order_type.prepare_cup()
        print("Put some cacao...")
        super(Chocolate, self).prepare()

    def cost(self):
        return 15 + self.additions_cost


class Coffee(Beverage):
    def drink(self):
        print(f"Drink {self.additions_names} coffee {self._order_type.where()}!")

    def prepare(self):
        self._order_type.prepare_cup()
        print("Put some coffee...")
        super(Coffee, self).prepare()

    def cost(self):
        return 10 + self.additions_cost


class Tea(Beverage):
    def drink(self):
        print(f"Drink {self.additions_names} tea {self._order_type.where()}!")

    def prepare(self):
        self._order_type.prepare_cup()
        print("Put some tea...")
        super(Tea, self).prepare()

    def cost(self):
        return 7 + self.additions_cost
