from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: pass

    @abstractmethod
    def handle(self, *args) -> Optional[int]: pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self,  a: int, b: int, action: str) -> Optional[int]:
        if self._next_handler:
            return self._next_handler.handle(a, b, action)
        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class SumHandler(AbstractHandler):
    def handle(self,  a: int, b: int, action: str):
        if action in ["+", "plus"]:
            print(f"  performing summation: {a}+{b} =", end="")
            return a + b
        else:
            return super().handle(a, b, action)


class SubtractHandler(AbstractHandler):
    def handle(self,  a: int, b: int, action: str):
        if action in ["-", "minus"]:
            print(f"  performing subtraction: {a}-{b} =", end="")
            return a - b
        else:
            return super().handle(a, b, action)


class MultiplyHandler(AbstractHandler):
    def handle(self, a: int, b: int, action: str):
        if action in ["+", "plus"]:
            print(f"  performing multiplication: {a}*{b} =", end="")
            return a * b
        else:
            return super().handle(a, b, action)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    tasks = [
        (4, 5, "minus"),
        (4, 5, "/"),
        (4, 5, "plus"),
    ]
    for a, b, operation in tasks:
        print(f"\nClient: Process {a, b, operation}...")
        result = handler.handle(a, b, operation)
        if result:
            print(f"  {result}")
        else:
            print(f"  operation {operation} is unknown to handler", end="")


if __name__ == "__main__":
    plus = SumHandler()
    minus = SubtractHandler()
    multiply = MultiplyHandler()

    plus.set_next(minus).set_next(multiply)
    print("Chain: Plus > Minus > Multiply")
    client_code(plus)

# Client: Process (4, 5, 'minus')...
#   performing subtraction: 4-5 =  -1
# Client: Process (4, 5, '/')...
#   operation / is unknown to handler
# Client: Process (4, 5, 'plus')...
#   performing summation: 4+5 =  9