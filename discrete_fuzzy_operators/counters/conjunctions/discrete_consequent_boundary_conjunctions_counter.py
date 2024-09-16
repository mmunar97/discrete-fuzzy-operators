from discrete_fuzzy_operators.counters.conjunctions.discrete_neutrality_principle_conjunctions_counter import DiscreteNeutralityPrincipleConjunctionsCounter


class DiscreteConsequentBoundaryConjunctionsCounter(DiscreteNeutralityPrincipleConjunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete conjunctions which satisfy the
        consequent boundary for conjunctions over the finite chain Ln; that is, the conjunctions
        that C(x,y) <= y for all x,y in Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteConsequentBoundaryConjunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete conjunctions which satisfy (CB) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        identity = [i for i in range(1, self.n + 1)]
        np_count, partial_fixed_column_counts = DiscreteNeutralityPrincipleConjunctionsCounter.fixed_column_counter(n=self.n, restrictions=identity)

        cb_count = 0
        for seq in self.generate_decreasing_sequences(upper_bounds=identity, max_size=self.n):
            if seq[self.n-1] == self.n:
                string_representation = ",".join(str(x) for x in seq)
                cb_count += partial_fixed_column_counts[string_representation]

        cb_count += np_count
        return cb_count
