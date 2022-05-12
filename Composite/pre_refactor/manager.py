class Manager:
    def __init__(self, name):
        self._name = name

    def pay_expenses(self, amount):
        print(f"{self._name} has been paid ${amount}")
