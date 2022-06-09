from __future__ import annotations
from typing import List


class Runway:
    def __init__(self, runway_id: int):
        self._is_available = True
        self._id = runway_id

    @property
    def id(self):
        return self._id

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, is_available: bool):
        self._is_available = is_available


class Mediator:
    _runways: List[Runway] = []
    _planes_in_flight: List[Plane] = []
    _planes_on_the_ground: List[Plane] = []

    def take_off(self):



class Plane:
    def __init__(self, id: int, runway_id: int, mediator: Mediator):
        self._id = id
        self._runway_id = runway_id
        self._isInTheAir = False
        self._mediator = mediator

    def take_off(self):
        # mediator.
        self._isInTheAir = True
        self._mediator.take_off(self)

    @property
    def isInTheAir(self):
        return self._isInTheAir

    @isInTheAir.setter
    def isInTheAir(self, isInTheAir: bool):
        self._isInTheAir = isInTheAir

    @property
    def id(self):
        return self._id