from discrete_fuzzy_operators.counters.base.discrete_conjunctions_counter import DiscreteConjunctionsCounter
from typing import List


class DiscreteConjunctionsFastRecursionCounter(DiscreteConjunctionsCounter):

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
        for initial_restrictions in DiscreteConjunctionsFastRecursionCounter.generate_initial_restrictions(n=self.n):
            value += DiscreteConjunctionsFastRecursionCounter.conjunction_counter(restrictions=initial_restrictions, r=self.n - 1, n=self.n)
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
            return DiscreteConjunctionsFastRecursionCounter.initial_conjunction_counter(i=1, j=0, x=restrictions, n=n)
        else:
            value = 0
            for limits in DiscreteConjunctionsFastRecursionCounter.generate_restrictions(upper_bounds=restrictions, n=n):
                value += DiscreteConjunctionsFastRecursionCounter.conjunction_counter(restrictions=limits, r=r - 1, n=n)
            return value

    @staticmethod
    def initial_conjunction_counter(i: int, j: int, x: List[int], n: int):
        if i == n:
            value = 0
            for k in range(j, x[i-1]+1):
                value += 1
            return value
        else:
            value = 0
            for k in range(j, x[i - 1] + 1):
                value += DiscreteConjunctionsFastRecursionCounter.initial_conjunction_counter(i=i+1, j=k, x=x, n=n)
            return value