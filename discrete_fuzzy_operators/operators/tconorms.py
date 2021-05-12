from enum import Enum
from discrete_fuzzy_operators.base.fuzzy_aggregation_operator import DiscreteFuzzyAggregationOperator


# region Declaration of the avaliable t-conorm
class Tconorm(Enum):
    """
    Object that stores the values of the different t-conorms which analytical expression is available.
    """
    MAXIMUM = "maximum_tconorm"
    DRASTIC = "drastic_tconorm"
    NILPOTENT_MAXIMUM = "nilpotent_maximum_tconorm"
    LUKASIEWICZ = "lukasiewicz_tconorm"
# endregion


# region Declaration of the getter of the t-conorm
def get_tconorm(tconorm: Tconorm, n: int) -> DiscreteFuzzyAggregationOperator:
    """
    Returns a DiscreteFuzzyAggregationOperator object representing the selected t-conorm.

    Args:
        tnorm: A Tconorm value, representing the chosen t-conorm.
        n: An integer, representing the dimension of the domain where the t-conorm is defined.

    Returns:
        A DiscreteFuzzyAggregationOperator object.
    """
    if tconorm == Tconorm.MAXIMUM:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=maximum_tconorm)
    elif tconorm == Tconorm.DRASTIC:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=drastic_tconorm)
    elif tconorm == Tconorm.NILPOTENT_MAXIMUM:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=nilpotent_maximum)
    elif tconorm == Tconorm.LUKASIEWICZ:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=lukasiewicz)


def maximum_tconorm(x: int, y: int, n: int) -> int:
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


def drastic_tconorm(x: int, y: int, n: int):
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


def nilpotent_maximum(x: int, y: int, n: int):
    """
    Implementation of the discrete nilpotent maximum t-conorm.

    Args:
        x: An integer, representing the first coordinate of the evaluation point.
        y: An integer, representing the second coordinate of the evaluation point.
        n: n integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        An integer, representing the value of the t-conorm in the point (x,y).
    """
    if x+y >= n:
        return n
    return max(x, y)


def lukasiewicz(x: int, y: int, n: int):
    """
    Implementation of the discrete Lukasiewicz t-conorm.

    Args:
        x: An integer, representing the first coordinate of the evaluation point.
        y: An integer, representing the second coordinate of the evaluation point.
        n: n integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        An integer, representing the value of the t-conorm in the point (x,y).
    """
    return min(n, x+y)
# endregion
