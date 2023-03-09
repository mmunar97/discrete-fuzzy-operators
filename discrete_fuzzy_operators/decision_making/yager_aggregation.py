from typing import Callable, List, Tuple


def yager_aggregation_decision_making(assessments: List[List[int]], aggregation_function: Callable[[List[int]], int]) -> Tuple[List[int], Tuple[int, int]]:
    """
    Computes the best alternative from a matrix of assessments. The matrix contains, in each row, the assessment made
    in a certain alternative for all the experts.

    The method computes, for each row, the value of the aggregation function; then, select the alternative which
    associated value is greater.

    References:
        Yager, R. R. (1995). An approach to ordinal decision making.
        International Journal of Approximate Reasoning, 12(3), 237–261.
        https://doi.org/https://doi.org/10.1016/0888-613X(94)00035-2

    Args:
        assessments: A list of list of integers, containing in each row the assessments made of that alternative by
                     different experts. The number of rows of the matrix must agree with the number of alternatives,
                     and the number of columns with the number of experts.
        aggregation_function: A callable method which receives as a parameter the list of values to be aggregated.
                              Since the aggregation must be an ordinal value, the output of the function must be an
                              integer.

    Returns:
        A tuple of two values:
            - The first one, the aggregations of each alternative with respect to all experts, in the same order as
               provided. If the aggregation_function parameter is not associative, the results are not order-free.
            - The second one, a tuple of two vañues. The first, representing the index of the alternative that
               has the best value; the second, the value of the aggregation function that reaches the maximum.
    """
    aggregation_values = [aggregation_function(alternative_assessment) for alternative_assessment in assessments]
    return aggregation_values, (aggregation_values.index(max(aggregation_values)), max(aggregation_values))
