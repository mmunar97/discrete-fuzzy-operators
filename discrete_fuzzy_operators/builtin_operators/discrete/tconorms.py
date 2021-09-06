from enum import Enum
from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.tconorm import Tconorm


class TconormExamples(Enum):
    """
    Object that stores the values of the most known t-conorms.
    """
    MAXIMUM = "maximum_tconorm"
    DRASTIC = "drastic_tconorm"
    NILPOTENT_MAXIMUM = "nilpotent_maximum_tconorm"
    LUKASIEWICZ = "lukasiewicz_tconorm"

    @staticmethod
    def get_tconorm(tconorm: "TconormExamples", n: int) -> Tconorm:
        """
        Returns a DiscreteFuzzyAggregationOperator object representing the selected t-conorm.

        Args:
            tconorm: A Tconorm value, representing the chosen t-conorm.
            n: An integer, representing the dimension of the domain where the t-conorm is defined.

        Returns:
            A DiscreteFuzzyAggregationOperator object.
        """
        if tconorm == TconormExamples.MAXIMUM:
            return Tconorm(n=n, operator_expression=TconormExamples.__maximum_tconorm)
        elif tconorm == TconormExamples.DRASTIC:
            return Tconorm(n=n, operator_expression=TconormExamples.__drastic_tconorm)
        elif tconorm == TconormExamples.NILPOTENT_MAXIMUM:
            return Tconorm(n=n, operator_expression=TconormExamples.__nilpotent_maximum)
        elif tconorm == TconormExamples.LUKASIEWICZ:
            return Tconorm(n=n, operator_expression=TconormExamples.__lukasiewicz)

    @staticmethod
    def __maximum_tconorm(x: int, y: int, n: int) -> int:
        """
        Implementation of the discrete minimum t-conorm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-conorm in the point (x,y).
        """
        return max(x, y)

    @staticmethod
    def __drastic_tconorm(x: int, y: int, n: int):
        """
        Implementation of the discrete drastic t-conorm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-conorm in the point (x,y).
        """
        if x != 0 and y != 0:
            return n
        return max(x, y)

    @staticmethod
    def __nilpotent_maximum(x: int, y: int, n: int):
        """
        Implementation of the discrete nilpotent maximum t-conorm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-conorm in the point (x,y).
        """
        if x + y >= n:
            return n
        return max(x, y)

    @staticmethod
    def __lukasiewicz(x: int, y: int, n: int):
        """
        Implementation of the discrete Lukasiewicz t-conorm.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the t-conorm in the point (x,y).
        """
        return min(n, x + y)
