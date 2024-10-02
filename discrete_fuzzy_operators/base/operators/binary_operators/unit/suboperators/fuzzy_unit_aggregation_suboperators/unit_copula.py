import warnings
import numpy
from numpy import isclose
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_conjunction import \
    FuzzyUnitConjunction


class FuzzyUnitCopula(FuzzyUnitConjunction):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a copula C: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitCopula, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_copula():
            warnings.warn("With the input arguments, the generated operator is not a copula since it does not fulfill "
                          "the conditions in the definition.")

    def is_copula(self, scatter_grid_x: int = 50, scatter_grid_y: int = 50) -> bool:

        """
        Checks if the operator is a copula; that is,
            - It fulfills C(x,0)=C(0,y) for all x,y in [0,1]
            - It fulfills C(x,1)=x for all x in [0,1]
            - C(1,y) = y for all y in [0,1]
            - C(x2,y2) - C(x2,y1) - C(x1,y2) + C(x1,y1) >= 0 for all x1,x2,y1,y2 in [0,1] such that x1 <= x2, y1 <= y2
        in a grid of a specified size.

         Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
            scatter_grid_y: An integer, representing the number of points to consider in the Y grid.
        """
        x1 = numpy.linspace(0, 1, scatter_grid_x)
        y1 = numpy.linspace(0, 1, scatter_grid_y)
        x2 = numpy.linspace(0, 1, scatter_grid_x)
        y2 = numpy.linspace(0, 1, scatter_grid_y)

        for x1_idx, x1_val in enumerate(x1):
            if not isclose(self.evaluate_operator(x1_val, 1), x1_val):
                return False
                print("Cond2")
            for y1_idx, y1_val in enumerate(y1):
                if not isclose(self.evaluate_operator(x1_val, 0), self.evaluate_operator(0, y1_val)):
                    print("Cond1")
                    return False
                if not isclose(self.evaluate_operator(1, y1_val), y1_val):
                    print("Cond3")
                    return False
                for x2_idx, x2_val in enumerate(x2):
                    for y2_idx, y2_val in enumerate(y2):
                        if x1_val <= x2_val and y1_val <= y2_val:
                            if not (self.evaluate_operator(x2_val, y2_val)-self.evaluate_operator(x2_val,y1_val)-self.evaluate_operator(x1_val,y2_val)+self.evaluate_operator(x1_val,y1_val)>0\
                                    or isclose(self.evaluate_operator(x2_val, y2_val)-self.evaluate_operator(x2_val,y1_val)-self.evaluate_operator(x1_val,y2_val)+self.evaluate_operator(x1_val,y1_val),0)):
                                return False

        return True
