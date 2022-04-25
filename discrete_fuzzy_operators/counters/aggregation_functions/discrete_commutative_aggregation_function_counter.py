from discrete_fuzzy_operators.base.generators.discrete_operator_counter import DiscreteOperatorCounter
import decimal


class DiscreteCommutativeAggregationFunctionsCounter(DiscreteOperatorCounter):

    def __init__(self, n: int):
        """
        Initializes the object that counts all possible discrete commutative aggregation functions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteCommutativeAggregationFunctionsCounter, self).__init__(n)
        self.n = n

    def count_operators(self) -> int:
        """
        Counts the number of discrete commutative aggregation functions defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of commutative discrete conjunctions.
        """
        count = self.symmetric_plane_partition_counter(a=self.n + 1, c=self.n) - 2 * self.symmetric_plane_partition_counter(a=self.n + 1, c=self.n - 1) + \
                self.symmetric_plane_partition_counter(a=self.n + 1, c=self.n - 2)

        return int(count.to_integral(rounding=decimal.ROUND_HALF_DOWN))

    @staticmethod
    def symmetric_plane_partition_counter(a: int, c: int) -> decimal.Decimal:
        """
        Computes the number of symmetric (a,a,c)-cubic plane partitions, given by the formula:
                    prod_{i=1}^a (2*i+c-1)/(2*i-1) (prod_{j=i+1}^a ((i+j+c-1)/(i+j-1)))

        Args:
            a: An integer, representing the number of rows and columns of the plane partition.
            c: An integer, representing the upper bound of the elements of the plane partition.

        Returns:
            An integer, representing the cardinality of the set of symmetric (a,a,c)-cubic plane partitions.
        """
        value = decimal.Decimal(1)
        for i in range(1, a + 1):
            temp_value1 = decimal.Decimal(2 * i + c - 1) / decimal.Decimal(2 * i - 1)
            temp_value2 = decimal.Decimal(1)
            for j in range(i + 1, a + 1):
                temp_value2 *= decimal.Decimal(i + j + c - 1) / decimal.Decimal(i + j - 1)
            value *= temp_value1 * temp_value2
        return value
