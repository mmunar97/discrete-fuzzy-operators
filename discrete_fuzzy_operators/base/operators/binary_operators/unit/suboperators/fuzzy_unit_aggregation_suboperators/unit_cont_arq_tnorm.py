import warnings
import numpy
from math import isclose
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_tnorm import \
    FuzzyUnitTnorm
from discrete_fuzzy_operators.base.numeric_comparator.numeric_comparator import NumericComparator


class FuzzyUnitContArqTnorm(FuzzyUnitTnorm):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 t: Callable[[float], float] = None,
                 t_inv: Callable[[float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a continuous, arquimedean fuzzy tnorm T: [0,1]x[0,1] -> [0,1] from its analytical
        expression or its additive generator and its inverse.

        Args:
            operator_expression: A function, representing the analytical expression.
            t: additive generator of the continuous, Arquimedean t-norm.
            t_inv: inverse of t.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """

        if (operator_expression is None) and (t is None or t_inv is None):
            raise Exception("To initialise a continuous, Arquimedean t-norm it is necessary to provide its expression "
                            "or its additive generator and the corresponding inverse.")

        self.check_properties_in_load = check_properties_in_load
        if operator_expression is not None:
            super(FuzzyUnitContArqTnorm, self).__init__(operator_expression=operator_expression,
                                                        check_properties_in_load=check_properties_in_load)
        if t is not None and t_inv is not None:
            super(FuzzyUnitContArqTnorm, self).__init__(operator_expression=lambda x, y: t_inv(min(t(0),t(x)+t(y))),
                                                        check_properties_in_load=check_properties_in_load)

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
            if not NumericComparator.compare_equal(self.evaluate_operator(x_val, 1), x_val):
                return False
        return True
