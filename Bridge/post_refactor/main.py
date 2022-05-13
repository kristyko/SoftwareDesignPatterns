from beverage_additions import WaterAddition, ExtraAddition, MilkAddition
from beverages import Beverage, Coffee, Chocolate, Tea


def beverage_info(beverage: Beverage):
    print("=========================")
    beverage.prepare()
    print(f"Cost of beverage: {beverage.cost()} grn\n")
    beverage.drink()


if __name__ == '__main__':
    black_chocolate = Chocolate(3, [WaterAddition(200)])
    black_coffee = Coffee(3, [ExtraAddition(), WaterAddition(200)])
    black_tea = Tea(0, [WaterAddition(300)])

    beverage_info(black_chocolate)
    beverage_info(black_coffee)
    beverage_info(black_tea)

    milk_chocolate = Chocolate(3, [MilkAddition(200)])
    coffee_with_milk = Coffee(3, [MilkAddition(200)])
    tea_with_milk = Tea(2, [MilkAddition(300)])

    beverage_info(milk_chocolate)
    beverage_info(coffee_with_milk)
    beverage_info(tea_with_milk)
