from typing import List

from discrete_fuzzy_operators.decision_making.yager_aggregation import yager_aggregation_decision_making


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


if __name__ == "__main__":
    assessments = [[4, 3, 1, 4, 0], [1, 0, 4, 1, 3], [1, 4, 4, 2, 4], [2, 4, 0, 3, 4], [1, 2, 1, 2, 4], [3, 4, 3, 4, 2]]

    optimistic_yager_decision = yager_aggregation_decision_making(assessments=assessments,
                                                                  aggregation_function=optimistic_aggregation)
    print(f"Using the optimistic Yager decision the best alternative is number {optimistic_yager_decision[0]}")

    pessimistic_yager_decision = yager_aggregation_decision_making(assessments=assessments,
                                                                   aggregation_function=pessimistic_aggregation)
    print(f"Using the pessimistic Yager decision the best alternative is number {pessimistic_yager_decision[0]}")
