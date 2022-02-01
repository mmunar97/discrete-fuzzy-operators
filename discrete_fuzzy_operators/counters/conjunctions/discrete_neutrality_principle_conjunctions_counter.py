from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
from math import comb, factorial
from typing import Generator, List

import numpy


class DiscreteNeutralityPrincipleConjunctionsCounter(DiscreteAggregationFunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete conjunctions which satisfy the
        neutrality principle for conjunctions over the finite chain Ln; that is, the conjunctions
        that C(n,y) = y for all y in Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteNeutralityPrincipleConjunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete conjunctions which satisfy (NP) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        identity = [i for i in range(self.n, 0, -1)]
        return DiscreteNeutralityPrincipleConjunctionsCounter.__fixed_column_counter(n=self.n, restrictions=identity)


    @staticmethod
    def __fixed_column_counter(n: int, restrictions: List[int]) -> int:
        """
        Counts the number of plane partitions whose first column is equal to a given vector.

        Args:
            n: An integer, representing the size of the plane partition.
            restrictions: A list of integers, representing the values to be set in the first column.

        Returns:
            An integer, representing the number of plane partitions whose first column is given.
        """
        if DiscreteNeutralityPrincipleConjunctionsCounter.__is_reduced_sequence(vector=restrictions):
            return comb(n + restrictions[0] - 1, restrictions[0])
        else:
            sum_value = DiscreteNeutralityPrincipleConjunctionsCounter.__bounded_plane_partition_counter(n, restrictions)
            rev_restrictions = restrictions.copy()
            rev_restrictions.reverse()
            for vector in DiscreteNeutralityPrincipleConjunctionsCounter.__generate_decreasing_sequences(upper_bounds=rev_restrictions,
                                                                                                         max_size=n):
                sum_value -= DiscreteNeutralityPrincipleConjunctionsCounter.__fixed_column_counter(n=n, restrictions=vector)
            return sum_value

    @staticmethod
    def __bounded_plane_partition_counter(n: int, restrictions: List[int]):
        """
        Counts the number of plane partitions whose first column is upper-bounded by a vector.

        Args:
            n: An integer, representing the size of the plane partition.
            restrictions: A list of integers, decreasingly sorted, representing the upper bound of the first column.

        Returns:
            An integer, representing the number of plane partitions with bounded column.
        """
        combination_matrix = numpy.zeros((n, n))
        for s in range(1, n + 1):
            for t in range(1, n + 1):
                combination_matrix[s - 1, t - 1] = comb(n + restrictions[t - 1], n - s + t)

        return round(numpy.linalg.det(combination_matrix))

    @staticmethod
    def __generate_decreasing_sequences(upper_bounds: List[int], max_size: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
        """
        Generates all possible vectors of size n whose entries are decreasing and each value is less than or equal to the
        restriction of the same position.

        Args:
            upper_bounds: A list of integers, representing the restrictions of the previous row.
            max_size: An integer, representing the dimension of the finite chain.
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
                yield from DiscreteNeutralityPrincipleConjunctionsCounter.__generate_decreasing_sequences(upper_bounds=upper_bounds,
                                                                                                          max_size=max_size,
                                                                                                          recursion_depth=recursion_depth + 1,
                                                                                                          restrictions=temp_restrictions)
        elif 0 < recursion_depth < max_size:
            for x in range(restrictions[recursion_depth - 1], upper_bounds[recursion_depth] + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteNeutralityPrincipleConjunctionsCounter.__generate_decreasing_sequences(upper_bounds=upper_bounds,
                                                                                                          max_size=max_size,
                                                                                                          recursion_depth=recursion_depth + 1,
                                                                                                          restrictions=temp_restrictions)
        else:
            if restrictions != upper_bounds:
                restrictions.reverse()
                yield restrictions

    @staticmethod
    def __is_reduced_sequence(vector: List[int]) -> bool:
        """
        Checks if a decreasing sequence is reduced; that is, if all entries from the second position to the end are equal to zero.

        Args:
            vector: A sequence of integers, decreasingly sorted.

        Returns:
            A boolean, representing if the sequence of vectors is reduced.
        """
        for i in range(1, len(vector)):
            if vector[i] != 0:
                return False
        return True
