from discrete_fuzzy_operators.counters.aggregation_functions.discrete_aggregation_function_counter import DiscreteAggregationFunctionsCounter
from math import comb, factorial


class DiscreteIdentityPrincipleConjunctionsCounter(DiscreteAggregationFunctionsCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete conjunctions which satisfy the
        identity principle for conjunctions over the finite chain Ln; that is, the conjunctions
        that C(x,n-x) = 0.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteIdentityPrincipleConjunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete conjunctions which satisfy (IP) defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set.
        """
        return self.__staircase_plane_partition(r=self.n, l=self.n+1, k=1, m=self.n+1)-self.__staircase_plane_partition(r=self.n, l=self.n+1, k=1, m=self.n)

    @staticmethod
    def __staircase_plane_partition(r: int, l: int, k: int, m: int) -> int:
        """
        Computes the number of staircase plane partition with r rows, step k, initial length l and maximum value m.

        Args:
            r: The number of rows of the plane partition.
            l: The initial length of the first row.
            k: The decrementing step of the length of each row.
            m: The maximum value of the plane partition.

        Returns:
            An integer, representing the number of staircase plane partitions.
        """
        x1 = 1
        for i in range(1, r+1):
            x1 *= factorial(m+l-k*i-1)/factorial(m+i-2)

        x2 = 1
        for i in range(1, r+1):
            up_fact = DiscreteIdentityPrincipleConjunctionsCounter.__upper_factorial(m+(l-k*i)/(k+1), i-1)
            x2 *= up_fact/factorial(r+l-i*(k+1))

        x3 = (k+1)**comb(r, 2)

        x4 = 1
        for i in range(2, r):
            x4 *= i**(r-i)

        return round(x1*x2*x3*x4)

    @staticmethod
    def __upper_factorial(z: float, i: int) -> float:
        """
        Computes the upper factorial of a positive real number with respect to a positive integer.
        The upper factorial is defined as <z>_i = Prod_{j=0}^{i-1} (z-j).

        Args:
            z: A positive real number.
            i: A positive integer.

        Returns:
            The upper factorial of z with respect to i.
        """
        fact = 1
        for k in range(0, i):
            fact *= (z+k)
        return fact
