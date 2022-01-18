from enum import Enum

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_sheffer_stoke_operator import \
    DiscreteFuzzyShefferStrokeOperator


class ShefferStroke(Enum):
    """
    Object that stores the values of the most known Sheffer stroke operations.
    """
    MIN = "min_sheffer_stroke"
    MAX = "max_sheffer_stroke"

    @staticmethod
    def get_sheffer_stroke(operation: "ShefferStroke", n: int) -> DiscreteFuzzyShefferStrokeOperator:
        """
        Returns a DiscreteFuzzyShefferStrokeOperator object representing the selected negation.

        Args:
            operation: A ShefferStroke value, representing the chosen operation.
            n: An integer, representing the dimension of the domain where the operation is defined.

        Returns:
            A DiscreteFuzzyShefferStrokeOperator object.
        """
        if operation == ShefferStroke.MIN:
            return DiscreteFuzzyShefferStrokeOperator(n=n, operator_expression=ShefferStroke.__min_sheffer_stroke)
        elif operation == ShefferStroke.MAX:
            return DiscreteFuzzyShefferStrokeOperator(n=n, operator_expression=ShefferStroke.__max_sheffer_stroke)

    @staticmethod
    def __min_sheffer_stroke(x: int, y: int, n: int) -> int:
        """
        Implementation of the minimum Sheffer stroke operation.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the Sheffer stroke operation in the point (x,y).
        """
        if 0 < x <= n and 0 < y <= n:
            return 0
        else:
            return n

    @staticmethod
    def __max_sheffer_stroke(x: int, y: int, n: int) -> int:
        """
        Implementation of the maximum Sheffer stroke operation.

        Args:
            x: An integer, representing the first coordinate of the evaluation point.
            y: An integer, representing the second coordinate of the evaluation point.
            n: n integer, representing the dimension of the domain where the t-norm is defined.

        Returns:
            An integer, representing the value of the Sheffer stroke operation in the point (x,y).
        """
        if x == n and y == n:
            return 0
        else:
            return n
