from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter


class DiscreteAggregationFunctionsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete aggregation functions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteAggregationFunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete aggregation functions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of discrete conjunctions.
        """
        return self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n) - 2 * self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n - 1) + \
               self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n - 2)

    @staticmethod
    def plane_partition_counter(a: int, b: int, c: int) -> int:
        """
        Computes the number of (a,b,c)-cubic plane partitions, given by the formula:
                    prod_{i=1}^a prod_{j=1}^b prod_{k=1}^c (i+j+k-1)/(i+j+k-2)

        Args:
            a: An integer, representing the number of rows of the plane partition.
            b: An integer, representing the number of columns of the plane partition.
            c: An integer, representing the upper bound of the elements of the plane partition.

        Returns:
            An integer, representing the cardinality of the set of (a,b,c)-cubic plane partitions.
        """
        value = 1
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                for k in range(1, c + 1):
                    value *= (i + j + k - 1) / (i + j + k - 2)
        value = round(value)
        return int(value)
