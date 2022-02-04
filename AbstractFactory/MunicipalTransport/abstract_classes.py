from __future__ import annotations
from abc import abstractmethod, ABC


class PublicTransport(ABC):
    """
    Helper class that has common properties of different transport types.
    """
    _cost: int
    _usage_cost: int

    def __init__(self, cost, usage_cost):
        self._cost = cost
        self._usage_cost = usage_cost

    def get_cost(self) -> int:
        return self._cost

    def get_usage_cost(self) -> int:
        return self._usage_cost


class Bus(ABC, PublicTransport):

    @abstractmethod
    def go_by_road(self):
        pass


class Tram(ABC, PublicTransport):

    @abstractmethod
    def go_by_rails(self):
        pass


class Trolley(ABC, PublicTransport):

    @abstractmethod
    def go_by_contact_network(self):
        pass


class TransportFactory(ABC):

    @abstractmethod
    def create_bus(self) -> Bus:
        pass

    @abstractmethod
    def create_tram(self) -> Tram:
        pass

    @abstractmethod
    def create_trolley(self) -> Trolley:
        pass