import numpy


class NumericComparator:
    def __init__(self, rtol: float = 1e-15, atol: float = 0):
        self.rtol = rtol
        self.atol = atol

    @staticmethod
    def compare_equal(a: float, b: float) -> bool:
        rtol = NumericComparator().rtol
        atol = NumericComparator().atol
        return abs(a - b) <= max(rtol * max(abs(a), abs(b)), atol)

    @staticmethod
    def compare_less_equal(a: float, b: float) -> bool:
        return a <= b or NumericComparator.compare_equal(a, b)

    @staticmethod
    def compare_greater_equal(a: float, b: float) -> bool:
        return a >= b or NumericComparator.compare_equal(a, b)
