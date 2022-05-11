class Auto:
    def __init__(self, age: int, model: str, damaged: bool, mileage: int):
        self._age = age
        self._model = model
        self._damaged = damaged
        self._mileage = mileage

    @property
    def age(self):
        return self._age

    @property
    def model(self):
        return self._model

    @property
    def damaged(self):
        return self._damaged

    @property
    def mileage(self):
        return self._mileage

    def __str__(self):
        return (
            f"Auto  model: {self.model}; age: {self.age}; is damaged: {self.damaged}, milleage: {self.mileage}"
        )
