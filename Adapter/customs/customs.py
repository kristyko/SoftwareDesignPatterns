from abc import ABC, abstractmethod

from auto import Auto


class Customs(ABC):
    @abstractmethod
    def vehicle_price(self, auto: Auto):
        pass

    @abstractmethod
    def tax(self, auto: Auto):
        pass
