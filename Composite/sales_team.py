from typing import List

from SoftwareDesignPatterns.Composite.manager import Manager
from SoftwareDesignPatterns.Composite.salesperson import Salesperson


class SalesTeam:
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
