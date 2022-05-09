from __future__ import annotations

from threading import Thread

from builder import Pizzaiolo, PizzaBuilder
from pizza import Flour, Product


def _test_pizzaiolo(builder):
    pizzaiolo = Pizzaiolo(builder)
    print(pizzaiolo.builder)


if __name__ == "__main__":
    pizza_builder = PizzaBuilder()
    pizza_builder2 = PizzaBuilder()
    pizza_builder2.set_crust(flour=Flour.GLUTEN_FREE)

    # test Singleton
    print("builder1: ", pizza_builder, "builder2: ", pizza_builder2)
    process1 = Thread(target=_test_pizzaiolo, args=(pizza_builder,))
    process2 = Thread(target=_test_pizzaiolo, args=(pizza_builder2,))
    process1.start()
    process2.start()

    # make pizzas
    pizzaiolo = Pizzaiolo(pizza_builder)

    margherita = pizzaiolo.make_margherita()
    print(margherita)

    # make author pizza
    pizza_builder.set_ingredient(Product.TOMATO_SAUCE)
    pizza_builder.set_ingredient(Product.MOZZARELLA, 2)
    pizza_builder.set_ingredient(Product.BURRATA_CHEESE)
    pizza_builder.set_ingredient(Product.PROSCIUTTO)
    pizza_builder.set_ingredient(Product.OLIVES)
    author_pizza = pizza_builder.bake
    print(author_pizza)
