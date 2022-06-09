from __future__ import annotations

from abc import ABC, abstractmethod


# ========= Command ==========

class Command(ABC):
    def __init__(self, receiver: Lamp):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class On(Command):
    def execute(self):
        self._receiver.light_on()


class Off(Command):
    def execute(self):
        self._receiver.light_off()


# ========= Invoker ==========

class Controller:
    def __init__(self, on_command: On, off_command: Off):
        self._on_command = on_command
        self._off_command = off_command

    def on(self):
        self._on_command.execute()

    def off(self):
        self._off_command.execute()


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
    on_command = On(lamp)
    off_command = Off(lamp)
    controller = Controller(on_command, off_command)

    controller.on()
    controller.on()
    controller.off()
    controller.off()
    controller.on()
    controller.on()
    controller.off()

# default: Light is on
# default: Light is off
# default: Light is on
# default: Light is off
