from discrete_fuzzy_operators.base.decision_making.two_tuple import TwoTuple, LinguisticTermSet
from discrete_fuzzy_operators.decision_making.two_tuple_aggregation import *

if __name__ == "__main__":

    term_set = LinguisticTermSet(term_set=[0, 1, 2, 3, 4])

    # EXAMPLE 1: Determination of the best alternative among different expert assessments.
    two_tuples_set1 = [TwoTuple(label_index=0, alpha=0, context=term_set),
                       TwoTuple(label_index=2, alpha=0, context=term_set),
                       TwoTuple(label_index=3, alpha=0, context=term_set),
                       TwoTuple(label_index=3, alpha=0, context=term_set)]

    two_tuples_set2 = [TwoTuple(label_index=2, alpha=0, context=term_set),
                       TwoTuple(label_index=1, alpha=0, context=term_set),
                       TwoTuple(label_index=0, alpha=0, context=term_set),
                       TwoTuple(label_index=3, alpha=0, context=term_set)]

    two_tuples_set3 = [TwoTuple(label_index=2, alpha=0, context=term_set),
                       TwoTuple(label_index=0, alpha=0, context=term_set),
                       TwoTuple(label_index=2, alpha=0, context=term_set),
                       TwoTuple(label_index=1, alpha=0, context=term_set)]

    two_tuples_set4 = [TwoTuple(label_index=1, alpha=0, context=term_set),
                       TwoTuple(label_index=3, alpha=0, context=term_set),
                       TwoTuple(label_index=2, alpha=0, context=term_set),
                       TwoTuple(label_index=1, alpha=0, context=term_set)]

    print("EXAMPLE 1: Aggregation of the assessments using arithmetic mean aggregation")
    print(two_tuple_arithmetic_mean_aggregation(tuples=two_tuples_set1))
    print(two_tuple_arithmetic_mean_aggregation(tuples=two_tuples_set2))
    print(two_tuple_arithmetic_mean_aggregation(tuples=two_tuples_set3))
    print(two_tuple_arithmetic_mean_aggregation(tuples=two_tuples_set4))

    # EXAMPLE 2: Aggregation of tuples using weighted averaging
    tuples = [TwoTuple(label_index=1, alpha=0, context=term_set),
              TwoTuple(label_index=3, alpha=0, context=term_set),
              TwoTuple(label_index=2, alpha=0, context=term_set),
              TwoTuple(label_index=0, alpha=0, context=term_set)]
    weights = [0.2, 0.15, 0.5, 0.15]

    print("EXAMPLE 2: Aggregation of tuples using weighted averaging")
    print(two_tuple_weighted_average_aggregation(tuples=tuples, weights=weights))
