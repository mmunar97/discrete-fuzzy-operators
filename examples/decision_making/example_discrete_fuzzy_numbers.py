from discrete_fuzzy_operators.base.decision_making.discrete_fuzzy_numbers.discrete_fuzzy_number import \
    DiscreteFuzzyNumber

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import \
    DiscreteFuzzyAggregationBinaryOperator
from discrete_fuzzy_operators.builtin_operators.discrete.tnorms import TnormExamples
from typing import Tuple


def custom_idempotent_uninorm(x, y, n) -> int:
    if y <= 8 - x:
        return min(x, y)
    else:
        return max(x, y)


def custom_idempotent_uninorm_global(x, y, n) -> int:
    if 4 <= x <= 8 and 4 <= y <= 8:
        return max(x, y)
    else:
        return min(x, y)


def xu_yager_order(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool:
    a, b = interval1
    c, d = interval2

    if (a+b < c+d) or (a+b == c+d and b-a <= d-c):
        return True
    return False


if __name__ == "__main__":

    # EXAMPLE 1
    dfn1 = DiscreteFuzzyNumber(fuzzy_number={3: 0.3, 4: 1, 5: 1, 6: 0.75, 7: 0.5}, n=8)
    dfn2 = DiscreteFuzzyNumber(fuzzy_number={2: 0.3, 3: 0.5, 4: 1, 5: 0.75, 6: 0.3}, n=8)

    print(f"Support of DFN1: {dfn1.support()}")
    print(f"Support of DFN2: {dfn2.support()}")

    print(f"0.5-cut of DFN1: {dfn1.cut(alpha=0.5)}")
    print(f"0.5-cut of DFN2: {dfn2.cut(alpha=0.5)}")

    lukasiewicz_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.LUKASIEWICZ, n=8)
    nilpotent_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.NILPOTENT_MINIMUM, n=8)

    aggregation_lk = dfn1.aggregate(other=dfn2, discrete_aggregation_function=lukasiewicz_operator)
    aggregation_nm = dfn1.aggregate(other=dfn2, discrete_aggregation_function=nilpotent_operator)

    DiscreteFuzzyNumber.plot_discrete_fuzzy_numbers(discrete_fuzzy_numbers=[aggregation_lk, aggregation_nm, dfn1, dfn2],
                                                    discrete_fuzzy_numbers_titles=["Aggregation with Lukasiewicz",
                                                                                   "Aggregation with nilpotent minimum",
                                                                                   "DFN1", "DFN2"],
                                                    figure_size=(900, 600))

    # EXAMPLE 2 (Uninorms and nullnorms on the set of discrete fuzzy numbers)
    o1_p1 = DiscreteFuzzyNumber(fuzzy_number={2: 0.6, 3: 1, 4: 0.8, 5: 0.7}, n=8)
    o2_p1 = DiscreteFuzzyNumber(fuzzy_number={3: 0.3, 4: 0.6, 5: 1, 6: 0.7}, n=8)
    o3_p1 = DiscreteFuzzyNumber(fuzzy_number={2: 0.7, 3: 0.8, 4: 1, 5: 0.5}, n=8)
    o1_p2 = DiscreteFuzzyNumber(fuzzy_number={6: 0.8, 7: 0.9, 8: 1}, n=8)
    o2_p2 = DiscreteFuzzyNumber(fuzzy_number={5: 0.6, 6: 0.7, 7: 1, 8: 0.7}, n=8)
    o3_p2 = DiscreteFuzzyNumber(fuzzy_number={4: 0.5, 5: 0.7, 6: 1, 7: 0.7, 8: 0.4}, n=8)
    o1_p3 = DiscreteFuzzyNumber(fuzzy_number={0: 0.1, 1: 0.6, 2: 1, 3: 0.4}, n=8)
    o2_p3 = DiscreteFuzzyNumber(fuzzy_number={3: 0.5, 4: 0.7, 5: 1}, n=8)
    o3_p3 = DiscreteFuzzyNumber(fuzzy_number={2: 0.6, 3: 0.7, 4: 1, 5: 0.8}, n=8)

    uninorm = DiscreteFuzzyAggregationBinaryOperator(n=8, operator_expression=custom_idempotent_uninorm)
    u1 = o1_p1.aggregate(o2_p1.aggregate(o3_p1, discrete_aggregation_function=uninorm),
                         discrete_aggregation_function=uninorm)
    u2 = o1_p2.aggregate(o2_p2.aggregate(o3_p2, discrete_aggregation_function=uninorm),
                         discrete_aggregation_function=uninorm)
    u3 = o1_p3.aggregate(o2_p3.aggregate(o3_p3, discrete_aggregation_function=uninorm),
                         discrete_aggregation_function=uninorm)
    print(f"Aggregation of O1_P1, O2_P1 and O3_P1: {u1}")
    print(f"Aggregation of O1_P2, O2_P2 and O3_P2: {u2}")
    print(f"Aggregation of O1_P3, O2_P3 and O3_P3: {u3}")

    # EXAMPLE 3 (Survey. Example 6.1)
    dfn1 = DiscreteFuzzyNumber(fuzzy_number={3: 0.3, 4: 0.8, 5: 1, 6: 0.75, 7: 0.5}, n=8)
    dfn2 = DiscreteFuzzyNumber(fuzzy_number={2: 0.3, 3: 0.5, 4: 1, 5: 0.75, 6: 0.3}, n=8)

    uninorm = DiscreteFuzzyAggregationBinaryOperator(n=8, operator_expression=custom_idempotent_uninorm)
    aggregation_uninorm = dfn1.aggregate(other=dfn2, discrete_aggregation_function=uninorm)

    DiscreteFuzzyNumber.plot_discrete_fuzzy_numbers(discrete_fuzzy_numbers=[dfn1, dfn2, aggregation_uninorm],
                                                    discrete_fuzzy_numbers_titles=["A", "B", "Aggregation of A and B"],
                                                    figure_size=(1000, 600))

    # EXAMPLE 4 (Survey. Example 8.2)
    o1_a1 = DiscreteFuzzyNumber(fuzzy_number={2: 0.2, 3: 0.5, 4: 1, 5: 0.6}, n=8)
    o2_a1 = DiscreteFuzzyNumber(fuzzy_number={3: 0.6, 4: 0.9, 5: 1, 6: 0.2}, n=8)
    o3_a1 = DiscreteFuzzyNumber(fuzzy_number={2: 0.3, 3: 0.4, 4: 1, 5: 0.7, 6: 0.1}, n=8)
    o1_a2 = DiscreteFuzzyNumber(fuzzy_number={4: 0.1, 5: 0.3, 6: 1, 7: 0.7}, n=8)
    o2_a2 = DiscreteFuzzyNumber(fuzzy_number={4: 0.3, 5: 0.4, 6: 0.7, 7: 1, 8: 0.1}, n=8)
    o3_a2 = DiscreteFuzzyNumber(fuzzy_number={5: 0.5, 6: 0.8, 7: 1, 8: 1}, n=8)
    o1_a3 = DiscreteFuzzyNumber(fuzzy_number={0: 0.1, 1: 1, 2: 0.6}, n=8)
    o2_a3 = DiscreteFuzzyNumber(fuzzy_number={3: 0.5, 4: 1, 5: 0.1}, n=8)
    o3_a3 = DiscreteFuzzyNumber(fuzzy_number={1: 0.6, 2: 0.7, 3: 1, 4: 0.5}, n=8)

    uninorm1 = DiscreteFuzzyAggregationBinaryOperator(n=8, operator_expression=custom_idempotent_uninorm)
    uninorm2 = DiscreteFuzzyAggregationBinaryOperator(n=8, operator_expression=custom_idempotent_uninorm_global)
    lukasiewicz_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.LUKASIEWICZ, n=8)

    u1 = o1_a1.aggregate(o2_a1.aggregate(o3_a1, discrete_aggregation_function=uninorm1),
                         discrete_aggregation_function=uninorm1)
    u2 = o1_a2.aggregate(o2_a2.aggregate(o3_a2, discrete_aggregation_function=uninorm1),
                         discrete_aggregation_function=uninorm1)
    u3 = o1_a3.aggregate(o2_a3.aggregate(o3_a3, discrete_aggregation_function=uninorm1),
                         discrete_aggregation_function=uninorm1)
    print(f"Aggregation of O1_A1, O2_A1 and O3_A1: {u1}")
    print(f"Aggregation of O1_A2, O2_A2 and O3_A2: {u2}")
    print(f"Aggregation of O1_A3, O2_A3 and O3_A3: {u3}")

    global_evaluation = u1.aggregate(u2.aggregate(u3, discrete_aggregation_function=uninorm2),
                                     discrete_aggregation_function=uninorm2)
    print(f"Overall aggregation of U1, U2 and U3: {global_evaluation}")

    print(f"The evaluation U1 is equal to the evaluation U2: {u1.total_order_equal(u2)}")
    print(f"The evaluation U1 is less than the evaluation U2: {u1.total_order_less(u2, order=xu_yager_order)}")
    print(f"The evaluation U1 is less than or equal to the evaluation U2: {u1.total_order_less_equal(u2, order=xu_yager_order)}")
