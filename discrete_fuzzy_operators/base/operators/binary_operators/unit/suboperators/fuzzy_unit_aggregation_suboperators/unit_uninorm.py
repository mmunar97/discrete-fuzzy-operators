import warnings
import numpy
from math import isclose
from discrete_fuzzy_operators.base.numeric_comparator.numeric_comparator import NumericComparator
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_operator import \
    FuzzyUnitAggregationBinaryOperator


class FuzzyUnitUninorm(FuzzyUnitAggregationBinaryOperator):

    def __init__(self, e: float, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a fuzzy uninorm U: [0,1]x[0,1] -> [0,1] from its analytical
        expression and neutral element

        Args:
            operator_expression: A function, representing the analytical expression.
            e: A float, representing the neutral element of the uninorm.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        self.e = e
        super(FuzzyUnitUninorm, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_uninorm():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy uninorm since "
                          "it is not increasing, associative, commutative and/or satisfies the boundary conditions.")

    def is_fuzzy_uninorm(self) -> bool:
        """
        Checks if the operator is a fuzzy conjunction; that is, if it is increasing with respect to each variable,
        commutative, associative and satisfies the boundary conditions.
        """
        return (self.is_decreasing_x() and self.is_decreasing_y() and self.is_commutative() and self.is_associative()
                and self.verifies_boundary_conditions())

    def verifies_boundary_conditions(self, scatter_grid_x: int = 50) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a uninorm with neutral element e; that is, if
        U(x,e)=x for all x in [0,1]; in a grid of a specified size.
        """
        x = numpy.linspace(0, 1, scatter_grid_x)
        for x_idx, x_val in enumerate(x):
            if NumericComparator.compare_equal(self.evaluate_operator(x_val, self.e), x):
                return True
            return False
