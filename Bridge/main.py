from beverages import *


def beverage_info(beverage: Beverage):
    print("=========================")
    beverage.prepare()
    print(f"Cost of beverage: {beverage.cost()} grn\n")
    beverage.drink()


if __name__ == "__main__":
    black_chocolate = BlackChocolate(3, 200)
    black_coffee = BlackCoffee(3, 200, True)
    black_tea = BlackTea(0, 300)

    beverage_info(black_chocolate)
    beverage_info(black_coffee)
    beverage_info(black_tea)

    milk_chocolate = MilkChocolate(3, 200)
    coffee_with_milk = CoffeeWithMilk(3, 200)
    tea_with_milk = TeaWithMilk(2, 300)

    beverage_info(milk_chocolate)
    beverage_info(coffee_with_milk)
    beverage_info(tea_with_milk)
