from typing import List

from discrete_fuzzy_operators.decision_making.yager_ordinal_aggregation import yager_ordinal_decision_making


if __name__ == "__main__":

    # EXAMPLE 1: Computation of the Yager ordinal weighted aggregation.
    assessments = [[3, 2, 4, 1]]
    weights = [1, 3, 5, 5]

    yager_decision = yager_ordinal_decision_making(assessments=assessments, weights=weights)
    print("EXAMPLE 1:")
    print(f"\t Using the ordinal Yager aggregation function the value  is {yager_decision[1]}.")

    # EXAMPLE 2: Decision making
    assessments = [[0, 2, 3, 3], [2, 1, 0, 3], [2, 0, 2, 1], [1, 3, 2, 1]]
    weights = [1, 3, 5, 5]

    yager_decision = yager_ordinal_decision_making(assessments=assessments, weights=weights)
    print("EXAMPLE 2:")
    print(f"\t Using the ordinal Yager decision the best alternative is number {yager_decision[0]}")
