from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_ordering_principle_conjunctions_counter import DiscreteOrderingPrincipleConjunctionsCounter


class DiscreteOrderingPrincipleImplicationsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which satisfy the ordering
        principle over the finite chain Ln; that is, the discrete implications such that I(x,y)=n if, and
        only if, x <= y.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteOrderingPrincipleImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications which satisfy (OP) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return DiscreteOrderingPrincipleConjunctionsCounter(self.n).count_operators()
