from discrete_fuzzy_operators.base.exceptions.decision_making.two_tuple_bad_operation import TwoTupleBadOperation
from functools import total_ordering
from typing import List


class LinguisticTermSet:

    def __init__(self, term_set: List[int]):
        self.term_set = term_set

    def delta(self, value) -> "TwoTuple":
        """
        Computes the image of the delta function, defined as Delta(beta) = (s_i, alpha), where i=round(beta) and
        alpha = beta-i.

        Args:
            value: A float value  between 0 and n, where n+1 is the length of the linguistic term set.

        Returns:
            A two-tuple object.
        """
        if not 0 <= value <= len(self.term_set) - 1:
            raise TwoTupleBadOperation()

        i = round(value)
        alpha = value - i

        return TwoTuple(label_index=i, alpha=round(alpha, 4), context=self)

    @staticmethod
    def inverse_delta(two_tuple: "TwoTuple") -> float:
        """
        Computes the inverse value of the delta function, defined as the sum of the index of the linguistic label and
        the symbolic translation.

        Returns:
            A float value, representing the value of the inverse delta function.
        """
        return two_tuple.label+two_tuple.alpha


@total_ordering
class TwoTuple:
    """
    Object that stores all the information of the 2-tuple.

    References:
        Herrera, F., & Martinez, L. (2000). A 2-tuple fuzzy linguistic representation model for computing with words.
        IEEE Transactions on Fuzzy Systems, 8(6), 746–752.
        https://doi.org/10.1109/91.890332
    """

    def __init__(self, label_index: int, alpha: float, context: "LinguisticTermSet"):
        """
        Initializes the object that stores all the information of the 2-tuple.

        Args:
            label_index: An integer, representing the position of the linguistic label in the linguistic term set.
            alpha: A float, representing the symbolic translation.
            context: A list of integers, representing the linguistic term set.
        """
        self.label = label_index
        self.alpha = alpha
        self.context = context

    # region Representation and ordering of 2-tuples.
    def __repr__(self) -> str:
        """
        Represents the 2-tuple as a string.
        """
        return f"({self.label}, {self.alpha})"

    def __lt__(self, other: "TwoTuple") -> bool:
        """
        Checks if one 2-tuple is less than another, using the lexicographic order.

        Args:
            other: Another 2-tuple object.

        Returns:
            A boolean, indicating if one two tuple is less than the other.
        """
        if self.label < other.label:
            return True
        elif self.label > other.label:
            return False
        elif self.label == other.label:
            if self.alpha == other.alpha:
                return False
            elif self.alpha < other.alpha:
                return True
            elif self.alpha > other.alpha:
                return False

    def __eq__(self, other: "TwoTuple"):
        """
        Checks if one 2-tuple is equal to another. Two 2-tuples are equal if, and only if, the linguistic index and
        the symbolic translation are equal.

        Args:
            other: Another 2-tuple object.

        Returns:
            A boolean, indicating if one two tuple is equal to the other.
        """
        if self.label == other.label and self.alpha == other.alpha:
            return True
        return False

    def __gt__(self, other):
        """
        Checks if one 2-tuple is greater than another, using the lexicographic order.

        Args:
            other: Another 2-tuple object.

        Returns:
            A boolean, indicating if one two tuple is less than the other.
        """
        if self.label < other.label:
            return False
        elif self.label > other.label:
            return True
        elif self.label == other.label:
            if self.alpha == other.alpha:
                return False
            elif self.alpha < other.alpha:
                return False
            elif self.alpha > other.alpha:
                return True
    # endregion
