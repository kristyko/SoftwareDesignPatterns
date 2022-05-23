from car import CarBuilder, CarColor
from engine import Fuel


def build_random_car():
    pass


if __name__ == '__main__':
    car_builder = CarBuilder()
    car1 = car_builder.build()
    car1.showInfo()

    car_builder.reset()
    car_builder.set_car_color(CarColor.BLACK)
    car2 = car_builder.build()
    car2.showInfo()

    car_builder.reset()
    car_builder.set_engine(150, Fuel.ELECTRIC)
    car3 = car_builder.build()
    car3.showInfo()
