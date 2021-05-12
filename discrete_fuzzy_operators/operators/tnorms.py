from enum import Enum
from discrete_fuzzy_operators.base.fuzzy_aggregation_operator import DiscreteFuzzyAggregationOperator


# region Declaration of the avaliable t-norm
class Tnorm(Enum):
    """
    Object that stores the values of the different t-norms which analytical expression is available.
    """
    MINIMUM = "minimum_tnorm"
    DRASTIC = "drastic_tnorm"
    NILPOTENT_MINIMUM = "nilpotent_minimum_tnorm"
    LUKASIEWICZ = "lukasiewicz_tnorm"
# endregion


# region Declaration of the getter of the t-norm
def get_tnorm(tnorm: Tnorm, n: int) -> DiscreteFuzzyAggregationOperator:
    """
    Returns a DiscreteFuzzyAggregationOperator object representing the selected t-norm.

    Args:
        tnorm: A Tnorm value, representing the chosen t-norm.
        n: An integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        A DiscreteFuzzyAggregationOperator object.
    """
    if tnorm == Tnorm.MINIMUM:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=minimum_tnorm)
    elif tnorm == Tnorm.DRASTIC:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=drastic_tnorm)
    elif tnorm == Tnorm.NILPOTENT_MINIMUM:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=nilpotent_minimum)
    elif tnorm == Tnorm.LUKASIEWICZ:
        return DiscreteFuzzyAggregationOperator(n=n, operator_expression=lukasiewicz)


def minimum_tnorm(x: int, y: int, n: int) -> int:
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


def drastic_tnorm(x: int, y: int, n: int):
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


def nilpotent_minimum(x: int, y: int, n: int):
    """
    Implementation of the discrete nilpotent minimum t-norm.

    Args:
        x: An integer, representing the first coordinate of the evaluation point.
        y: An integer, representing the second coordinate of the evaluation point.
        n: n integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        An integer, representing the value of the t-norm in the point (x,y).
    """
    if x+y <= n:
        return 0
    return min(x, y)


def lukasiewicz(x: int, y: int, n: int):
    """
    Implementation of the discrete Lukasiewicz t-norm.

    Args:
        x: An integer, representing the first coordinate of the evaluation point.
        y: An integer, representing the second coordinate of the evaluation point.
        n: n integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        An integer, representing the value of the t-norm in the point (x,y).
    """
    return max(0, x+y-n)
# endregion
