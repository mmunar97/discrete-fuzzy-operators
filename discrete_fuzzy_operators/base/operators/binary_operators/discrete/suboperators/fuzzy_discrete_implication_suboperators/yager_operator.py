from typing import Callable

import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import \
    DiscreteBinaryOperator
from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_implication_operator import \
    DiscreteImplicationOperator
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.yager_generator_operator import \
    YagerGeneratorOperator


class YagerImplication(DiscreteImplicationOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 yager_generator: YagerGeneratorOperator = None,
                 binary_operator: DiscreteBinaryOperator = None):
        if operator_matrix is None and operator_expression is None and yager_generator is None:
            raise Exception("To initialise a discrete Yager implication it is necessary to provide its matrix "
                            "expression, a callable method or the discrete generator.")

        if operator_matrix is not None or operator_expression is not None:
            super(YagerImplication, self).__init__(n, operator_matrix, operator_expression)
        if yager_generator is not None and binary_operator is not None:
            super(YagerImplication, self).__init__(n, YagerImplication.__generate_implication_matrix_from_components(n=n,
                                                                                                                     generator=yager_generator,
                                                                                                                     binary_operator=binary_operator), None)

    @staticmethod
    def __generate_implication_matrix_from_components(n: int,
                                                      generator: YagerGeneratorOperator,
                                                      binary_operator: DiscreteBinaryOperator) -> numpy.ndarray:

        if generator.n != binary_operator.n != n:
            raise Exception("The dimensions of the generator, the binary function and the provided dimension do not "
                            "match.")

        matrix = numpy.zeros((n + 1, n + 1), dtype=int)
        for x in range(0, n + 1):
            for y in range(0, n + 1):
                matrix[y, x] = generator.get_pseudoinverse().evaluate_operator(
                    binary_operator.evaluate_operator(x, generator.evaluate_operator(y)))
        return matrix
