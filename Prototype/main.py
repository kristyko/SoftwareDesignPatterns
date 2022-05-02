from equation_prototype import *


if __name__ == "__main__":
    lin_eq = Equation([2, 4])
    quad_eq = QuadraticEquation([1, 2, 1])
    biquad_eq = BiQuadraticEquation([1, 0, 2, 0, 1])
    print(lin_eq, quad_eq, biquad_eq)
