from discrete_fuzzy_operators.base.decision_making.two_tuple.two_tuple import TwoTuple
from discrete_fuzzy_operators.base.exceptions.decision_making.two_tuple.two_tuple_bad_operation import TwoTupleBadOperation
from typing import List


class LinguisticTermSet:

    def __init__(self, term_set: List[int]):
        self.term_set = term_set

    def delta(self, value) -> TwoTuple:
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
    def inverse_delta(two_tuple: TwoTuple) -> float:
        """
        Computes the inverse value of the delta function, defined as the sum of the index of the linguistic label and
        the symbolic translation.

        Returns:
            A float value, representing the value of the inverse delta function.
        """
        return two_tuple.label+two_tuple.alpha
