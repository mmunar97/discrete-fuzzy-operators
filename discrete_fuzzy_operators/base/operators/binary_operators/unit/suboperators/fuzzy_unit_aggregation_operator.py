from discrete_fuzzy_operators.base.numeric_comparator.numeric_comparator import NumericComparator
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.unit.fuzzy_unit_binary_operator import \
    FuzzyUnitBinaryOperator

from typing import Callable, Tuple


class FuzzyUnitAggregationBinaryOperator(FuzzyUnitBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a binary aggregation function A: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """

        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitAggregationBinaryOperator, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_aggregation():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy aggregation function since "
                          "it is not increasing and/or satisfies the boundary conditions.")

    def is_fuzzy_aggregation(self) -> bool:
        """
        Checks if the operator is a fuzzy aggregation function; that is, if it is monotone increasing with respect each
        variable and satisfies the boundary conditions A(0,0)=0 and A(1,1)=1.
        """
        return self.is_increasing_x() and self.is_increasing_y() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy aggregation function; that is, if A(0,0)=0 and
        A(1,1)=1.
        """
        if NumericComparator.compare_equal(self.evaluate_operator(0, 0),0) and NumericComparator.compare_equal(self.evaluate_operator(1, 1),1):
            return True
        return False


