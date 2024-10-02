import plotly.graph_objects as go

from decimal import Decimal
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_implication_operator import \
    DiscreteImplicationOperator
from discrete_fuzzy_operators.base.operators.binary_operators.unit.fuzzy_unit_binary_operator import \
    FuzzyUnitBinaryOperator

from typing import Callable, Tuple


class FuzzyUnitImplicationOperator(FuzzyUnitBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a binary fuzzy implication I: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitImplicationOperator, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_implication():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy implication since it is "
                          "not decreasing/increasing and/or satisfies the boundary conditions.")

    def is_fuzzy_implication(self) -> bool:
        """
        Checks if the operator is a fuzzy implication; that is, if it is monotone decreasing with respect to the
        1st variable, increasing with respect to the 2nd variable and satisfies the boundary conditions.
        """
        return self.is_decreasing_x() and self.is_increasing_y() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy implication; that is, if I(1,0)=0 and
        I(1,1)=I(0,0)=1.
        """
        if self.evaluate_operator(1, 0) == 0 and self.evaluate_operator(0, 0) == 1 and self.evaluate_operator(1, 1) == 1:
            return True
        return False

    def get_upper_discretized_operator(self, n: int) -> DiscreteImplicationOperator:
        """
        Computes the upper discretization of an implication, defined as Ceil(n*I(x/n,y/n)), and represents it as a
        DiscreteFuzzyImplicationOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A DiscreteFuzzyImplicationOperator object, representing the discrete implication.
        """
        return DiscreteImplicationOperator(n=n, operator_matrix=super(FuzzyUnitImplicationOperator,
                                                                      self).get_upper_discretized_operator(n).operator_matrix)

    def get_lower_discretized_operator(self, n: int) -> DiscreteImplicationOperator:
        """
        Computes the lower discretization of an implication, defined as Floor(n*I(x/n,y/n)), and represents it as a
        DiscreteFuzzyImplicationOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A DiscreteFuzzyImplicationOperator object, representing the discrete implication.
        """
        return DiscreteImplicationOperator(n=n, operator_matrix=super(FuzzyUnitImplicationOperator,
                                                                      self).get_lower_discretized_operator(n).operator_matrix)

    # region Plot of the discretizations
    def plot_lower_discretization(self, n: int, figure_title: str = "Lower discretization of the implication",
                                  figure_size: Tuple[int, int] = (700, 700)):
        """
        Plots the lower discretization of the implication.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete implication is defined.
            figure_title: A string, representing the title of the figure.
            figure_size: A tuple, representing the size of the figure as WIDTHxHEIGHT.
        """
        self.get_lower_discretized_operator(n).plot_operator(figure_size=figure_size,
                                                             figure_title=figure_title)

    def plot_upper_discretization(self, n: int, figure_title: str = "Upper discretization of the implication",
                                  figure_size: Tuple[int, int] = (700, 700)):
        """
        Plots the lower discretization of the implication.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete implication is defined.
            figure_title: A string, representing the title of the figure.
            figure_size: A tuple, representing the size of the figure as WIDTHxHEIGHT.
        """
        self.get_upper_discretized_operator(n).plot_operator(figure_size=figure_size,
                                                             figure_title=figure_title)
    # endregion
