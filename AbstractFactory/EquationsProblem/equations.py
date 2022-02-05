from math import sqrt
from typing import List

INF = "infinite amount of solutions"


def _discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def _get_square_roots(x):
    return [-sqrt(x), sqrt(x)] if x > 0 else [0] if x == 0 else []


class Equation:
    _type: str = "Linear Equation"
    _coefficients: List[int]

    def __init__(self, coeff: List[int]):
        self._coefficients = coeff

    def solve(self):
        b, c = self._coefficients
        if b == 0:
            return [INF] if c == 0 else []
        return [-c / b]

    def _coef2str(self):
        n = len(self._coefficients)
        return " + ".join(
            [
                str(coef) + ("" if i == n else "x" if i == n - 1 else f"x^{n - i}")
                for i, coef in enumerate(self._coefficients, 1) if (coef != 0 or i >= n - 1)
            ]
        )

    def __str__(self):
        return f"{self._type:<22}  {self._coef2str()} = 0"

    def __repr__(self):
        return f"{self._type:<22}  {self._coef2str()} = 0"


class QuadraticEquation(Equation):
    _type: str = "Quadratic Equation"

    def solve(self):
        a, b, c = self._coefficients
        D = _discriminant(a, b, c)
        if D < 0:
            return []
        elif D == 0:
            return [-b / 2 / a]
        else:
            return [(-b - sqrt(D)) / 2 / a, (-b + sqrt(D)) / 2 / a]


class BiQuadraticEquation(Equation):
    _type: str = "Biquadratic Equation"

    def solve(self):
        a, _, b, _, c = self._coefficients
        D = _discriminant(a, b, c)
        if D < 0:
            return []
        elif D == 0:
            x = -b / 2 / a
            return _get_square_roots(x)
        else:
            x1, x2 = (-b - sqrt(D)) / 2 / a, (-b + sqrt(D)) / 2 / a
            return _get_square_roots(x1) + _get_square_roots(x2)
