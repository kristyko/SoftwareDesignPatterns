from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, sugar):
        self._sugar = sugar

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def cost(self):
        pass


#===============Chocolate=================


class Chocolate(Beverage, ABC):
    def __init__(self, sugar):
        super().__init__(sugar)

    def prepare(self):
        print("Put some cacao...")

    def cost(self):
        return 15


class MilkChocolate(Chocolate):
    def __init__(self, sugar, milk_volume):
        super().__init__(sugar)
        self._milk_volume = milk_volume

    def drink(self):
        print("Drink milk chocolate!")

    def prepare(self):
        super().prepare()
        print(f"Put some milk : {self._milk_volume} ml...")
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost() + int(self._milk_volume / 20)


class BlackChocolate(Chocolate):
    def __init__(self, sugar, water_volume):
        super().__init__(sugar)
        self._water_volume = water_volume

    def drink(self):
        print("Drink chocolate beverage!")

    def prepare(self):
        super().prepare()
        print(f"Put some hot water : {self._water_volume} ml...")
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost()


# ===============Coffee=================

class Coffee(Beverage, ABC):
    def __init__(self, sugar):
        super().__init__(sugar)

    def prepare(self):
        print("Put some coffee...")

    def cost(self):
        return 10


class BlackCoffee(Coffee):
    def __init__(self, sugar, water_volume, extra_coffee):
        super().__init__(sugar)
        self._water_volume = water_volume
        self._extra_coffee = extra_coffee

    def drink(self):
        print("Drink black coffee!")

    def prepare(self):
        super().prepare()
        if self._extra_coffee:
            print(f"Put extra coffee...")
        print(f"Put some hot water : {self._water_volume} ml...")
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost()


class CoffeeWithMilk(Coffee):
    def __init__(self, sugar, milk_volume):
        super().__init__(sugar)
        self._milk_volume = milk_volume

    def drink(self):
        print("Drink coffee with milk!")

    def prepare(self):
        super().prepare()
        print(f"Put some milk : {self._milk_volume} ml...")
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost() + int(self._milk_volume / 20)


# ===============Tea=================

class Tea(Beverage, ABC):
    def __init__(self, sugar):
        super().__init__(sugar)

    def prepare(self):
        print("Put some tea...")

    def cost(self):
        return 7


class TeaWithMilk(Tea):
    def __init__(self, sugar, milk_volume):
        super().__init__(sugar)
        self._milk_volume = milk_volume

    def drink(self):
        print("Drink tea with milk!")

    def prepare(self):
        super().prepare()
        print(f"Put some milk : {self._milk_volume} ml...", )
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost() + int(self._milk_volume / 20.0)


class BlackTea(Tea):
    def __init__(self, sugar, water_volume):
        super().__init__(sugar)
        self._water_volume = water_volume

    def drink(self):
        print("Drink black tea!")

    def prepare(self):
        super().prepare()
        print("Put extra tea...")
        print(f"Put some hot water : {self._water_volume} ml...", )
        if self._sugar > 0:
            print(f"Put some sugar: {self._sugar} pieces ...")

    def cost(self):
        return super().cost()
