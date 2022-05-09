from pizza import Pizza, Flour, CrustType, Product
from singleton import SingletonMeta

class PizzaBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()

    @property
    def bake(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def set_name(self, name: str):
        self._product.set_name(name)

    def set_crust(self, flour: Flour = Flour.ALL_PURPOSE, crust_type: CrustType = CrustType.STANDARD):
        self._product.set_crust(flour, crust_type)

    def set_ingredient(self, ingredient: Product, amount: int = 1):
        self._product.add_ingredient(ingredient, amount)


class Pizzaiolo(metaclass=SingletonMeta):
    def __init__(self, builder: PizzaBuilder = PizzaBuilder()) -> None:
        self._builder = builder

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    def make_margherita(self):
        self._builder.set_name("Margherita")
        self._builder.set_crust(Flour.GLUTEN_FREE, CrustType.THIN)
        self._builder.set_ingredient(Product.OLIVE_OIL)
        self._builder.set_ingredient(Product.TOMATO_SAUCE)
        self._builder.set_ingredient(Product.MOZZARELLA)
        self._builder.set_ingredient(Product.BASIL)
        self._builder.set_ingredient(Product.SPICES, 2)
        return self._builder.bake

