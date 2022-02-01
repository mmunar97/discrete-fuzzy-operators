from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from discrete_fuzzy_operators.counters.conjunctions.discrete_commutative_conjunctions_counter import DiscreteCommutativeConjunctionsCounter


class DiscreteContrapositiveSymmetryImplicationsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which satisfy the contrapositive
         symmetry with respect to the unique discrete strong negation over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteContrapositiveSymmetryImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete implications which satisfy CP(N_c) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return DiscreteCommutativeConjunctionsCounter(self.n).count_operators()
