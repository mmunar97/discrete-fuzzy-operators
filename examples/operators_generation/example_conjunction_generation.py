from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.conjunction import Conjunction
from discrete_fuzzy_operators.counters.conjunctions.discrete_commutative_conjunctions_recursive_counter import DiscreteCommutativeConjunctionsRecursiveCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_conjunctions_exhaustive_recursion_counter import DiscreteConjunctionsExhaustiveRecursionCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_conjunctions_fast_recursion_counter import DiscreteConjunctionsFastRecursionCounter
from discrete_fuzzy_operators.generators.conjunctions.discrete_conjunctions_recursive_generator import DiscreteConjunctionsRecursiveGenerator

from time import time


if __name__ == "__main__":

    t = time()
    counter = DiscreteConjunctionsExhaustiveRecursionCounter(n=6)
    print(counter.count_operators())
    print(f"Exhaustive conjunction counter finished. Elapsed time: {round(time()-t, 4)} s")

    t = time()
    counter = DiscreteConjunctionsFastRecursionCounter(n=6)
    print(counter.count_operators())
    print(f"Fast conjunction counter finished. Elapsed time: {round(time()-t, 4)} s")
