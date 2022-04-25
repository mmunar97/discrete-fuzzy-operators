import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteAggregationBinaryOperator
from discrete_fuzzy_operators.base.operators.unary_operators.fuzzy_discrete_unary_operator import \
    DiscreteUnaryOperator
from typing import Callable


class Toperator(DiscreteAggregationBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the object that represents a t-operator F: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            n: An integer, representing the dimension of the space where the t-operator is defined.
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a t-operator it is necessary to provide its matrix expression or a callable "
                            "method.")

        super(Toperator, self).__init__(n, operator_matrix, operator_expression)

        f0 = DiscreteUnaryOperator(n=self.n, operator_vector=self.operator_matrix[:, 0].flatten())
        fn = DiscreteUnaryOperator(n=self.n, operator_vector=self.operator_matrix[:, self.n].flatten())
        if not(self.is_associative() and self.is_commutative() and f0.is_smooth() and fn.is_smooth()):
            raise Exception("With the input arguments, the generated operator is not a t-operator since not verifies "
                            "the associativity, the commutativity or the minimum-internal condition.")
