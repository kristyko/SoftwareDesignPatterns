from abc import ABC, abstractmethod

from .auto import Auto
from ..vehicle_calculator.calculators import CarCalculator, TruckCalculator
from ..vehicle_calculator.vehicles import Car, Truck


class Customs(ABC):
    @abstractmethod
    def vehicle_price(self, auto: Auto):
        pass

    @abstractmethod
    def tax(self, auto: Auto):
        pass


class CustomsAdapter(Customs):
    _usd2uah = 8.  # Yes, contra spem spero :)
    _tax_coeff = 0.15

    def _vehicle_price_bare(self, auto: Auto) -> float:
        if auto.model == "truck":
            calculator = TruckCalculator()
            vehicle = Truck(age=auto.age, mileage=auto.mileage)
        else:
            calculator = CarCalculator()
            vehicle = Car(age=auto.age, model=auto.model, damage=auto.damaged)

        calculator.set_vehicle(vehicle)
        usd_price = float(calculator.calculate_price()[:-3])
        return usd_price * self._usd2uah

    def vehicle_price(self, auto: Auto) -> str:
        return str(self._vehicle_price_bare(auto)) + "UAH"

    def tax(self, auto: Auto) -> str:
        return str(self._vehicle_price_bare(auto) * self._tax_coeff) + "UAH"

