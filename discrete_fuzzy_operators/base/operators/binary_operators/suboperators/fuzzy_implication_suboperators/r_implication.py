import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.tnorm import \
    Tnorm
from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_implication_operator import \
    DiscreteFuzzyImplicationOperator
from typing import Callable


class RImplication(DiscreteFuzzyImplicationOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 operator_tnorm: Tnorm = None):
        """
        Initializes the object that represents an R-implication I: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix representation, its analytical expression or its components.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
            operator_tnorm: A Tnorm object, representing the t-norm.
        """
        if operator_matrix is None and operator_expression is None and operator_tnorm:
            raise Exception("To initialise an R-implication it is necessary to provide its matrix expression, a "
                            "callable method or a t-norm.")

        if not (operator_matrix is None or operator_expression is None):
            super(RImplication, self).__init__(n, operator_matrix, operator_expression)
        if not (operator_tnorm is None):
            super(RImplication, self).__init__(n, RImplication.__generate_implication_matrix_from_components(n, operator_tnorm))

    @staticmethod
    def __generate_implication_matrix_from_components(n: int, operator_tnorm: Tnorm) -> numpy.ndarray:
        """
        Generates the R-implication matrix representation from a given t-norm. The implication is defined with the
        concept of residuation: I(x,y)=max{z in L | T(x, z) <= y}.

        Args:
            n: An integer, representing the domain where the implication is defined.
            operator_tnorm: A Tnorm object, representing the t-norm.

        Returns:
            A numpy array, representing the matrix representation of the implication.
        """
        matrix = numpy.zeros((n + 1, n + 1), dtype=int)

        for x in range(0, n+1):
            for y in range(0, n+1):
                residuation_values = []
                for z in range(0, n+1):
                    if operator_tnorm.evaluate_operator(x, z) <= y:
                        residuation_values.append(z)
                matrix[y, x] = max(residuation_values)
        return matrix
