from abc import ABC, abstractmethod

from .vehicles import Vehicle, Car, Truck


class VehicleCalculator(ABC):
    @abstractmethod
    def set_vehicle(self, vehicle: Vehicle) -> None:
        pass

    @abstractmethod
    def calculate_price(self) -> str:
        pass


class CarCalculator(VehicleCalculator):
    average_car_price = 6000

    def __init__(self):
        self._vehicle = None

    def get_retail_price(self) -> int:
        assert self._vehicle is not None

        model = self._vehicle.get_model()
        if model == "Ford":
            return 3000
        if model == "Audi":
            return 5000
        if model == "BMW":
            return 7000
        if model == "Tesla":
            return 10000
        return CarCalculator.average_car_price

    def set_vehicle(self, vehicle: Car):
        self._vehicle = vehicle

    def calculate_price(self) -> str:
        assert self._vehicle is not None

        vehicle = self._vehicle
        # the formula is modified, otherwise I got 0 USD for non-damaged car
        price = ((1 - vehicle.get_damage()) * max(self.get_retail_price() - (vehicle.get_age() * 100), 0))
        return str(price) + "USD"


class TruckCalculator(VehicleCalculator):
    average_price = 10000

    def __init__(self):
        self._vehicle = None

    def set_vehicle(self, vehicle: Truck):
        self._vehicle = vehicle

    def calculate_price(self) -> str:
        vehicle = self._vehicle
        assert vehicle is not None

        price = max(TruckCalculator.average_price - vehicle.get_age() * 100 - vehicle.get_mileage() / 100, 0)
        return str(price) + "USD"
