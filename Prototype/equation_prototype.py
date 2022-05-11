# implementation of Prototype is hinted by the tips in Refactoring Guru - the book

import copy

from math import sqrt
from typing import List

INF = "infinite amount of solutions"


def _discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def _get_square_roots(x):
    return [-sqrt(x), sqrt(x)] if x > 0 else [0] if x == 0 else []


class Equation:
    _n_coeff = 2
    _type: str = "Linear Equation"
    _coefficients: List[int]

    def __init__(self, coeff: List[int]):
        assert len(coeff) == self._n_coeff and coeff[0] != 0
        self._coefficients = coeff

    def set_coefficient(self, a: int, i: int):
        try:
            self._coefficients[i] = a
        except IndexError:
            print(
                f"Probably you got the index wrong:\n"
                f"  valid values: 0..{self._n_coeff-1}, your index: {i}"
            )

    def get_coefficients(self):
        return self._coefficients

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

    def __copy__(self):
        coefficients = copy.copy(self._coefficients)

        new_obj = self.__class__(coefficients)
        new_obj.__dict__.update(self.__dict__)

        return new_obj

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}

        coefficients = copy.deepcopy(self._coefficients, memodict)
        new_obj = self.__class__(coefficients)
        new_obj.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new_obj

    def __str__(self):
        return f"{self._type:<22}  {self._coef2str()} = 0"

    def __repr__(self):
        return f"{self._type:<22}  {self._coef2str()} = 0"


class QuadraticEquation(Equation):
    _n_coeff = 3
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
    _n_coeff = 5
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
