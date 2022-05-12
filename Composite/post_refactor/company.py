from abc import ABC
from typing import List


class WorkingUnit(ABC):
    def pay_expenses(self, amount):
        print(f"has been paid ${amount}")


class Manager(WorkingUnit):
    def __init__(self, name: str):
        self._name = name

    def pay_expenses(self, amount):
        print(self._name, end=" ")
        super().pay_expenses(amount)


class Salesperson(WorkingUnit):
    def __init__(self, name: str, manager: Manager):
        self._name = name
        self._manager = manager

    def pay_expenses(self, amount):
        print(self._name, end=" ")
        super().pay_expenses(amount)


class SalesTeam(WorkingUnit):
    # it's not clear from the task, whether it is allowed to have a sub-team,
    # so the classes' relation structure isn't really *recursive* as explained on the refactoring_guru
    def __init__(self):
        self._managers: List[Manager] = []
        self._salespeople: List[Salesperson] = []

    def add_manager(self, manager):
        self._managers.append(manager)

    def add_salesperson(self, salesperson):
        self._salespeople.append(salesperson)

    def pay_expenses(self, amount):
        for manager in self._managers:
            manager.pay_expenses(amount)

        for salesperson in self._salespeople:
            salesperson.pay_expenses(amount)
