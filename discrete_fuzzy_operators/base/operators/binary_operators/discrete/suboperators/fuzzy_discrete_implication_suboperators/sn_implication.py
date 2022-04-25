import numpy


from typing import Callable

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.tconorm import \
    Tconorm
from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_implication_operator import \
    DiscreteImplicationOperator
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.fuzzy_negation_operator import \
    DiscreteNegation


class SNImplication(DiscreteImplicationOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 operator_tconorm: Tconorm = None, operator_negation: DiscreteNegation = None):
        """
        Initializes the object that represents an SN-implication I: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix representation, its analytical expression or its components.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
            operator_tconorm: A Tconorm object, representing the t-conorm.
            operator_negation: A DiscreteFuzzyNegation object, representing the discrete negation.
        """
        if (operator_matrix is None and operator_expression is None and operator_tconorm is None and
                operator_negation is None):
            raise Exception("To initialise an SN-implication it is necessary to provide its matrix expression, a "
                            "callable method or its components (a t-conorm and a negation).")

        if not(operator_matrix is None or operator_expression is None):
            super(SNImplication, self).__init__(n, operator_matrix, operator_expression)
        if not(operator_tconorm is None and operator_negation is None):
            super(SNImplication, self).__init__(n, SNImplication.__generate_implication_matrix_from_components(n, operator_tconorm, operator_negation), None)

    @staticmethod
    def __generate_implication_matrix_from_components(n: int,
                                                      operator_tconorm: Tconorm,
                                                      operator_negation: DiscreteNegation) -> numpy.ndarray:
        """
        Generates the SN-implication matrix representation from its components: a discrete t-conorm and a discrete
        negation. The implication is defined as I(x,y)=S(N(x),y).

        Args:
            n: An integer, representing where the implication is defined.
            operator_tconorm: A Tconorm object, representing the t-conorm.
            operator_negation: A DiscreteFuzzyNegation object, representing the discrete negation.

        Returns:
            A numpy array, representing the matrix representation of the implication.
        """
        if operator_tconorm.n != operator_negation.n != n:
            raise Exception("The dimensions of the t-conorm, the discrete negation and the provided dimension do not "
                            "match.")

        matrix = numpy.zeros((n + 1, n + 1), dtype=int)
        for x in range(0, n + 1):
            for y in range(0, n + 1):
                matrix[y, x] = operator_tconorm.evaluate_operator(operator_negation.evaluate_operator(x), y)
        return matrix
