import numpy
import plotly.express as plot_express
import plotly.graph_objects as go
from typing import Callable, List, Tuple




class FuzzyUnitUnaryOperator:
    def __init__(self, operator_expression: Callable[[float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the base object representing the operator defined in the unit interval from its analytical
        expression. Since the class works with numbers between 0 and 1, in order to prevent rounding errors the
        Decimal class is used.

        Args:
            operator_expression: A function, representing the analytical expression.
        """
        self.check_properties_in_load = check_properties_in_load
        if operator_expression is None:
            raise Exception("In order to define a unary operator, its analytical expression must be provided.")

        self.operator_expression = operator_expression

    def evaluate_operator(self, x: float) -> float:
        """
        Evaluates the operator in the given point.

        Args:
            x: A float expressed as Decimal, representing the given point.

        Returns:
            A float, representing the value of the function in the given point.
        """
        if not 0 <= x <= 1:
            raise Exception("To evaluate a binary operator defined in the unit interval, the arguments must be between "
                            "0 and 1.")
        return self.operator_expression(x)

    # region Plot of the operator
    def plot_operator(self, scatter_grid_x: int = 50, figure_size: Tuple[int, int] = (700, 700)):
        """
        Plots the operator.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
            figure_size: A tuple, representing the size of the figure as WIDTHxHEIGHT.
        """
        x = numpy.linspace(0, 1, scatter_grid_x)
        y = numpy.zeros(len(x))

        for x_idx, x_val in enumerate(x):
            y[x_idx] = self.evaluate_operator(x_val)

        figure = plot_express.line(x=x, y=y)
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1])
        figure.show()

    def is_decreasing(self, scatter_grid_x: int = 50) -> bool:
        """
        Checks if the operator is monotone decreasing in a grid of a specified size.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
        """

        x = numpy.linspace(0, 1, scatter_grid_x)

        for i in range(0,scatter_grid_x-1):
            if not self.evaluate_operator(x[i+1]) <= self.evaluate_operator(x[i]):
                return False
        return True

    def is_increasing(self, scatter_grid_x: int = 50) -> bool:
        """
        Checks if the operator is monotone increasing in a grid of a specified size.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
        """

        x = numpy.linspace(0, 1, scatter_grid_x)

        for i in range(0,scatter_grid_x-1):
            if not self.evaluate_operator(x[i+1]) >= self.evaluate_operator(x[i]):
                return False
        return True