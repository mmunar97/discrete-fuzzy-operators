import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import \
    DiscreteFuzzyAggregationBinaryOperator
from typing import Callable, Dict


class Uninorm(DiscreteFuzzyAggregationBinaryOperator):

    def __init__(self, n: int, e: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 operator_components: Dict[str, numpy.ndarray] = None):
        """
        Initializes the object that represents a uninorm U: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            n: An integer, representing the dimension of the space where the uninorm is defined.
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
            operator_components: A dictionary containing the components of the uninorms, which a t-norm in [0, e], a
                                 t-conorm in [e, n], and two mappings in the compensation space
                                 [0,e)x(e,n]U(e,n]x[0,e).
        """
        if operator_matrix is None and operator_expression is None and operator_components is None:
            raise Exception("To initialise a uninorm it is necessary to provide its matrix expression, a callable "
                            "method or its components.")

        if not(operator_matrix is None or operator_expression is None):
            super(Uninorm, self).__init__(n, operator_matrix, operator_expression)
            self.e = e
        else:
            super(Uninorm, self).__init__(n, Uninorm.__generate_uninorm_matrix_from_components(n, e, operator_components))
            self.e = e

        if not(self.is_associative() and self.is_commutative() and self.checks_boundary_condition(element=self.e)):
            raise Exception("With the input arguments, the generated operator is not a uninorm since not verifies "
                            "the associativity, the commutativity or the neutral element.")

    @staticmethod
    def __generate_uninorm_matrix_from_components(n: int, e: int, components: Dict[str, numpy.ndarray]) -> numpy.ndarray:
        """
        Generates the uninorm matrix representation from the components that define a uninorm: a t-norm in [0,e], a
        t-conorm in [e,n] and two mappings in the compensation space.

        Args:
            n: An integer, representing the dimension of the space where the uninorm is defined.
            e: An integer, representing the neutral element.
            components: A dictionary, which contains strings as keys and numpy arrays as values. Each pair key-value
                        represents a component of the uninorm.

        Returns:
            A numpy array, representing the matrix representation of the uninorm.
        """
        uninorm_matrix = numpy.zeros(shape=(n+1, n+1), dtype=int)

        if not("TNORM" in components and "TCONORM" in components and "CE_LEFT" in components and "CE_RIGHT" in components):
            raise Exception("The dictionary with the components does not have a correct key structure. ")

        tnorm_matrix = numpy.array(components["TNORM"])
        tconorm_matrix = numpy.array(components["TCONORM"])
        compensation_mapping_left_matrix = numpy.array(components["CE_LEFT"])
        compensation_mapping_right_matrix = numpy.array(components["CE_RIGHT"])

        # Verification of the shapes
        if not(tnorm_matrix.shape == (e+1, e+1) and tconorm_matrix.shape == (n-e+1, n-e+1) and
               compensation_mapping_left_matrix.shape == (n-e, e) and
               compensation_mapping_right_matrix.shape == (e, n-e)):
            raise Exception("The dimensions of the components of the uninorms are not correct for the initialization. "
                            "The t-norm matrix must be of size (e, e), the t-conorm matrix must be (n-e, n-e), the "
                            "left compensation mapping must be (n-e, e) and the right compensation mapping must be "
                            "(e, n-e).")

        for x in range(0, e+1):
            for y in range(0, e+1):
                uninorm_matrix[y, x] = tnorm_matrix[y, x]
        for x in range(e, n+1):
            for y in range(e, n+1):
                uninorm_matrix[y, x] = tconorm_matrix[y-e, x-e]
        for x in range(0, e):
            for y in range(e+1, n+1):
                uninorm_matrix[y, x] = compensation_mapping_left_matrix[y-e-1, x]
        for x in range(e+1, n+1):
            for y in range(0, e):
                uninorm_matrix[y, x] = compensation_mapping_right_matrix[y, x-e-1]

        return uninorm_matrix
