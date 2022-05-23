from enum import Enum

from engine import Engine, Fuel, EngineFactory
from wheel import Wheel, WheelFactory


class CarColor(Enum):
    WHITE = "White"
    BLACK = "Black"
    RED = "Red"
    GREY = "Grey"


class CarType(Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"


class Car:
    def __init__(self, car_type: CarType, car_color: CarColor, engine: Engine, wheel: Wheel):
        self._car_type = car_type
        self._car_color = car_color
        self._engine = engine
        self._wheel = wheel

    def showInfo(self):
        print(
            "Car:\n" +
            f" type={self._car_type.value},\n"
            f" car_color={self._car_color.value},\n"
            f" engine={self._engine},\n"
            f" wheel={self._wheel}\n"
            f" hash={hash(self)}\n"
        )


class CarBuilder:
    _car_type: CarType
    _car_color: CarColor
    _engine: Engine
    _wheel: Wheel

    def __init__(self, engine_factory=EngineFactory(), wheel_factory=WheelFactory()):
        self._engine_factory = engine_factory
        self._wheel_factory = wheel_factory
        self.reset()

    def reset(self):
        self._car_type = CarType.SEDAN
        self._car_color = CarColor.WHITE
        self._engine = self._engine_factory.get_engine(105, Fuel.PETROL)
        self._wheel = self._wheel_factory.get_wheel(17)
        return self

    def set_type(self, car_type):
        self._car_type = car_type
        return self

    def set_car_color(self, car_color):
        self._car_color = car_color
        return self

    def set_engine(self, power=None, fuel=None):
        self._engine = self._engine_factory.get_engine(power, fuel)
        return self

    def set_wheel(self, diameter=None, material=None):
        self._wheel = self._wheel_factory.get_wheel(diameter, material)
        return self

    def build(self):
        if not (self._car_type and self._car_color and self._engine and self._wheel):
            raise Exception
        return Car(self._car_type, self._car_color, self._engine, self._wheel)
