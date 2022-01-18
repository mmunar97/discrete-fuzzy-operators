import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteFuzzyAggregationBinaryOperator
from typing import Callable, List


class Copula(DiscreteFuzzyAggregationBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 permutation: List[int] = None):
        """
        Initializes the object that represents a copula C: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix or its analytical expression.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A callable method with three parameters (x, y, n), which returns an integer value.
            permutation: A list of integers, representing the permutation of n elements.
        """
        if operator_matrix is None and operator_expression is None and permutation is None:
            raise Exception("To initialise a copula it is necessary to provide its matrix expression, a callable method"
                            " or a permutation.")

        if operator_matrix is None and operator_expression is None:
            super(Copula, self).__init__(n, Copula.convert_permutation_to_matrix(permutation, n), operator_expression)
        else:
            super(Copula, self).__init__(n, operator_matrix, operator_expression)

        if not(self.checks_two_increasing_condition() and self.checks_double_boundary_condition()):
            raise Exception("With the input arguments, the generated operator is not a copula since not verifies the"
                            "two increasing condition and the boundary conditions.")

    @staticmethod
    def generate_permutation_matrix(permutation: List[int], n: int) -> numpy.ndarray:
        """
        From a permutation of n elements, generate the associated permutation matrix. By definition, the permutation matrix
        in the input (i,j) contains the value 1 if i=p(j), or 0 otherwise.

        Args:
            permutation: A list of integers, representing the permutation of n elements.
            n: An integer, representing the dimension.

        Returns:
            A matrix of shape n x n, representing the permutation matrix.
        """
        permutation_matrix = numpy.zeros(shape=(n, n), dtype=int)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == permutation[j-1]:
                    permutation_matrix[i-1][j-1] = 1

        return permutation_matrix

    @staticmethod
    def convert_permutation_to_matrix(permutation: List[int], n: int) -> numpy.ndarray:
        """
        Generates the matrix expression of a copula from a permutation. If A is the permutation matrix associated to
        the permutation, then C(x,y)=SUM_{i <= x, j <= y} a_{ij}.

        Args:
            permutation: A list of integers, representing the permutation of n elements.
            n: An integer, representing the dimension.

        Returns:
            A matrix of shape n+1 x n+1, representing the matrix expression of the copula.
        """
        copula_matrix = numpy.zeros(shape=(n+1, n+1), dtype=int)

        permutation_matrix = Copula.generate_permutation_matrix(permutation=permutation, n=n)

        for x in range(0, n+1):
            for y in range(0, n+1):

                if x == 0 or y == 0:
                    copula_matrix[y][x] = 0
                else:
                    partial_sum = 0
                    for i in range(1, x+1):
                        for j in range(1, y+1):
                            partial_sum += permutation_matrix[i-1][j-1]
                    copula_matrix[y][x] = partial_sum

        return copula_matrix
