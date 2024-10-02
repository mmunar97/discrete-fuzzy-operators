import warnings
import numpy
from math import isclose
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_conjunction import \
    FuzzyUnitConjunction


class FuzzyUnitTnorm(FuzzyUnitConjunction):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a fuzzy tnorm T: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitTnorm, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_tnorm():
            warnings.warn("With the input arguments, the generated operator is not a tnorm since "
                          "it is not a fuzzy conjunction, or is not commutative or is not associative or it does"
                          "not satisfy the boundary conditions.")

    def is_tnorm(self) -> bool:
        """
        Checks if the operator is a tnorm; that is,
            - It is commutative
            - It is associative
            - It is monotone increasing with respect to each variable
            - It satisfy the boundary conditions
        """
        return self.is_fuzzy_conjunction() and self.is_commutative() and self.is_associative() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self, scatter_grid_x: int = 50) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a tnorm; that is, if T(x,1)=x for all x in [0,1];
        in a grid of a specified size.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
        """

        x = numpy.linspace(0, 1, scatter_grid_x)

        for x_idx, x_val in enumerate(x):
            if not isclose(self.evaluate_operator(x_val, 1), x_val):
                return False
        return True
