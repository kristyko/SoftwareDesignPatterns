from collections import namedtuple, defaultdict
from enum import Enum


class Product(Enum):
    # class to define costs of products
    SPICES = 0.1
    BASIL = 0.15
    OLIVE_OIL = 0.2
    TOMATO_SAUCE = 0.25
    OLIVES = 0.5
    MOZZARELLA = 0.6
    BURRATA_CHEESE = 0.8
    PARMESAN = 0.9
    PROSCIUTTO = 1


class Flour(Enum):
    ALL_PURPOSE = 1
    WHOLE_WHEAT = 1.2
    GLUTEN_FREE = 1.5


class CrustType(Enum):
    THIN = 1
    STANDARD = 1.3
    WITH_CHEESE = 2


class PizzaCrust(namedtuple("PizzaCrust", ["flour", "cr_type"])):
    @property
    def cost(self):
        return self.flour.value * self.cr_type.value

    def __str__(self):
        return f"Crust: {self.flour.name.lower()} flour, {self.cr_type.name.lower()}"


class Pizza:
    def __init__(self) -> None:
        self._crust = PizzaCrust(Flour.ALL_PURPOSE, CrustType.STANDARD)  # default crust
        self._ingredients = defaultdict(int)
        self._name = ""

    def set_name(self, name):
        self._name = name

    def set_crust(self, flour: Flour, crust_type: CrustType) -> None:
        self._crust = PizzaCrust(flour, crust_type)

    def add_ingredient(self, ingredient: Product, amount: int) -> None:
        assert isinstance(ingredient, Product) and amount > 0
        self._ingredients[ingredient] += amount

    @property
    def cost(self):
        return self._crust.cost + sum([amount * product.value for product, amount in self._ingredients.items()])

    def _get_str(self):
        return (
            f"PIZZA {self._name}:\n  {self._crust}\n"
            f"  Ingredients: "
            f"{'; '.join([f'{product.name.lower()} x {amount}' for product, amount in self._ingredients.items()])}\n"
            f"  Cost: {self.cost}"
        )

    def __str__(self):
        return self._get_str()

    def __repr__(self):
        return self._get_str()
