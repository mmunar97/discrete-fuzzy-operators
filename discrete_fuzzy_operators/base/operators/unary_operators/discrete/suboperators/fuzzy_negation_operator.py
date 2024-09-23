import numpy
import warnings

from discrete_fuzzy_operators.base.operators.unary_operators.discrete.fuzzy_discrete_unary_operator import \
    DiscreteUnaryOperator
from typing import Callable


class DiscreteNegation(DiscreteUnaryOperator):

    def __init__(self, n: int,
                 operator_vector: numpy.array = None,
                 operator_expression: Callable[[int, int], int] = None,
                 check_properties_in_load: bool = False):
        """
        Initializes the object representing the discrete negation from its vector expression or its analytical
        expression.

        Args:
            n: An integer, representing the size of the finite chain.
            operator_vector: A list of integers, representing the operator in its vector expression.
            operator_expression: A function, representing the analytical expression.
        """
        super(DiscreteNegation, self).__init__(n, operator_vector, operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_negation():
            warnings.warn("With the input arguments, the generated operator is not a discrete negation since it is "
                          "not decreasing and satisfies the boundary conditions.")

    # region Basic properties of negations
    def is_negation(self) -> bool:
        """
        Checks if the operator is a discrete negation; that is, if it is monotone decreasing and satisfies the
        boundary conditions.
        """
        return self.is_decreasing() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a discrete negation; that is, if N(0)=n and
        N(n)=0.
        """
        if self.evaluate_operator(0) == self.n and self.evaluate_operator(self.n) == 0:
            return True
        return False
    # endregion
