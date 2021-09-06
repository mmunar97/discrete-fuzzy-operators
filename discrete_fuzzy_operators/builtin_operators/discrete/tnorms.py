from enum import Enum

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.tnorm import \
    Tnorm


class TnormExamples(Enum):
    """
    Object that stores the values of the most known t-norms.
    """
    MINIMUM = "minimum_tnorm"
    DRASTIC = "drastic_tnorm"
    NILPOTENT_MINIMUM = "nilpotent_minimum_tnorm"
    LUKASIEWICZ = "lukasiewicz_tnorm"

    @staticmethod
    def get_tnorm(tnorm: "TnormExamples", n: int) -> Tnorm:
        """
        Returns a DiscreteFuzzyAggregationOperator object representing the selected t-norm.

        Args:
            tnorm: A Tnorm value, representing the chosen t-norm.
            n: An integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            A DiscreteFuzzyAggregationOperator object.
        """
        if tnorm == TnormExamples.MINIMUM:
            return Tnorm(n=n, operator_expression=TnormExamples.__minimum_tnorm)
        elif tnorm == TnormExamples.DRASTIC:
            return Tnorm(n=n, operator_expression=TnormExamples.__drastic_tnorm)
        elif tnorm == TnormExamples.NILPOTENT_MINIMUM:
            return Tnorm(n=n, operator_expression=TnormExamples.__nilpotent_minimum)
        elif tnorm == TnormExamples.LUKASIEWICZ:
            return Tnorm(n=n, operator_expression=TnormExamples.__lukasiewicz)

    @staticmethod
    def __minimum_tnorm(x: int, y: int, n: int) -> int:
        """
        Implementation of the discrete minimum t-norm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-norm in the point (x,y).
        """
        return min(x, y)

    @staticmethod
    def __drastic_tnorm(x: int, y: int, n: int):
        """
        Implementation of the discrete drastic t-norm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-norm in the point (x,y).
        """
        if x != n and y != n:
            return 0
        return min(x, y)

    @staticmethod
    def __nilpotent_minimum(x: int, y: int, n: int):
        """
        Implementation of the discrete nilpotent minimum t-norm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-norm in the point (x,y).
        """
        if x + y <= n:
            return 0
        return min(x, y)

    @staticmethod
    def __lukasiewicz(x: int, y: int, n: int):
        """
        Implementation of the discrete Lukasiewicz t-norm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-norm in the point (x,y).
        """
        return max(0, x + y - n)
