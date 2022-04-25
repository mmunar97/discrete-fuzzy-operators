from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
import decimal


class DiscreteAggregationFunctionsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete aggregation functions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteAggregationFunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self, **kwargs) -> int:
        """
        Counts the number of discrete aggregation functions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of discrete conjunctions.
        """
        if self.n == 1:
            return 4
        elif self.n == 2:
            return 135
        else:
            count = self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n) - 2 * self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n - 1) + \
                    self.plane_partition_counter(a=self.n + 1, b=self.n + 1, c=self.n - 2)
            return int(count.to_integral(rounding=decimal.ROUND_HALF_DOWN))

    @staticmethod
    def plane_partition_counter(a: int, b: int, c: int) -> decimal.Decimal:
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
        value = decimal.Decimal(1)
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                for k in range(1, c + 1):
                    value *= decimal.Decimal(i + j + k - 1) / decimal.Decimal(i + j + k - 2)

        return value
