from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.copula import Copula
from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
from discrete_fuzzy_operators.counters.aggregation_functions.discrete_commutative_aggregation_function_counter import DiscreteCommutativeAggregationFunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_commutative_conjunctions_counter import DiscreteCommutativeConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_conjunctions_counter import DiscreteConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_consequent_boundary_conjunctions_counter import DiscreteConsequentBoundaryConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_identity_principle_conjunctions_counter import DiscreteIdentityPrincipleConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_neutrality_principle_conjunctions_counter import DiscreteNeutralityPrincipleConjunctionsCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_ordering_principle_conjunctions_counter import DiscreteOrderingPrincipleConjunctionsCounter
from discrete_fuzzy_operators.counters.implications.discrete_consequent_boundary_implications_counter import DiscreteConsequentBoundaryImplicationsCounter
from discrete_fuzzy_operators.counters.implications.discrete_identity_principle_implications_counter import DiscreteIdentityPrincipleImplicationsCounter
from discrete_fuzzy_operators.counters.implications.discrete_ordering_principle_implications_counter import DiscreteOrderingPrincipleImplicationsCounter
from discrete_fuzzy_operators.counters.negations.discrete_negations_counter import DiscreteNegationsCounter

from sklearn.linear_model import LinearRegression
import numpy as np
from math import log, exp

if __name__ == "__main__":


    n_values = []
    count_values = []

    for n in range(2, 40):

        negations_counter = DiscreteConjunctionsCounter(n=n)

        n_values.append([n])
        count_values.append(log(negations_counter.count_operators()))

    X = np.array(n_values)
    y = np.array(count_values)

    model = LinearRegression().fit(X, y)

    print(model.score(X, y))
    print(exp(model.coef_))
    print(exp(model.intercept_))

    """
    import itertools

    n = 7
    number_archimedean = 0
    for permutation in itertools.permutations(range(1, n+1)):

        copula = Copula(n=n, permutation=list(permutation))
        if copula.is_archimedean():
            number_archimedean += 1
    print(number_archimedean)
    """

    """
    negations_counter = DiscreteNegationsCounter(n=n)
    print(f"Number of discrete negations with n={n}: {negations_counter.count_operators()}")

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

    op_implications_counter = DiscreteOrderingPrincipleImplicationsCounter(n=n)
    print(f"Number of discrete implications which satisfy OP with n={n}: {op_implications_counter.count_operators()}")

    ip_conjunctions_counter = DiscreteIdentityPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions which satisfy IP with n={n}: {ip_conjunctions_counter.count_operators()}")

    ip_implications_counter = DiscreteIdentityPrincipleImplicationsCounter(n=n)
    print(f"Number of discrete implications which satisfy IP with n={n}: {ip_implications_counter.count_operators()}")

    np_conjunctions_counter = DiscreteNeutralityPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions which satisfy NP with n={n}: {np_conjunctions_counter.count_operators()}")

    np_implications_counter = DiscreteNeutralityPrincipleConjunctionsCounter(n=n)
    print(f"Number of discrete implications which satisfy NP with n={n}: {np_implications_counter.count_operators()}")

    cb_conjunction_counter = DiscreteConsequentBoundaryConjunctionsCounter(n=n)
    print(f"Number of discrete conjunctions which satisfy CB with n={n}: {cb_conjunction_counter.count_operators()}")

    cb_implications_counter = DiscreteConsequentBoundaryImplicationsCounter(n=n)
    print(f"Number of discrete implications which satisfy CB with n={n}: {cb_implications_counter.count_operators()}")
    """