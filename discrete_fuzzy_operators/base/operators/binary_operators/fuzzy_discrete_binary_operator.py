import numpy
import plotly.graph_objects as go

from discrete_fuzzy_operators.base.exceptions.operator_bad_definition import FuzzyOperatorBadDefinition
from discrete_fuzzy_operators.base.exceptions.operator_image_invalid import FuzzyOperatorImageRangeException
from discrete_fuzzy_operators.base.exceptions.operator_size_exception import FuzzyOperatorSizeException

from typing import Callable, Tuple


class FuzzyDiscreteBinaryOperator:

    def __init__(self, n: int, operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the base object representing the operator from its matrix expression or its analytical expression.

        Args:
            n: An integer, representing the size of the finite chain.
            operator_matrix: A numpy array, representing the operator in its matrix expression.
            operator_expression: A function, representing the analytical expression.
        """
        if operator_matrix is None and operator_expression is None:
            raise FuzzyOperatorBadDefinition()

        self.n = n
        if operator_expression is not None:
            self.operator_expression = operator_expression

        if operator_matrix is not None:
            if not (len(operator_matrix.shape) == 2 and operator_matrix.shape[0] == operator_matrix.shape[1]):
                raise FuzzyOperatorSizeException()

            if not ((operator_matrix >= 0).all() and (operator_matrix <= n).all()):
                raise FuzzyOperatorImageRangeException()
            self.operator_matrix = operator_matrix
        else:
            self.operator_matrix = self.generate_operator_matrix()

    def generate_operator_matrix(self):
        """
        Generates the matrix expression from the analytic function.

        Returns:
            A numpy array, representing the matrix expression of the operator.
        """
        matrix = numpy.zeros((self.n+1, self.n+1), dtype=int)
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                matrix[y, x] = self.operator_expression(x, y, self.n)
        return matrix

    def evaluate_operator(self, x: int, y: int) -> int:
        """
        Evaluates the operator in the given point.

        Args:
            x: An integer, representing the first coordinate of the point.
            y: An integer, representing the second coordinate of the point.

        Returns:
            An integer, representing the value of the function in the given point.
        """
        if self.operator_matrix is not None:
            # Warning: The matrix is evaluated in the reversed point since is defined increasingly, where columns
            # represent X coordinates and rows represent Y coordinates.
            return self.operator_matrix[y, x]
        elif self.operator_expression is not None:
            return self.operator_expression(x, y, self.n)

    def plot_operator(self, figure_size: Tuple[int, int], figure_title: str = "Discrete operator"):
        """
        Plots the discrete operator.

        Args:
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
            figure_title: A string, representing the label of the operator.
        """
        x_disc = []
        y_disc = []
        operator_values = []
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                x_disc.append(x)
                y_disc.append(y)
                operator_values.append(self.operator_matrix[y, x])

        discrete_scatter = go.Scatter3d(
            x=x_disc,
            y=y_disc,
            z=operator_values,
            mode="markers",
            name=figure_title,
            marker=dict(size=12, color=['rgb(0,0,0)'], opacity=0.9)
        )

        figure = go.Figure(data=[discrete_scatter, self.__generate_cube_contour()])
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1],
                             legend=dict(yanchor="bottom", xanchor="center"))
        figure.show()

    def __generate_cube_contour(self) -> go.Scatter3d:
        """
        Generates the contour of the cube which embeds the plot inside.

        Returns:
            A Scatter3d object, representing the shape of the cube.
        """
        n = self.n
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

        return lower_scatter