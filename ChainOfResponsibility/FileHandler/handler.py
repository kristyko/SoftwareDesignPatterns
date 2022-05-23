from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def open(self, filename: str): pass

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: pass


class BaseHandler(Handler):
    pass