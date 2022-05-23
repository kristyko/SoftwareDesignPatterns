from enum import Enum
from typing import Tuple, Dict


class Fuel(Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"


class Engine:
    _power: int
    _fuel: Fuel

    def __init__(self, power: int, fuel: Fuel = Fuel.PETROL):
        self._power = power
        self._fuel = fuel

    def __str__(self):
        return f"Engine power={self._power}, fuel={self._fuel.value}, hash={hash(self)}"


class EngineFactory:
    _engines: Dict[Tuple[int, Fuel], Engine] = {}

    def get_engine(self, power: int = 105, fuel: Fuel = Fuel.PETROL) -> Engine:
        param = (power, fuel)
        if param in self._engines.keys():
            return self._engines.get(param)
        new_engine = Engine(power, fuel)
        self._engines[param] = new_engine
        return new_engine