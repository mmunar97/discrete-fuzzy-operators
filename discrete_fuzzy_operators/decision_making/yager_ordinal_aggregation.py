from typing import List, Tuple


def yager_ordinal_decision_making(assessments: List[List[int]], weights: List[int]) -> Tuple[int, int]:
    """
    Computes the best alternative from a matrix of assessments. The matrix contains, in each row, the assessment made
    in a certain alternative for all the experts.

    The method computes, for each row, the value of the ordinal aggregation function; then, select the alternative which
    associated value is greater.

    References:
        Yager, R. R. (1995). An approach to ordinal decision making.
        International Journal of Approximate Reasoning, 12(3), 237–261.
        https://doi.org/https://doi.org/10.1016/0888-613X(94)00035-2

    Args:
        assessments: A list of list of integers, containing in each row the assessments made of that alternative by
                     different experts. The number of rows of the matrix must agree with the number of alternatives,
                     and the number of columns with the number of experts.
        weights: A list of increasing integers, representing the weight dedicated to each expert.

    Returns:
        A tuple of two values: the first, representing the index of the alternative that has the best value; the second,
        the value of the aggregation function that reaches the maximum.
    """
    aggregation_values = [__yager_ordinal_weighted_averaging(alternative_assessment, weights)
                          for alternative_assessment in assessments]
    return aggregation_values.index(max(aggregation_values)), max(aggregation_values)


def __yager_ordinal_weighted_averaging(alternative_assessment: List[int], weights: List[int]) -> int:
    """
    Computes the Yager's ordinal weighted averaging.

    References:
        Yager, R. R. (1995). An approach to ordinal decision making.
        International Journal of Approximate Reasoning, 12(3), 237–261.
        https://doi.org/https://doi.org/10.1016/0888-613X(94)00035-2

    Returns:
        An integer, representing the value of the Yager's ordinal weighted averaging.
    """
    sorted_assessments = sorted(alternative_assessment)
    sorted_assessments.reverse()

    values = [min(weights[j], sorted_assessments[j]) for j in range(len(alternative_assessment))]

    return max(values)
