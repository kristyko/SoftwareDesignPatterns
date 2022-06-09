from __future__ import annotations

from abc import ABC


class State(ABC):
    def turn_up(self, fan: Fan): pass

    def turn_down(self, fan: Fan): pass


class Low(State):
    def turn_up(self, fan):
        fan.set_state(Medium())
        print("Fan is on medium")


class Medium(State):
    def turn_up(self, fan):
        fan.set_state(High())
        print("Fan is on high")

    def turn_down(self, fan):
        fan.set_state(Low())
        print("Fan is on low")


class High(State):
    def turn_down(self, fan):
        fan.set_state(Medium())
        print("Fan is on medium")


class Fan:
    _state = Low()

    def set_state(self, state: State):
        self._state = state

    @property
    def state(self):
        return self._state

    def turn_up(self):
        self._state.turn_up(self)

    def turn_down(self):
        self._state.turn_down(self)


if __name__ == '__main__':
    fan = Fan()
    fan.turn_up()
    fan.turn_up()
    fan.turn_down()
    fan.turn_down()
    fan.turn_down()
    fan.turn_up()

# Fan is on medium
# Fan is on high
# Fan is on medium
# Fan is on low
# Fan is on medium