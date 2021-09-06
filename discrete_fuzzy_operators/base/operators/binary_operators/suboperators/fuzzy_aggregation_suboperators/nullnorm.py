import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import \
    DiscreteFuzzyAggregationBinaryOperator
from typing import Callable


class Nullnorm(DiscreteFuzzyAggregationBinaryOperator):

    def __init__(self, n: int,
                 k: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the object that represents a nullnorm G: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            n: An integer, representing the dimension of the space where the nullnorm is defined.
            k: An integer, representing the absorbing element.
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a nullnorm it is necessary to provide its matrix expression or a callable "
                            "method.")

        if not(0 <= k <= n):
            raise Exception("The absorbing element must be between 0 and n.")

        super(Nullnorm, self).__init__(n, operator_matrix, operator_expression)

        if not(self.is_associative() and self.is_commutative() and self.absorbing_element(element=k)):
            raise Exception("With the input arguments, the generated operator is not a nullnorm since not verifies "
                            "the associativity, the commutativity or the absorbing element nullnorm.")
