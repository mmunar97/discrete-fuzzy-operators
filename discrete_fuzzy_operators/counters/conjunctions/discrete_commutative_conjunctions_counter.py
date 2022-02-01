from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.aggregation_functions.discrete_commutative_aggregation_function_counter import DiscreteCommutativeAggregationFunctionsCounter


class DiscreteCommutativeConjunctionsCounter(DiscreteCommutativeAggregationFunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible commutative discrete conjunctions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteCommutativeConjunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of commutative discrete conjunctions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of commutative discrete conjunctions.
        """
        return self.symmetric_plane_partition_counter(a=self.n, c=self.n)-self.symmetric_plane_partition_counter(a=self.n, c=self.n-1)
