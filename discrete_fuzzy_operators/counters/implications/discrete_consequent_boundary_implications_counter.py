from discrete_fuzzy_operators.counters.conjunctions.discrete_neutrality_principle_conjunctions_counter import DiscreteNeutralityPrincipleConjunctionsCounter


class DiscreteConsequentBoundaryImplicationsCounter(DiscreteNeutralityPrincipleConjunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which satisfy the
        consequent boundary over the finite chain Ln; that is, the implications
        that I(x,y) >= y for all x,y in Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteConsequentBoundaryImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications which satisfy (CB) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return super().count_operators()
