from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from typing import Generator, List

from discrete_fuzzy_operators.counters.base.discrete_conjunctions_counter import DiscreteConjunctionsCounter


class DiscreteConjunctionsExhaustiveRecursionCounter(DiscreteConjunctionsCounter):

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
        value = 0
        for initial_restrictions in self.generate_initial_restrictions(n=self.n):
            value += DiscreteConjunctionsExhaustiveRecursionCounter.conjunction_counter(restrictions=initial_restrictions, r=self.n - 1, n=self.n)
        return value

    @staticmethod
    def conjunction_counter(restrictions: List, r: int, n: int) -> int:
        """
        Implements the recursive function that counts the number of discrete conjunctions defined over the finite chain Ln.
        Computes all the possible combinations of elements that fit in the representation matrix of the conjunctions from the
        previous row.

        Args:
            restrictions: A list of integers, representing the restrictions given by the previous row.
            r: An integer, representing the recursive step.
            n: An integer, representing the dimension of the finite chain.

        Returns:
            An integer, representing the partial operators defined over the finite chain up to the row r.
        """
        if len(restrictions) != n:
            raise Exception("The dimension of the constraints to calculate the CONJUNCTION COUNTER function does not coincide with the "
                            "value of n. ")

        if r == 1:
            value = 0
            for _ in DiscreteConjunctionsExhaustiveRecursionCounter.generate_restrictions(upper_bounds=restrictions, n=n):
                value += 1
            return value
        else:
            value = 0
            for limits in DiscreteConjunctionsExhaustiveRecursionCounter.generate_restrictions(upper_bounds=restrictions, n=n):
                value += DiscreteConjunctionsExhaustiveRecursionCounter.conjunction_counter(restrictions=limits, r=r - 1, n=n)
            return value