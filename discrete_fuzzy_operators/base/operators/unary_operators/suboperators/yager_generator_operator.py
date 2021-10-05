import numpy

from discrete_fuzzy_operators.base.operators.unary_operators.fuzzy_discrete_unary_operator import \
    FuzzyDiscreteUnaryOperator
from typing import Callable


class YagerGeneratorOperator(FuzzyDiscreteUnaryOperator):

    def __init__(self, n: int,
                 operator_vector: numpy.array = None,
                 operator_expression: Callable[[int, int], int] = None):
        """
        Initializes the object representing the generator of the discrete Yager implications. This operator must be
        decreasing, and verify the boundary conditions f(n)=0 and f(0)=n.

        Args:
            n: An integer, representing the size of the finite chain.
            operator_vector: A list of integers, representing the operator in its vector expression.
            operator_expression: A function, representing the analytical expression.
        """
        super(YagerGeneratorOperator, self).__init__(n, operator_vector, operator_expression)

    def get_pseudoinverse(self) -> FuzzyDiscreteUnaryOperator:
        """
        Computes the pseudo-inverse of a decreasing function. By definition, it is given by
        Returns:

        """
        pseudoinverse_vector = []

        for t in range(0, self.n+1):
            candidates = []
            for i in range(0, self.n+1):
                if (self.evaluate_operator(i)-t)*(self.evaluate_operator(self.n)-self.evaluate_operator(0)) <= 0:
                    candidates.append(i)
            pseudoinverse_vector.append(max(candidates))
        return FuzzyDiscreteUnaryOperator(n=self.n, operator_vector=numpy.array(pseudoinverse_vector))
