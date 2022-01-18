from typing import Generator


class DiscreteOperatorGenerator:

    def __init__(self, n: int):
        self.n = n

    def generate_operators(self) -> Generator:
        """
        Generates all possible operators defined over the finite chain Ln.

        Returns:
            A Generator object, representing the object that recursively generates all possible operators.
        """
        pass
