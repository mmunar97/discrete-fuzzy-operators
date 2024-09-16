import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.uninorm import Uninorm
from discrete_fuzzy_operators.decision_making.yager_aggregation import yager_aggregation_decision_making
from typing import List


def optimistic_aggregation(alternative_assessment: List[int]) -> int:
    """
    Aggregates the assessments of an alternative, using the maximum as aggregation function.

    Args:
        alternative_assessment: A list of integers, representing the assessments made of an alternative by a group
                                of experts.
    """
    return max(alternative_assessment)


def pessimistic_aggregation(alternative_assessment: List[int]) -> int:
    """
    Aggregates the assessments of an alternative, using the minimum as aggregation function.

    Args:
        alternative_assessment: A list of integers, representing the assessments made of an alternative by a group
                                of experts.
    """
    return min(alternative_assessment)


def uninorm_aggregation(alternative_assessment: List[int]) -> int:
    """
    Aggregates the assessments of an alternative, using a non-idempotent uninorm generated with the nilpotent minimum
    discrete t-norm and the Lukasiewicz discrete t-conorm.

    Args:
        alternative_assessment: A list of integers, representing the assessments made of an alternative by a group
                                of experts.
    """
    mat = numpy.array([[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 2, 3, 4], [0, 1, 3, 3, 4], [0, 1, 4, 4, 4]])
    custom_uninorm = Uninorm(n=4, e=2, operator_matrix=mat)

    aggregation = custom_uninorm.evaluate_operator(alternative_assessment[0], alternative_assessment[1])
    for i in range(2, 4+1):
        aggregation = custom_uninorm.evaluate_operator(aggregation, alternative_assessment[i])
    return aggregation


if __name__ == "__main__":

    assessments = [[4, 3, 1, 4, 0], [1, 0, 4, 1, 3], [1, 4, 4, 2, 4], [2, 4, 0, 3, 4], [1, 2, 1, 2, 4], [3, 4, 3, 4, 2]]

    optimistic_aggregation, optimistic_best_decision = yager_aggregation_decision_making(assessments=assessments,
                                                                                         aggregation_function=optimistic_aggregation)
    print(f"Using the optimistic Yager decision the alternatives are {optimistic_aggregation}")

    pessimistic_aggregation, pessimistic_best_decision = yager_aggregation_decision_making(assessments=assessments,
                                                                                           aggregation_function=pessimistic_aggregation)
    print(f"Using the pessimistic Yager decision the alternatives are {pessimistic_aggregation}")

    uni_aggregation, uni_best_decision = yager_aggregation_decision_making(assessments=assessments,
                                                                           aggregation_function=uninorm_aggregation)
    print(f"Using the custom uninorm with Yager decision the alternatives are {uni_aggregation}")