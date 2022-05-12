class Salesperson:
    def __init__(self, name, manager):
        self._name = name
        self._manager = manager

    def pay_expenses(self, amount):
        print(f"{self._name} has been paid ${amount}")