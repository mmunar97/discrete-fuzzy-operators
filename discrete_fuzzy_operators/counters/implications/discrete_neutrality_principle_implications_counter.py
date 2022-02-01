from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_neutrality_principle_conjunctions_counter import DiscreteNeutralityPrincipleConjunctionsCounter


class DiscreteNeutralityPrincipleImplicationsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which satisfy the neutrality principle
        over the finite chain Ln; that is, the discrete implications such that I(n,y)=y for all y in Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteNeutralityPrincipleImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications which satisfy (NP) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return DiscreteNeutralityPrincipleConjunctionsCounter(self.n).count_operators()
