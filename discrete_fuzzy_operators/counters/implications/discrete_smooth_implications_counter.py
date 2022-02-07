from discrete_fuzzy_operators.counters.conjunctions.discrete_smooth_conjunctions_counter import DiscreteSmoothConjunctionsCounter


class DiscreteSmoothImplicationsCounter(DiscreteSmoothConjunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete implications which are smooth in each argument
        over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteSmoothImplicationsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of smooth discrete implications defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of discrete conjunctions.
        """
        return super().count_operators()
