import copy
from equation_prototype import *


if __name__ == "__main__":
    # lin_eq = Equation([2, 4])
    quad_eq = QuadraticEquation([1, 2, 1])

    quad_eq_copy = copy.copy(quad_eq)
    quad_eq_deepcopy = copy.deepcopy(quad_eq)
    print(
        f"Original:  {quad_eq}\n"
        f"Copy:      {quad_eq_copy}\n"
        f"Deep copy: {quad_eq_deepcopy}"
    )
    # change list of coefficients in copy
    quad_eq_copy.set_coefficient(5, 2)
    print(
        "Equations after changing the copy\n"
        f"Original:  {quad_eq}\n"
        f"Copy:      {quad_eq_copy}\n"
        f"Deep copy: {quad_eq_deepcopy}"
    )
    # change list of coefficients in original
    quad_eq.set_coefficient(2, 0)
    print(
        "equations after changing the original\n"
        f"Original:  {quad_eq}\n"
        f"Copy:      {quad_eq_copy}\n"
        f"Deep copy: {quad_eq_deepcopy}"
    )
