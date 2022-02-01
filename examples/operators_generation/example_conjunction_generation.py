from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
from discrete_fuzzy_operators.counters.aggregation_functions.discrete_commutative_aggregation_function_counter import DiscreteCommutativeAggregationFunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_commutative_conjunctions_counter import DiscreteCommutativeConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_conjunctions_counter import DiscreteConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_neutrality_principle_conjunctions_counter import DiscreteNeutralityPrincipleConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_ordering_conjunctions_counter import DiscreteOrderingPrincipleConjunctionsCounter
from discrete_fuzzy_operators.counters.implications.discrete_ordering_implications_counter import DiscreteOrderingImplicationsCounter

if __name__ == "__main__":

    n = 4

    aggregation_function_counter = DiscreteAggregationFunctionsCounter(n=n)
    print(f"Number of discrete aggregation functions with n={n}: {aggregation_function_counter.count_operators()}")

    commutative_aggregation_function_counter = DiscreteCommutativeAggregationFunctionsCounter(n=n)
    print(f"Number of commutative discrete aggregation functions with n={n}: {commutative_aggregation_function_counter.count_operators()}")

    conjunctions_counter = DiscreteConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions with n={n}: {conjunctions_counter.count_operators()}")

    commutative_conjunctions_counter = DiscreteCommutativeConjunctionsCounter(n=n)
    print(f"Number of commutative discrete conjunctions with n={n}: {commutative_conjunctions_counter.count_operators()}")

    op_conjunctions_counter = DiscreteOrderingPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions which satisfy OP with n={n}: {op_conjunctions_counter.count_operators()}")

    op_implications_counter = DiscreteOrderingImplicationsCounter(n=n)
    print(f"Number of discrete implications which satisfy OP with n={n}: {op_implications_counter.count_operators()}")

    np_conjunctions_counter = DiscreteNeutralityPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions which satisfy NP with n={n}: {np_conjunctions_counter.count_operators()}")

    np_implications_counter = DiscreteNeutralityPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete implications which satisfy NP with n={n}: {np_implications_counter.count_operators()}")
