import warnings
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_operator import \
    FuzzyUnitAggregationBinaryOperator


class FuzzyUnitDisjunction(FuzzyUnitAggregationBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a fuzzy disjunction D: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitDisjunction, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_disjunction():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy disjunction since "
                          "it is not increasing and/or satisfies the boundary conditions.")

    def is_fuzzy_disjunction(self) -> bool:
        """
        Checks if the operator is a fuzzy disjunction; that is, if it is an aggregation function and satisfies
        the boundary conditions.
        """
        return self.is_fuzzy_aggregation() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy disjunction; that is, if D(1,0)=D(0,1)=1.
        """
        if self.evaluate_operator(1, 0) == 1 and self.evaluate_operator(0, 1) == 1:
            return True
        return False