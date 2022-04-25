from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
import decimal


class DiscreteConjunctionsCounter(DiscreteAggregationFunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete conjunctions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteConjunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete conjunctions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of discrete conjunctions.
        """
        count = self.plane_partition_counter(a=self.n, b=self.n, c=self.n)-self.plane_partition_counter(a=self.n, b=self.n, c=self.n-1)
        return int(count.to_integral(rounding=decimal.ROUND_HALF_DOWN))