import numpy
import math
import warnings
from typing import Callable

from discrete_fuzzy_operators.base.operators.unary_operators.unit.fuzzy_unit_unary_operator import \
    FuzzyUnitUnaryOperator


class FuzzyNegation(FuzzyUnitUnaryOperator):
    def __init__(self,
                 operator_expression: Callable[[float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object representing the fuzzy negation from its analytical expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyNegation, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_negation():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy negation since it is "
                          "not decreasing and/or satisfies the boundary conditions.")

    # region Basic properties of negations
    def is_negation(self) -> bool:
        """
        Checks if the operator is a fuzzy negation; that is, if it is monotone decreasing and satisfies the
        boundary conditions.
        """
        return self.is_decreasing() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy negation; that is, if N(0)=1 and
        N(1)=0.
        """
        if self.evaluate_operator(0) == 1 and self.evaluate_operator(1) == 0:
            return True
        return False

    # endregion

    def is_strong(self, scatter_grid_x: int = 50) -> bool:
        """
        Checks if the fuzzy negation is strong; that is, N(N(x))=x for all x in [0,1], in a grid of a specified size.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
        """

        x = numpy.linspace(0, 1, scatter_grid_x)

        for x_idx, x_val in enumerate(x):
            if not math.isclose(self.evaluate_operator(self.evaluate_operator(x_val)), x_val):
                return False
        return True
