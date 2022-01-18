from typing import List

from discrete_fuzzy_operators.decision_making.yager_ordinal_aggregation import yager_ordinal_decision_making


if __name__ == "__main__":

    # EXAMPLE 1: Computation of the Yager ordinal weighted aggregation.
    assessments = [[4, 4, 3, 1, 0]]
    weights = [2, 4, 4, 5, 7]

    yager_decision = yager_ordinal_decision_making(assessments=assessments, weights=weights)
    print("EXAMPLE 1:")
    print(f"\t Using the ordinal Yager aggregation function the value  is {yager_decision[1]}.")

    # EXAMPLE 2: Decision making
    assessments = [[4, 3, 1, 4, 0], [1, 0, 4, 1, 3], [1, 4, 4, 2, 4], [2, 4, 0, 3, 4], [1, 2, 1, 2, 4], [3, 4, 3, 4, 2]]
    weights = [0, 2, 2, 4, 4, 4]

    yager_decision = yager_ordinal_decision_making(assessments=assessments, weights=weights)
    print("EXAMPLE 2:")
    print(f"\t Using the ordinal Yager decision the best alternative is number {yager_decision[0]}")
