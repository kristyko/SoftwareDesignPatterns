from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: pass

    @abstractmethod
    def handle(self, request) -> Optional[str]: pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class PDFHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        if request.split(".")[-1] in ["pdf"]:
            return f"Opening a pdf file."
        else:
            return super().handle(request)


class ImageHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.split(".")[-1] in ["jpg", "jpeg", "png"]:
            return f"Opening an image."
        else:
            return super().handle(request)


class TextHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request.split(".")[-1] in ["txt", "doc"]:
            return f"Opening a video"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    files = ["png1.png", "txt2.txt", "pdf3.pdf"]
    for file in files:
        print(f"\nClient: Who wants a {file}?")
        result = handler.handle(file)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {file} was left untouched.", end="")


if __name__ == "__main__":
    pdf = PDFHandler()
    image = ImageHandler()
    text = TextHandler()

    text.set_next(image).set_next(pdf)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Text > Image > PDF")
    client_code(text)
    print("\n")

    print("Subchain: Image > PDF")
    client_code(image)


# Chain: Text > Image > PDF
# Client: Who wants a png1.png?
#   Opening an image.
# Client: Who wants a txt2.txt?
#   Opening a video
# Client: Who wants a pdf3.pdf?
#   Opening a pdf file.

# Subchain: Image > PDF
# Client: Who wants a png1.png?
#   Opening an image.
# Client: Who wants a txt2.txt?
#   txt2.txt was left untouched.
# Client: Who wants a pdf3.pdf?
#   Opening a pdf file.
