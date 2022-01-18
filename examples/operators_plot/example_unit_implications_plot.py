from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_implication_operator import \
    FuzzyUnitImplicationOperator


def example_implication1(x: float, y: float) -> float:
    """
    Example of continuous implication whose discretizations are not smooth.
    """
    if x <= y:
        return 1
    elif x-1/2 <= y <= x:
        return 1+2*y-2*x
    else:
        return 0


def example_implication2(x: float, y: float) -> float:
    """
    Example of non-continuous implication whose lower discretization is smooth but its upper discretization is not.
    """
    if x == 0 or y == 1:
        return 1
    if 0 < x <= 1/3:
        if 0 <= y < 1/3:
            return 2/3
        elif 1/3 <= y < 2/3:
            return 2/3
        elif 2/3 <= y < 1:
            return 23/30
    if 1/3 < x <= 2/3:
        if 0 <= y < 1/3:
            return 1/3
        elif 1/3 <= y < 2/3:
            return 1/3
        elif 2/3 <= y < 1:
            return 43/60
    if 2/3 < x <= 1:
        if 0 <= y < 1/3:
            return 0
        elif 1/3 <= y < 2/3:
            return 1/3
        elif 2/3 <= y < 1:
            return 7/10


if __name__ == "__main__":

    unit_operator = FuzzyUnitImplicationOperator(operator_expression=example_implication2)
    # unit_operator = UnitImplicationExamples.get_unit_implication(UnitImplicationExamples.REICHENBACH)
    unit_operator.plot_operator()
    unit_operator.get_upper_discretized_operator(n=3).plot_operator()
    unit_operator.get_lower_discretized_operator(n=3).plot_operator()
