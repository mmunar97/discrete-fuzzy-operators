from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
from math import comb
from typing import Dict, Generator, List

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
        if self.n == 1:
            return 1
        identity = [i for i in range(1, self.n + 1)]
        np_count, _ = DiscreteNeutralityPrincipleConjunctionsCounter.fixed_column_counter(n=self.n, restrictions=identity)
        return np_count

    @staticmethod
    def fixed_column_counter(n: int, restrictions: List[int]) -> (int, Dict[str, int]):
        """
        Counts how many plane partitions there are such that their first column is equal to a given decreasing sequence.
        The computation is carried out using the recursive expression proposed by the authors; since the recursion
        repeats the previous terms, each recursive value is stored in a dictionary in order to avoid repeating computations.

        Args:
            n: An integer, representing the length of the restrictions.
            restrictions: An increasing sequence of integers, representing the restrictions of the first column. Its
                          length must match the parameter n.

        Returns:
            An integer, representing the number of plane partitions whose first column is equal to a given sequence of restrictions.
        """
        partial_fixed_column_values = {}

        decreasing_sequences = [dec_seq for dec_seq in DiscreteNeutralityPrincipleConjunctionsCounter.generate_decreasing_sequences(upper_bounds=restrictions, max_size=n)]
        decreasing_sequences.sort()

        for decreasing_sequence in decreasing_sequences:
            string_representation = ",".join(str(x) for x in decreasing_sequence)
            partial_fixed_column_values[string_representation] = 0

        for i in range(0, n + 1):
            reduced_sequence = "0," * (n - 1) + f"{i}"
            partial_fixed_column_values[reduced_sequence] = comb(n + i - 1, i)

        values_keys = list(partial_fixed_column_values.keys())
        for i in range(n + 1, len(values_keys)):

            vector = [int(x) for x in values_keys[i].split(",")]
            vector.reverse()

            column_vector_value = DiscreteNeutralityPrincipleConjunctionsCounter.bounded_plane_partition_counter(n=n, restrictions=vector)
            for j in range(0, i):
                s1 = values_keys[j][::-1]
                s2 = values_keys[i][::-1]

                if DiscreteNeutralityPrincipleConjunctionsCounter.__lexicographic_order(s1, s2):
                    column_vector_value -= partial_fixed_column_values[values_keys[j]]

            partial_fixed_column_values[values_keys[i]] = column_vector_value

        reverse_restrictions = restrictions.copy()
        reverse_restrictions.reverse()

        fixed_column_count = DiscreteNeutralityPrincipleConjunctionsCounter.bounded_plane_partition_counter(n=n, restrictions=reverse_restrictions) - sum(list(partial_fixed_column_values.values()))

        return fixed_column_count, partial_fixed_column_values

    @staticmethod
    def generate_decreasing_sequences(upper_bounds: List[int], max_size: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
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
                yield from DiscreteNeutralityPrincipleConjunctionsCounter.generate_decreasing_sequences(upper_bounds=upper_bounds,
                                                                                                        max_size=max_size,
                                                                                                        recursion_depth=recursion_depth + 1,
                                                                                                        restrictions=temp_restrictions)
        elif 0 < recursion_depth < max_size:
            for x in range(restrictions[recursion_depth - 1], upper_bounds[recursion_depth] + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteNeutralityPrincipleConjunctionsCounter.generate_decreasing_sequences(upper_bounds=upper_bounds,
                                                                                                        max_size=max_size,
                                                                                                        recursion_depth=recursion_depth + 1,
                                                                                                        restrictions=temp_restrictions)
        else:
            if restrictions != upper_bounds:
                yield restrictions

    @staticmethod
    def bounded_plane_partition_counter(n: int, restrictions: List[int]) -> int:
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
    def __lexicographic_order(s1: str, s2: str):
        """
        Compares two decreasing sequences of integers, represented as comma-separated strings. ç
        By default, the order is the lexicographic.

        Args:
            s1: A string, representing the string representation of a decreasing vector.
            s2: A string, representing the string representation of a decreasing vector.

        Returns:
            A boolean, indicating if the first vector is less than or equal to the second one.
        """
        s1_values = [int(x) for x in s1.split(",")]
        s2_values = [int(x) for x in s2.split(",")]

        for i in range(0, len(s1_values)):
            if s1_values[i] > s2_values[i]:
                return False
        return True
