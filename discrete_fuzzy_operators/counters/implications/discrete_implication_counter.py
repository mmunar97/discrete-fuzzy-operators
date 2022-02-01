from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_conjunctions_counter import DiscreteConjunctionsCounter


class DiscreteImplicationsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of discrete implications.
        """
        return DiscreteConjunctionsCounter(self.n).count_operators()