class DiscreteOperatorCounter:

    def __init__(self, n: int):
        """
        Initializes the object that counts the number of discrte operators defined over the finite chain Ln.

        Args:
            n: An integer, representing the size of the finite chain.
        """
        self.n = n

    def count_operators(self, **kwargs) -> int:
        """
        Counts the number of discrete operators defined over the finite chain Ln.

        Returns:
            An integer, representing the cardinality of the set of that discrete operators.
        """
        pass
