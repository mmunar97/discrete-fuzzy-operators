import numpy
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteAggregationBinaryOperator
from typing import Callable


class Conjunction(DiscreteAggregationBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the object that represents a conjunction C: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a conjunction it is necessary to provide its matrix expression or a callable"
                            " method.")

        super(Conjunction, self).__init__(n, operator_matrix, operator_expression)

        if not self.is_conjunction():
            warnings.warn("With the input arguments, the generated operator is not a conjunction since not verifies "
                          "the boundary conditions or is not monotone increasing.")

    def is_conjunction(self) -> bool:
        """
        Checks if the defined operator is a discrete conjunction; that is, if it is decreasing in the first argument,
        increasing in the second argument and satisfies some boundary conditions.

        Returns:
            A boolean, indicating if the operator is an implication function.
        """
        if not (self.evaluate_operator(0, self.n) == self.evaluate_operator(self.n, 0) == 0 and
                self.evaluate_operator(self.n, self.n) == self.n and self.is_increasing()):
            return False
        else:
            return True

    def get_asm_representation(self) -> numpy.ndarray:
        """
        Computes the Alternating Sign Matrix representation of a smooth conjunction.  If the smooth is not smooth,
        an Exception is raised.

        Returns:
            An nxn matrix, representing the associated alternating sign matrix of the operator.
        """
        if not self.is_smooth():
            raise Exception("To initialise a conjunction it is necessary to provide its matrix expression or a callable"
                            " method.")

        asm = numpy.zeros(shape=(self.n, self.n), dtype=int)
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                asm[i-1, j-1] = self.evaluate_operator(i, j)-self.evaluate_operator(i, j-1)-self.evaluate_operator(i-1, j)+self.evaluate_operator(i-1, j-1)
        return asm
