import plotly.graph_objects as go

from decimal import Decimal

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_implication_operator import \
    DiscreteFuzzyImplicationOperator
from discrete_fuzzy_operators.base.operators.binary_operators.unit.fuzzy_unit_binary_operator import \
    FuzzyUnitBinaryOperator

from typing import Callable, Tuple


class FuzzyUnitImplicationOperator(FuzzyUnitBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None):
        """
        Initializes the object that represents a binary fuzzy implication I: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression:
        """
        super(FuzzyUnitImplicationOperator, self).__init__(operator_expression)

    def get_upper_discretized_operator(self, n: int) -> DiscreteFuzzyImplicationOperator:
        """
        Computes the upper discretization of an implication, defined as Ceil(n*I(x/n,y/n)), and represents it as a
        DiscreteFuzzyImplicationOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A DiscreteFuzzyImplicationOperator object, representing the discrete implication.
        """
        return DiscreteFuzzyImplicationOperator(n=n, operator_matrix=super(FuzzyUnitImplicationOperator,
                                                                           self).get_upper_discretized_operator(n).operator_matrix)

    def get_lower_discretized_operator(self, n: int) -> DiscreteFuzzyImplicationOperator:
        """
        Computes the lower discretization of an implication, defined as Floor(n*I(x/n,y/n)), and represents it as a
        DiscreteFuzzyImplicationOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A DiscreteFuzzyImplicationOperator object, representing the discrete implication.
        """
        return DiscreteFuzzyImplicationOperator(n=n, operator_matrix=super(FuzzyUnitImplicationOperator,
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
