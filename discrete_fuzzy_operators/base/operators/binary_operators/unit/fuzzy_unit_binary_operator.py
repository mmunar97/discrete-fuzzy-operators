import numpy
import plotly.graph_objects as go

from decimal import Decimal
from math import ceil, floor
from typing import Callable, List, Tuple

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import \
    DiscreteBinaryOperator


class FuzzyUnitBinaryOperator:

    def __init__(self, operator_expression: Callable[[float, float], float] = None):
        """
        Initializes the base object representing the operator defined in the unit interval from its analytical
        expression. Since the class works with numbers between 0 and 1, in order to prevent rounding errors the
        Decimal class is used.

        Args:
            operator_expression: A function, representing the analytical expression.
        """
        if operator_expression is None:
            raise Exception("In order to define a binary operator, its analytical expression must be provided.")

        self.operator_expression = operator_expression

    def evaluate_operator(self, x: float, y: float) -> float:
        """
        Evaluates the operator in the given point.

        Args:
            x: A float expressed as Decimal, representing the first coordinate of the point.
            y: A float expressed as Decimal, representing the second coordinate of the point.

        Returns:
            A float, representing the value of the function in the given point.
        """
        if not 0 <= x <= 1 and 0 <= y <= 1:
            raise Exception("To evaluate a binary operator defined in the unit interval, the arguments must be between "
                            "0 and 1.")
        return self.operator_expression(x, y)

    # region Discretization
    def get_upper_discretized_operator(self, n: int) -> DiscreteBinaryOperator:
        """
        Computes the upper discretization of a binary operator, defined as Ceil(n*F(x/n,y/n)), and represents it as a
        FuzzyDiscreteBinaryOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A FuzzyDiscreteBinaryOperator object, representing the discrete operator.
        """
        operator_matrix = numpy.zeros((n+1, n+1), dtype=int)
        for x in range(0, n + 1):
            for y in range(0, n + 1):
                if x == 2 and y == 1:
                    a = 2
                operator_matrix[y, x] = ceil(round(n*self.evaluate_operator(x/n, y/n), 5))

        return DiscreteBinaryOperator(n=n, operator_matrix=operator_matrix)

    def get_lower_discretized_operator(self, n: int) -> DiscreteBinaryOperator:
        """
        Computes the upper discretization of a binary operator, defined as Ceil(n*F(x/n,y/n)), and represents it as a
        FuzzyDiscreteBinaryOperator object.

        Args:
            n: An integer, representing the dimension of the finite chain where the discrete operator is defined.

        Returns:
            A FuzzyDiscreteBinaryOperator object, representing the discrete operator.
        """
        operator_matrix = numpy.zeros((n + 1, n + 1), dtype=int)
        for x in range(0, n + 1):
            for y in range(0, n + 1):
                operator_matrix[y, x] = floor(round(n*self.evaluate_operator(x/n, y/n), 5))

        return DiscreteBinaryOperator(n=n, operator_matrix=operator_matrix)
    # endregion

    # region Plot of the operators
    def plot_operator(self, scatter_grid_x: int = 50, scatter_grid_y: int = 50,
                      figure_size: Tuple[int, int] = (700, 700)):
        """
        Plots the operator.

        Args:
            scatter_grid_x: An integer, representing the number of points to consider in the X grid.
            scatter_grid_y: An integer, representing the number of points to consider in the Y grid.
            figure_size: A tuple, representing the size of the figure as WIDTHxHEIGHT.
        """
        x = numpy.linspace(0, 1, scatter_grid_x)
        y = numpy.linspace(0, 1, scatter_grid_y)
        z = numpy.zeros((len(x), len(y)))

        for x_idx, x_val in enumerate(x):
            for y_idx, y_val in enumerate(y):
                z[y_idx, x_idx] = self.evaluate_operator(x_val, y_val)

        figure = go.Figure(data=[go.Surface(x=x, y=y, z=z, cmin=0, cmax=1, showscale=False)]+self.generate_unit_cube_contour(draw_diagonal=False))
        figure.update_layout(
            autosize=True,
            width=figure_size[0],
            height=figure_size[1],
            scene=dict(
                xaxis_title=r'X',
                xaxis=dict(nticks=3, range=[0, 1]),
                yaxis_title=r'Y',
                yaxis=dict(nticks=3, range=[0, 1]),
                zaxis_title=r'Z',
                zaxis=dict(nticks=3, range=[-0.1, 1]),
            )
        )

        figure.show()

    @staticmethod
    def generate_unit_cube_contour(draw_diagonal: bool) -> List[go.Scatter3d]:
        """
        Generates the contour of the unit cube which embeds the plot inside.

        Args:
            draw_diagonal: A boolean, indicating if the main diagonal of the cube has to be drawn; that is, if the
                           line which joins the point (1, 1, 1) with (0, 0, 0).

        Returns:
            A Scatter3d object, representing the shape of the cube.
        """
        coordinates_x = [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
        coordinates_y = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
        coordinates_z = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]

        lower_scatter = go.Scatter3d(
            x=coordinates_x,
            y=coordinates_y,
            z=coordinates_z,
            name="Contour",
            line=dict(color="red", width=3),
            marker=dict(size=0, color=['rgb(0,0,0)'], opacity=0)
        )

        if draw_diagonal:
            coordinates_diagonal_x = [0, 1]
            coordinates_diagonal_y = [0, 1]
            coordinates_diagonal_z = [0, 1]

            diagonal_scatter = go.Scatter3d(
                x=coordinates_diagonal_x,
                y=coordinates_diagonal_y,
                z=coordinates_diagonal_z,
                name="Diagonal",
                line=dict(color="red", width=5),
                marker=dict(size=0, color=['rgb(0,0,0)'], opacity=0)
            )

            return [lower_scatter, diagonal_scatter]

        return [lower_scatter]

    @staticmethod
    def generate_discrete_cube_contour(n: int, draw_diagonal: bool) -> List[go.Scatter3d]:
        """
        Generates the contour of the discrete cube which embeds the plot inside.

        Args:
            n: An integer, representing the dimension of the cube.
            draw_diagonal: A boolean, indicating if the main diagonal of the cube has to be drawn; that is, if the
                           line which joins the point (n, n, n) with (0, 0, 0).

        Returns:
            A Scatter3d object, representing the shape of the cube.
        """
        coordinates_x = [0, n, n, 0, 0, 0, n, n, n, n, n, n, 0, 0, 0, 0]
        coordinates_y = [0, 0, n, n, 0, 0, 0, 0, 0, n, n, n, n, n, n, 0]
        coordinates_z = [0, 0, 0, 0, 0, n, n, 0, n, n, 0, n, n, 0, n, n]

        lower_scatter = go.Scatter3d(
            x=coordinates_x,
            y=coordinates_y,
            z=coordinates_z,
            name="Contour",
            line=dict(color="red", width=3),
            marker=dict(size=0, color=['rgb(0,0,0)'], opacity=0)
        )

        if draw_diagonal:
            coordinates_diagonal_x = [0, n]
            coordinates_diagonal_y = [0, n]
            coordinates_diagonal_z = [0, n]

            diagonal_scatter = go.Scatter3d(
                x=coordinates_diagonal_x,
                y=coordinates_diagonal_y,
                z=coordinates_diagonal_z,
                name="Diagonal",
                line=dict(color="red", width=5),
                marker=dict(size=0, color=['rgb(0,0,0)'], opacity=0)
            )

            return [lower_scatter, diagonal_scatter]

        return [lower_scatter]
    # endregion
