import warnings
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_operator import FuzzyUnitAggregationBinaryOperator
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_disjunction import \
    FuzzyUnitDisjunction
from discrete_fuzzy_operators.base.operators.unary_operators.unit.suboperators.fuzzy_negation_operator import FuzzyNegation


class FuzzyUnitConjunction(FuzzyUnitAggregationBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a fuzzy conjunction C: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitConjunction, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_conjunction():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy conjunction since "
                          "it is not increasing and/or satisfies the boundary conditions.")

    def is_fuzzy_conjunction(self) -> bool:
        """
        Checks if the operator is a fuzzy conjunction; that is, if it is an aggregation function and satisfies
        the boundary conditions.
        """
        return self.is_fuzzy_aggregation() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy conjunction; that is, if C(1,0)=C(0,1)=0.
        """
        if self.evaluate_operator(1, 0) == 0 and self.evaluate_operator(0, 1) == 0:
            return True
        return False
