import numpy
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.tconorm import \
    Tconorm
from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.tnorm import \
    Tnorm
from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_implication_operator import \
    DiscreteFuzzyImplicationOperator
from typing import Callable


class DOperator(DiscreteFuzzyImplicationOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 operator_tnorm: Tnorm = None,
                 operator_tconorm: Tconorm = None):
        """
        Initializes the object that represents a D-operator I: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix representation, its analytical expression or its components. If the
        implication is defined from its components, not for every t-norm and every t-conorm is an implication.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
            operator_tnorm: A Tnorm object, representing the t-norm.
            operator_tconorm: A Tconorm object, representing the t-conorm.
        """
        if operator_matrix is None and operator_expression is None and operator_tnorm and operator_tconorm is None:
            raise Exception("To initialise a D-implication it is necessary to provide its matrix expression, a "
                            "callable method or a t-norm.")

        if not (operator_matrix is None or operator_expression is None):
            super(DOperator, self).__init__(n, operator_matrix, operator_expression)
        if not (operator_tnorm is None and operator_tconorm is None):
            super(DOperator, self).__init__(n, DOperator.__generate_implication_matrix_from_components(n, operator_tnorm,
                                                                                                       operator_tconorm))

        if not self.is_implication():
            warnings.warn("With the given parameters, the initialized D-operator is not an implication.")

    @staticmethod
    def __generate_implication_matrix_from_components(n: int,
                                                      operator_tnorm: Tnorm,
                                                      operator_tconorm: Tconorm) -> numpy.ndarray:
        """
        Generates the QL-implication matrix representation from a given t-norm. The implication is defined as
        I(x, y) = S(T(n − x, n − y), y).

        Args:
            n: An integer, representing the domain where the implication is defined.
            operator_tnorm: A Tnorm object, representing the t-norm.
            operator_tconorm: A Tconorm object, representing the t-conorm.

        Returns:
            A numpy array, representing the matrix representation of the implication.
        """
        matrix = numpy.zeros((n + 1, n + 1), dtype=int)

        for x in range(0, n + 1):
            for y in range(0, n + 1):
                matrix[y, x] = operator_tconorm.evaluate_operator(operator_tnorm.evaluate_operator(n-x, n-y), y)
        return matrix

