from collections import defaultdict
from typing import List

from equation_factory import LinearEquationFactory, QuadraticEquationFactory, BiQuadraticEquationFactory
from equations import Equation, INF


def create_equation(coef: List[int]) -> Equation:
    n = len(coef)
    if n == 2:
        return LinearEquationFactory.create_equation(coef)
    elif n == 3:
        return QuadraticEquationFactory.create_equation(coef)
    elif n == 5:
        return BiQuadraticEquationFactory.create_equation(coef)
    else:
        raise ValueError("Unknown type of equation. Unsupported number of parameters.")


def _save_results(filename, solutions):
    with open(filename.split(".")[0] + "_solutions.txt", "w") as outfile:
        for key, values in solutions.items():
            outfile.write(f"# of solutions: {key}\n")
            for value in values:
                outfile.write(f"   {str(value[0]):<60}  Roots: {value[1]}\n")
            outfile.write("\n")

        outfile.write("\n")
        min_solution = min(solutions[1], key=lambda x: x[1])
        max_solution = max(solutions[1], key=lambda x: x[1])
        outfile.write(f"Equation with minimal solution : {min_solution}\n")
        outfile.write(f"Equation with maximal solution : {max_solution}\n")


def solve_equations(filename, save_result=True):
    equations: List[Equation] = []

    with open(filename, "r") as f:
        for line in f.readlines():
            coeff = list(map(int, line.split()))
            equation = create_equation(coeff)
            equations.append(equation)

    solutions = defaultdict(list)
    for equation in equations:
        roots = equation.solve()
        n_roots = len(roots)
        solutions[n_roots if INF not in roots else INF].append((equation, roots))

    if save_result:
        _save_results(filename, solutions)
    return solutions


if __name__ == "__main__":
    # see the results in ./data/<inputfile>_solutions.txt
    filename = "data/input01.txt"
    # filename = "data/input02.txt"
    # filename = "data/input03.txt"
    solve_equations(filename)
