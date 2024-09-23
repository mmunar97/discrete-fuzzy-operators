import numpy

from discrete_fuzzy_operators.base.operators.unary_operators.discrete.fuzzy_discrete_unary_operator import \
    DiscreteUnaryOperator
from discrete_fuzzy_operators.base.operators.unary_operators.discrete.suboperators.yager_generator_operator import \
    YagerGeneratorOperator


def yager_generation1(x: int, n: int):
    if 0 <= x <= 3:
        return 7-x
    elif 3 < x <= 5:
        return 4
    elif 6 <= x <= 7:
        return 7-x


def yager_generation2(x: int, n: int):
    if x == 0:
        return 10
    elif 1 <= x <= 5:
        return 5
    elif 6 <= x <= 7:
        return 2
    else:
        return 0


def aggregation_function(x: int, y: int, n: int) -> int:
    if x == y == 0:
        return 0
    else:
        return n


if __name__ == "__main__":

    n = 10
    generator = YagerGeneratorOperator(n=n, operator_expression=yager_generation2)

    composition1 = []
    composition2 = []
    for x in range(0, n+1):
        composition1.append(generator.evaluate_operator(generator.get_pseudoinverse().evaluate_operator(x)))
        composition2.append(generator.get_pseudoinverse().evaluate_operator(generator.evaluate_operator(x)))

    ff1 = DiscreteUnaryOperator(n=n, operator_vector=numpy.array(composition1))
    f1f = DiscreteUnaryOperator(n=n, operator_vector=numpy.array(composition2))

    generator.plot_operator(figure_size=(800, 700))
    generator.get_pseudoinverse().plot_operator(figure_size=(800, 700))
    ff1.plot_operator(figure_size=(800, 700))
    f1f.plot_operator(figure_size=(800, 700))
