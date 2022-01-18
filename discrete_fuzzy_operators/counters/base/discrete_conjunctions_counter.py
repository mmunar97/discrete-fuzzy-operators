from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from typing import Generator, List


class DiscreteConjunctionsCounter(DiscreteOperatorCounter):

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
        pass

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
        pass

    @staticmethod
    def generate_restrictions(upper_bounds: List[int], n: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
        """
        Generates all possible vectors of size n whose entries are increasing and each value is less than or equal to the
        restriction of the same position.

        Args:
            upper_bounds: A list of integers, representing the restrictions of the previous row.
            n: An integer, representing the dimension of the finite chain.
            recursion_depth: An integer, representing the position of the vector that is being generated.
            restrictions: A list of integers, representing the temporal vector to be generated.

        Returns:
            A generator of increasing vectors whose entries satisfy upper restrictions.
        """
        if restrictions is None:
            restrictions = []

        if recursion_depth == 0:
            for x in range(0, upper_bounds[recursion_depth] + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteConjunctionsCounter.generate_restrictions(upper_bounds=upper_bounds, n=n, recursion_depth=recursion_depth + 1,
                                                                             restrictions=temp_restrictions)
        elif 0 < recursion_depth < n:
            for x in range(restrictions[recursion_depth - 1], upper_bounds[recursion_depth] + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteConjunctionsCounter.generate_restrictions(upper_bounds=upper_bounds, n=n, recursion_depth=recursion_depth + 1,
                                                                             restrictions=temp_restrictions)
        else:
            yield restrictions

    @staticmethod
    def generate_initial_restrictions(n: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
        """
        Generates all possible vectors of size n whose entries are increasing and each value is less than or equal to n, that will
        be used as initial seed of the recursive counter.

        Args:
            n: An integer, representing the dimension of the finite chain.
            recursion_depth: An integer, representing the position of the vector that is being generated.
            restrictions: A list of integers, representing the temporal vector to be generated.

        Returns:
            A generator of increasing vectors whose entries are bounded above by n.
        """
        if restrictions is None:
            restrictions = []

        if recursion_depth == 0:
            for x in range(0, n + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteConjunctionsCounter.generate_initial_restrictions(n=n, recursion_depth=recursion_depth + 1,
                                                                                     restrictions=temp_restrictions)
        elif 0 < recursion_depth < n - 1:
            for x in range(restrictions[recursion_depth - 1], n + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteConjunctionsCounter.generate_initial_restrictions(n=n, recursion_depth=recursion_depth + 1,
                                                                                     restrictions=temp_restrictions)
        else:
            temp_restrictions = restrictions.copy()
            temp_restrictions.append(n)
            yield temp_restrictions
