from __future__ import annotations

from abc import ABC, abstractmethod


# ========= Command ==========
from typing import List


class Command(ABC):
    def __init__(self, receiver: ElectronicEquipment):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class On(Command):
    def execute(self):
        self._receiver.lights_on()

    def __str__(self):
        return f"Command On for {self._receiver.name}"


class Off(Command):
    def execute(self):
        self._receiver.lights_off()

    def __str__(self):
        return f"Command Off for {self._receiver.name}"


# ========= Invoker ==========

class Controller:
    def execute_command(self, command: Command):
        print(f"Execute {command}")
        command.execute()


# ========== Receiver ==========
class ElectronicEquipment(ABC):
    _name = "default"

    @abstractmethod
    def lights_on(self): pass

    @abstractmethod
    def lights_off(self): pass

    @property
    def name(self):
        return self._name


class Lamp(ElectronicEquipment):
    def __init__(self, name: str = "default"):
        self._name = name
        self._is_light_on = False

    def lights_on(self):
        if self._is_light_on:
            return
        print(self._name + ": on")
        self._is_light_on = True

    def lights_off(self):
        if not self._is_light_on:
            return
        print(self._name + ": off")
        self._is_light_on = False


class LightsSystem(ElectronicEquipment):
    def __init__(self, lamps: List[Lamp]):
        self._is_light_on = False
        self._lamps = lamps
        self._name = "Lights System"

    def lights_on(self):
        if self._is_light_on:
            return
        for lamp in self._lamps:
            lamp.lights_on()
        print("The whole system is on")
        self._is_light_on = True

    def lights_off(self):
        if not self._is_light_on:
            return
        for lamp in self._lamps:
            lamp.lights_off()
        print("The whole system is off")
        self._is_light_on = False


if __name__ == '__main__':
    lamp1 = Lamp("lamp1")
    on_command1 = On(lamp1)
    off_command1 = Off(lamp1)

    lamp2 = Lamp("lamp2")

    system = LightsSystem([lamp2, lamp1])
    on_command_system = On(system)
    off_command1_system = Off(system)

    controller = Controller()
    controller.execute_command(on_command1)
    controller.execute_command(on_command_system)
    controller.execute_command(off_command1_system)

# Execute Command On for lamp1
# lamp1: on
# Execute Command On for Lights System
# lamp2: on
# The whole system is on
# Execute Command Off for Lights System
# lamp2: off
# lamp1: off
# The whole system is off
