import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteAggregationBinaryOperator
from typing import Callable


class Disjunction(DiscreteAggregationBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a disjunction D: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a disjunction it is necessary to provide its matrix expression or a callable"
                            " method.")

        super(Disjunction, self).__init__(n, operator_matrix, operator_expression, check_properties_in_load)

        if check_properties_in_load and not(self.evaluate_operator(0, self.n) == self.evaluate_operator(self.n, 0) == self.n and self.evaluate_operator(0, 0) == 0):
            raise Exception("With the input arguments, the generated operator is not a disjunction since not verifies the boundary conditions.")
