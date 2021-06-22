from typing import List

from discrete_fuzzy_operators.base.decision_making.two_tuple import TwoTuple
from discrete_fuzzy_operators.base.exceptions.decision_making.owa_bad_weight_definition import OwaBadDefinition
from discrete_fuzzy_operators.base.exceptions.decision_making.owa_bad_weight_length import OwaBadLength


def two_tuple_arithmetic_mean_aggregation(tuples: List[TwoTuple]) -> TwoTuple:
    """
    Computes the 2-tuple arithmetic mean aggregation with respect to a set of weights.

    Args:
        tuples: A list of two-tuples, representing the set of tuples to be aggregated.

    Returns:
        A 2-tuple, representing the aggregated 2-tuple with respect to the arithmetic mean.
    """
    mean = 0
    term_set = tuples[0].context

    for two_tuple in tuples:
        mean = mean+term_set.inverse_delta(two_tuple)
    mean = mean/len(tuples)

    return term_set.delta(value=mean)


def two_tuple_weighted_average_aggregation(tuples: List[TwoTuple], weights: List[float]) -> TwoTuple:
    """
    Computes the 2-tuple weighted average aggregation with respect to a set of weights.

    Args:
        tuples: A list of two-tuples, representing the set of tuples to be aggregated.
        weights: A list of weights.

    Returns:
        A 2-tuple, representing the aggregated 2-tuple with respect to the weighted average.
    """
    if len(tuples) != len(weights):
        raise OwaBadLength()

    weighted_average = 0
    term_set = tuples[0].context

    for two_tuple_position, two_tuple in enumerate(tuples):
        weighted_average = weighted_average+term_set.inverse_delta(two_tuple)*weights[two_tuple_position]
    weighted_average = weighted_average/sum(weights)

    return term_set.delta(weighted_average)


def two_tuple_ordered_weighted_average_aggregation(tuples: List[TwoTuple], weights: List[float]) -> TwoTuple:
    """
    Computes the 2-tuple ordered weighted aggregation with respect to a set of weights.

    Args:
        tuples: A list of two-tuples, representing the set of tuples to be aggregated.
        weights: A list of ordered weights, sorted increasingly. Each entry of the list must be a float value between
                 0 and 1, and the sum of all values must be 1.

    Returns:
        A 2-tuple, representing the aggregated 2-tuple with respect to the ordered weighted average.
    """
    if len(tuples) != len(weights):
        raise OwaBadLength()
    elif sorted(weights) != weights or sum(weights) != 1:
        raise OwaBadDefinition()

    term_set = tuples[0].context

    betas = sorted([two_tuple.alpha+two_tuple.label for two_tuple in tuples])
    betas.reverse()

    ordered_weighted_average = 0
    for i in range(0, len(tuples)):
        ordered_weighted_average = ordered_weighted_average+weights[i]*betas[i]

    return term_set.delta(value=ordered_weighted_average)
