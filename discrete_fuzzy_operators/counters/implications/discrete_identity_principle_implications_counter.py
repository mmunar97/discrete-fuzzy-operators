from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_identity_principle_conjunctions_counter import DiscreteIdentityPrincipleConjunctionsCounter


class DiscreteIdentityPrincipleImplicationsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which satisfy the identity
        principle over the finite chain Ln; that is, the discrete implications such that I(x,x)=n if.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteIdentityPrincipleImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications which satisfy (IP) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return DiscreteIdentityPrincipleConjunctionsCounter(self.n).count_operators()
