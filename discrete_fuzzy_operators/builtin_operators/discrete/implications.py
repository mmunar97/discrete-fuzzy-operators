from enum import Enum
from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_implication_operator import \
    DiscreteImplicationOperator


class DiscreteImplicationExamples(Enum):
    """
    Object that stores the values of the most known implications.
    """
    LARGEST = "largest_implication"
    LUKASIEWICZ = "lukasiewicz_implication"
    GODEL = "godel_implication"
    RESCHER = "rescher_implication"
    WEBER = "weber_implication"
    FODOR = "fodor_implication"

    @staticmethod
    def get_discrete_implication(implication: "DiscreteImplicationExamples", n: int) -> DiscreteImplicationOperator:
        """
        Returns a DiscreteFuzzyImplicationOperator object representing the selected implication.

        Args:
            implication: An DiscreteImplication value, representing the chosen implication.
            n: An integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            A DiscreteFuzzyImplicationOperator object.
        """
        if implication == DiscreteImplicationExamples.LARGEST:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__largest_implication)
        elif implication == DiscreteImplicationExamples.LUKASIEWICZ:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__lukasiewicz_implication)
        elif implication == DiscreteImplicationExamples.GODEL:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__godel_implication)
        elif implication == DiscreteImplicationExamples.RESCHER:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__rescher_implication)
        elif implication == DiscreteImplicationExamples.WEBER:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__weber_implication)
        elif implication == DiscreteImplicationExamples.FODOR:
            return DiscreteImplicationOperator(n=n, operator_expression=DiscreteImplicationExamples.__fodor_implication)

    @staticmethod
    def __largest_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the largest implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        if x == n and y == 0:
            return 0
        else:
            return n

    @staticmethod
    def __lukasiewicz_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the Lukasiewicz implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        return min(n, n - x + y)

    @staticmethod
    def __godel_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the Godel implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        if x <= y:
            return n
        else:
            return y

    @staticmethod
    def __rescher_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the Rescher implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        if x <= y:
            return n
        else:
            return 0

    @staticmethod
    def __weber_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the Weber implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        if x < n:
            return n
        else:
            return y

    @staticmethod
    def __fodor_implication(x: int, y: int, n: int) -> int:
        """
        Implementation of the Fodor implication.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the largest implication in the point (x,y).
        """
        if x <= y:
            return n
        else:
            return max(n - x, y)
