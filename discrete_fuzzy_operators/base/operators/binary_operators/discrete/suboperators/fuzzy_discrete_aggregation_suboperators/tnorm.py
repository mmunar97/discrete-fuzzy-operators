import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.conjunction import \
    Conjunction
from typing import Callable


class Tnorm(Conjunction):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a tnorm T: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a t-norm it is necessary to provide its matrix expression or a callable "
                            "method.")

        super(Tnorm, self).__init__(n, operator_matrix, operator_expression, check_properties_in_load)

        if check_properties_in_load and not(self.is_associative() and self.is_commutative() and self.checks_boundary_condition(element=self.n)):
            raise Warning("With the input arguments, the generated operator is not a t-norm since not verifies "
                          "the associativity, the commutativity or the neutral element.")

    def is_divisible(self, **kwargs) -> bool:
        """
        Checks if the operator is divisible; that is, if for all x,y in L with x<=y, there is z in L such that
        x=F(y,z).

        Returns:
            A boolean, indicating if the operator is divisible.
        """
        return super(Tnorm, self).is_divisible(tnorm_condition=True)

    def is_archimedean(self, integer_limit: int = 100, **kwargs) -> bool:
        """
        Checks if the operator is archimedean; that is, if for all x,y in L, there is a natural number m such that
        x^m < y, where x^m represents the archimedean operator.

        Args:
            integer_limit: An integer, representing the maximum number to try when checking the archimedean property.

        Returns:
            A boolean, indicating if the operator is archimedean.
        """
        return super(Tnorm, self).is_archimedean(tnorm_condition=True, integer_limit=integer_limit)
