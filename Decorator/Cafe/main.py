from beverages import *
from add_ons import *

if __name__ == '__main__':
    # · Еспресо з двома порціями цукру.
    espresso = Espresso()
    espresso = Sugar(espresso, 2)
    print(espresso)

    # · Чорну каву з вершками та двома порціями цукру.
    coffee = DarkRoast()
    coffee = Whip(coffee)
    coffee = Sugar(coffee, 2)
    print(coffee)

    # · Чорну каву з кремом та порцією цукру.
    coffee = DarkRoast()
    coffee = Creme(coffee)
    coffee = Sugar(coffee)
    print(coffee)

    # · Кава без кофеїну з молоком та двома порціями цукру.
    coffee = Decaf()
    coffee = Milk(coffee)
    coffee = Sugar(coffee, 2)
    print(coffee)


# output:
# Beverage: Espresso, sugar x 2; $0.75
# Beverage: Dark Roast, whip, sugar x 2; $1.4
# Beverage: Dark Roast, creme, sugar x 1; $1.5
# Beverage: Decaf, milk, sugar x 2; $0.7
