class Vehicle:
    def __init__(self, age: int = 0, model: str = "default", damage: float = 0, mileage: int = 0):
        self._age = age  # вік автомобіля в роках
        self._model = model  # марка автомобіля
        self._damage = damage  # ступінь пошкодження автомобіля: 1 - без пошкоджено
                               # 0 - максимальне пошкодження, не підлягає ремону
        self._mileage = mileage  # пробіг автомобіля в милях

    def get_age(self) -> int:
        return self._age

    def get_model(self) -> str:
        return self._model

    def get_mileage(self) -> int:
        return self._mileage

    def get_damage(self) -> float:
        return self._damage


class Car(Vehicle):
    def __init__(self, age: int = 0, model: str = "default", damage: float = 0):
        super().__init__(age, model, damage, 0)


class Truck(Vehicle):
    def __init__(self, age: int = 0, mileage: int = 0):
        super().__init__(age, "truck", 0, mileage)
