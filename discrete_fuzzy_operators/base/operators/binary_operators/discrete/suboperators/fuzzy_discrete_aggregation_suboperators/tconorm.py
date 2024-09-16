import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.disjunction import \
    Disjunction
from typing import Callable


class Tconorm(Disjunction):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a tconorm S: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
        """
        if operator_matrix is None and operator_expression is None:
            raise Exception("To initialise a t-conorm it is necessary to provide its matrix expression or a callable "
                            "method.")

        super(Tconorm, self).__init__(n, operator_matrix, operator_expression, check_properties_in_load)

        if check_properties_in_load and not(self.is_associative() and self.is_commutative() and self.checks_boundary_condition(element=0) and self.is_increasing()):
            raise Exception("With the input arguments, the generated operator is not a t-conorm since not verifies "
                            "the associativity, the commutativity, the neutral element n or the monotonicity in each argument.")

    def is_divisible(self, **kwargs) -> bool:
        """
        Checks if the operator is divisible; that is, if for all x,y in L with x<=y, there is z in L such that
        y=F(x,z).

        Returns:
            A boolean, indicating if the operator is divisible.
        """
        return super(Tconorm, self).is_divisible(tnorm_condition=False)

    def is_archimedean(self, **kwargs) -> bool:
        """
        Checks if the t-conorm is archimedean; that is, if T(x,x)≠x, for all x in L\{0,n}.

        Returns:
            A boolean, indicating if the operator is archimedean.
        """
        for x in range(1, self.n):
            if self.evaluate_operator(x, x) == x:
                return False
        return True
