from enum import Enum
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.fuzzy_negation_operator import DiscreteNegation


class NegationExamples(Enum):
    """
    Object that stores the values of the most known negations.
    """
    CLASSIC = "classic_negation"
    LEAST = "least_discrete_negation"
    GREATEST = "greatest_discrete_negation"

    @staticmethod
    def get_negation(negation: "NegationExamples", n: int) -> DiscreteNegation:
        """
        Returns a FuzzyDiscreteUnaryOperator object representing the selected negation.

        Args:
            negation: A Negation value, representing the chosen negation.
            n: An integer, representing the dimension of the domain where the negation is defined.

        Returns:
            A FuzzyDiscreteUnaryOperator object.
        """
        if negation == NegationExamples.CLASSIC:
            return DiscreteNegation(n=n, operator_expression=NegationExamples.__classical_negation)
        elif negation == NegationExamples.LEAST:
            return DiscreteNegation(n=n, operator_expression=NegationExamples.__least_negation)
        elif negation == NegationExamples.GREATEST:
            return DiscreteNegation(n=n, operator_expression=NegationExamples.__greatest_negation)

    @staticmethod
    def __classical_negation(x: int, n: int) -> int:
        """
        Implementation of the classical discrete negation.

        Args:
            x: An integer, representing the coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the negation in the point.
        """
        return n - x

    @staticmethod
    def __least_negation(x: int, n: int) -> int:
        """
        Implementation of the least discrete negation.

        Args:
            x: An integer, representing the coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the negation in the point.
        """
        if x == 0:
            return n
        else:
            return 0

    @staticmethod
    def __greatest_negation(x: int, n: int) -> int:
        """
        Implementation of the greatest discrete negation.

        Args:
            x: An integer, representing the coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the negation in the point.
        """
        if x == n:
            return 0
        else:
            return n
