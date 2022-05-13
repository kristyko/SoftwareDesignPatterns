from abc import ABC, abstractmethod


class BeverageAddition(ABC):
    @property
    def name(self):
        return ""

    @abstractmethod
    def add(self):
        return

    def add_cost(self):
        return 0


class MilkAddition(BeverageAddition):
    def __init__(self, volume: int):
        self._volume = volume

    @property
    def name(self):
        return "milk"

    def add(self):
        print(f"Put some milk : {self._volume} ml...")

    def add_cost(self):
        return int(self._volume / 20)


class WaterAddition(BeverageAddition):
    def __init__(self, volume: int):
        self._volume = volume

    def add(self):
        print(f"Put some hot water : {self._volume} ml...")


class ExtraAddition(BeverageAddition):
    @property
    def name(self):
        return "black"

    def add(self):
        print("Put extra dose...")
