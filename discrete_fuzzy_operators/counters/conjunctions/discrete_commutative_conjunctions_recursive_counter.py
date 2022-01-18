from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
from typing import Generator, List


class DiscreteCommutativeConjunctionsRecursiveCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible commutative discrete conjunctions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteCommutativeConjunctionsRecursiveCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of commutative discrete conjunctions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of commutative discrete conjunctions.
        """
        value = 0
        for initial_restrictions in DiscreteCommutativeConjunctionsRecursiveCounter.__generate_initial_restrictions(n=self.n):
            value += DiscreteCommutativeConjunctionsRecursiveCounter.__commutative_conjunction_counter(restrictions=initial_restrictions, r=self.n - 1)
        return value

    @staticmethod
    def __commutative_conjunction_counter(restrictions: List, r: int) -> int:
        """
        Implements the recursive function that counts the number of discrete conjunctions defined over the finite chain Ln.
        Computes all the possible combinations of elements that fit in the representation matrix of the conjunctions from the
        previous row.

        Args:
            restrictions: A list of integers, representing the restrictions given by the previous row.
            r: An integer, representing the recursive step.

        Returns:
            An integer, representing the partial operators defined over the finite chain up to the row r.
        """

        if r == 1:
            return restrictions[0] + 1
        else:
            value = 0
            for limits in DiscreteCommutativeConjunctionsRecursiveCounter.__generate_restrictions(upper_bounds=restrictions, max_size=r-1):
                xr = restrictions[len(restrictions)-1]
                ir1 = limits[len(limits)-1]

                new_limit = limits[0:(len(restrictions)-1)]
                value += (xr-ir1+1)*DiscreteCommutativeConjunctionsRecursiveCounter.__commutative_conjunction_counter(restrictions=new_limit, r=r-1)
            return value

    @staticmethod
    def __generate_restrictions(upper_bounds: List[int], max_size: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
        """
        Generates all possible vectors of size n whose entries are increasing and each value is less than or equal to the
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
                yield from DiscreteCommutativeConjunctionsRecursiveCounter.__generate_restrictions(upper_bounds=upper_bounds, max_size=max_size,
                                                                                                   recursion_depth=recursion_depth + 1,
                                                                                                   restrictions=temp_restrictions)
        elif 0 < recursion_depth < max_size:
            for x in range(restrictions[recursion_depth - 1], upper_bounds[recursion_depth] + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteCommutativeConjunctionsRecursiveCounter.__generate_restrictions(upper_bounds=upper_bounds, max_size=max_size,
                                                                                                   recursion_depth=recursion_depth + 1,
                                                                                                   restrictions=temp_restrictions)
        else:
            yield restrictions

    @staticmethod
    def __generate_initial_restrictions(n: int, recursion_depth: int = 0, restrictions: List[int] = None) -> Generator[List[int], None, None]:
        """
        Generates all possible vectors of size n whose entries are increasing and each value is less than or equal to n, that will
        be used as initial seed of the recursive counter.

        Args:
            n: An integer, representing the dimension of the finite chain.
            recursion_depth: An integer, representing the position of the vector that is being generated.
            restrictions: A list of integers, representing the temporal vector to be generated.

        Returns:
            A generator of increasing vectors whose entries are bounded above by n and its length is n-1.
        """
        if restrictions is None:
            restrictions = []

        if recursion_depth == 0:
            for x in range(0, n + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteCommutativeConjunctionsRecursiveCounter.__generate_initial_restrictions(n=n, recursion_depth=recursion_depth + 1,
                                                                                                           restrictions=temp_restrictions)
        elif 0 < recursion_depth < n - 1:
            for x in range(restrictions[recursion_depth - 1], n + 1):
                temp_restrictions = restrictions.copy()
                temp_restrictions.append(x)
                yield from DiscreteCommutativeConjunctionsRecursiveCounter.__generate_initial_restrictions(n=n, recursion_depth=recursion_depth + 1,
                                                                                                           restrictions=temp_restrictions)
        else:
            yield restrictions
