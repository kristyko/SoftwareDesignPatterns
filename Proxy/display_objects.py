from abc import abstractmethod, ABC

from PIL import Image


class DisplayObject(ABC):
    @abstractmethod
    def display(self): pass


class ImageFile(DisplayObject):
    def __init__(self, path):
        self.image = self.load(path)

    def display(self):
        print("displaying image...")
        self.image.show()

    def load(self, path):
        print("Loading image from " + path + "...")
        image = Image.open(path)
        return image


class ImageFileProxy(DisplayObject):
    _display_obj: DisplayObject = None

    def __init__(self, path):
        self._path = path

    def display(self):
        if not self._display_obj:
            self._display_obj = ImageFile(self._path)
        self._display_obj.display()

