from enum import Enum
from typing import Dict, Tuple


class Material(Enum):
    STEEL = "steel"  # стальний диск
    ALLOY = "alloy"  # легкосплавний


class Wheel:

    _material: Material
    _diameter: int

    def __init__(self, diameter: int, material: Material = Material.STEEL):
        self._material = material
        self._diameter = diameter

    def __str__(self):
        return f"Wheel material={self._material.value}, diameter={self._diameter}, hash={hash(self)}"


class WheelFactory:
    _wheels: Dict[Tuple[int, Material], Wheel] = {}

    def get_wheel(self, diameter: int = 17, material: Material = Material.STEEL) -> Wheel:
        param = (diameter, material)
        if param in self._wheels.keys():
            return self._wheels.get(param)
        new_wheel = Wheel(diameter, material)
        self._wheels[param] = new_wheel
        return new_wheel
