from __future__ import annotations

from abc import ABC, abstractmethod


# ========= Command ==========

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class On(Command):
    def __init__(self, receiver: Lamp):
        self._receiver = receiver

    def execute(self):
        self._receiver.light_on()


class Off(Command):
    def __init__(self, receiver: Lamp):
        self._receiver = receiver

    def execute(self):
        self._receiver.light_off()


# ========= Invoker ==========

class Controller:
    def on(self, command: On):
        command.execute()

    def off(self, command: Off):
        command.execute()


# ========== Receiver ==========

class Lamp:
    def __init__(self, name: str = "default"):
        self._name = name
        self._is_light_on = False

    def light_on(self):
        if self._is_light_on:
            return
        print(self._name + ": Light is on")
        self._is_light_on = True

    def light_off(self):
        if not self._is_light_on:
            return
        print(self._name + ": Light is off")
        self._is_light_on = False


if __name__ == '__main__':
    lamp = Lamp()
    controller = Controller()
    on_command = On(lamp)
    off_command = Off(lamp)

    controller.on(on_command)
    controller.on(on_command)
    controller.off(off_command)
    controller.off(off_command)
    controller.on(on_command)
    controller.on(on_command)
    controller.off(off_command)
