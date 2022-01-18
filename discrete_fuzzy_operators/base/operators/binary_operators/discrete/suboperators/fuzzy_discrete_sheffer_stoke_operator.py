import numpy
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import \
    FuzzyDiscreteBinaryOperator
from typing import Callable


class DiscreteFuzzyShefferStrokeOperator(FuzzyDiscreteBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the object that represents a binary fuzzy Sheffer stroke H: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of H(x, y).
            operator_expression: A Callable method with three integer arguments (x,y,n) returning an integer value.
        """
        super(DiscreteFuzzyShefferStrokeOperator, self).__init__(n, operator_matrix, operator_expression)

        if not(self.is_decreasing() and self.satisfies_boundary_conditions()):
            warnings.warn("With the input arguments, the generated operator is not a discrete Sheffer stroke operation "
                          "since is not decreasing or the the boundary conditions are not satisfied.")

    # region Basic properties of implications
    def is_sheffer_stroke(self) -> bool:
        """
        Checks if the defined operator is a Sheffer stroke operation; that is, if it is decreasing in both arguments and
        satisfies some boundary conditions.

        Returns:
            A boolean, indicating if the operator is an implication function.
        """
        return self.is_decreasing_first_argument() and self.satisfies_boundary_conditions()

    def satisfies_boundary_conditions(self) -> bool:
        """
        Checks if the operator satisfies the boundary conditions of a Sheffer stroke operation; that is, if
        H(0,n)=H(n,0)=n and H(n,n)=0.

        Returns:
            A boolean, indicating if the operator satisfies the boundary conditions.
        """
        if self.evaluate_operator(0, self.n) == self.evaluate_operator(self.n, 0) == self.n and \
                self.evaluate_operator(self.n, self.n) == 0:
            return True
        else:
            return False
    # endregion
