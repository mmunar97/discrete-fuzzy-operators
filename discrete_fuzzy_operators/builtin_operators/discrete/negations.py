from enum import Enum

from discrete_fuzzy_operators.base.operators.unary_operators.fuzzy_discrete_unary_operator import \
    FuzzyDiscreteUnaryOperator


class NegationExamples(Enum):
    """
    Object that stores the values of the most known negations.
    """
    CLASSIC = "classic_negation"

    @staticmethod
    def get_negation(negation: "NegationExamples", n: int) -> FuzzyDiscreteUnaryOperator:
        """
        Returns a FuzzyDiscreteUnaryOperator object representing the selected negation.

        Args:
            negation: A Negation value, representing the chosen negation.
            n: An integer, representing the dimension of the domain where the negation is defined.

        Returns:
            A FuzzyDiscreteUnaryOperator object.
        """
        if negation == NegationExamples.CLASSIC:
            return FuzzyDiscreteUnaryOperator(n=n, operator_expression=NegationExamples.__classical_negation)

    @staticmethod
    def __classical_negation(x: int, n: int) -> int:
        """
        Implementation of the classical negation.

        Args:
            x: An integer, representing the coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the negation in the point.
        """
        return n - x