from abc import abstractmethod, ABC
from typing import List

from equations import Equation, BiQuadraticEquation, QuadraticEquation


class EquationFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_equation(coef) -> Equation:
        pass


class LinearEquationFactory(EquationFactory):
    @staticmethod
    def create_equation(coef) -> Equation:
        assert len(coef) == 2
        return Equation(coef)


class QuadraticEquationFactory(EquationFactory):
    @staticmethod
    def create_equation(coef) -> Equation:
        assert len(coef) == 3
        if coef[0] == 0:
            return Equation(coef[1:])
        return QuadraticEquation(coef)


class BiQuadraticEquationFactory(EquationFactory):
    @staticmethod
    def create_equation(coef) -> Equation:
        assert len(coef) == 5
        if coef[0] == 0:
            if coef[2] == 0:
                return Equation(coef[3:])
            return QuadraticEquation(coef[2:])
        return BiQuadraticEquation(coef)

