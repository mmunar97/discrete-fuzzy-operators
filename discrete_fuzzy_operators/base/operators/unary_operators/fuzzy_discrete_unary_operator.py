import numpy
import plotly.express as plot_express
import warnings

from discrete_fuzzy_operators.base.exceptions.operators.operator_bad_definition import FuzzyOperatorBadDefinition
from discrete_fuzzy_operators.base.exceptions.operators.operator_range_invalid import FuzzyOperatorImageRangeException
from discrete_fuzzy_operators.base.exceptions.operators.operator_size_exception import FuzzyOperatorSizeException

from typing import Callable, List, Tuple


class DiscreteUnaryOperator:

    def __init__(self, n: int, operator_vector: numpy.array = None,
                 operator_expression: Callable[[int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the base object representing the unary operator from its vector expression or its analytical
        expression.

        Args:
            n: An integer, representing the size of the finite chain.
            operator_vector: A list of integers, representing the function in its vector expression.
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the properties that define that class of operators.
                                      By default, is set to True, indicating that the properties have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        if operator_vector is None and operator_expression is None:
            raise FuzzyOperatorBadDefinition()

        self.n = n
        if operator_expression is not None:
            self.operator_expression = operator_expression

        if operator_vector is not None:
            if not len(operator_vector) == (self.n+1):
                raise FuzzyOperatorSizeException()

            if not ((operator_vector >= 0).all() and (operator_vector <= n).all()):
                raise FuzzyOperatorImageRangeException()
            self.operator_vector = operator_vector
        else:
            self.operator_vector = self.generate_operator_vector()

    def compute_completed_graph(self) -> List[Tuple[int, int]]:
        """
        Computes the completed graph of a decreasing function. The completed graph is defined as the set
        ({0}x[f(0), n])u({n}x[0, f(0)])u({(x,y) in [0, n-1]x[0, n] such that f(x+1) <= y <= f(x)}).

        Returns:
            A list of points, representing the coordinates of the completed graph.
        """
        if not self.is_decreasing():
            warnings.warn("The operator is not decreasing, so the completed graph will not correspond to its "
                          "theoretical formulation")

        completed_graph_points: List[Tuple[int, int]] = []
        for x in range(self.evaluate_operator(0), self.n+1):
            completed_graph_points.append((0, x))

        for x in range(0, self.evaluate_operator(self.n)+1):
            completed_graph_points.append((self.n, x))

        for x in range(0, self.n):
            for y in range(0, self.n+1):
                if self.evaluate_operator(x+1) <= y <= self.evaluate_operator(x):
                    completed_graph_points.append((x, y))

        return completed_graph_points

    def plot_completed_graph(self, figure_size: Tuple[int, int]):
        """
        Plots the completed graph of a decreasing function.

        Args:
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
        """
        completed_graph = self.compute_completed_graph()

        x = [point[0] for point in completed_graph]
        y = [point[1] for point in completed_graph]

        figure = plot_express.scatter(x=x, y=y)
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1])
        figure.show()

    def generate_operator_vector(self) -> numpy.array:
        """
        Generates the vector expression from the analytic function.

        Returns:
            A numpy array, representing the matrix expression of the operator.
        """
        return [self.operator_expression(x, self.n) for x in range(0, self.n+1)]

    def is_decreasing(self) -> bool:
        """
        Checks if the operator is monotone decreasing.
        """
        for x in range(0, self.n):
            if not self.operator_vector[x+1] <= self.operator_vector[x]:
                return False
        return True

    def is_increasing(self) -> bool:
        """
        Checks if the operator is monotone increasing.
        """
        for x in range(0, self.n):
            if not self.operator_vector[x+1] >= self.operator_vector[x]:
                return False
        return True

    def is_smooth(self, step: int = 1) -> bool:
        """
        Checks if the operator is k-smooth.

        Args:
            step: An integer, representing the step of smoothness.

        Returns:
            A boolean, indicating if the operator verifies the k-smoothness condition.
        """
        for x in range(0, self.n):
            if not abs(self.evaluate_operator(x + 1) - self.evaluate_operator(x)) <= step:
                return False
        return True

    def evaluate_operator(self, x: int) -> int:
        """
        Evaluates the operator in the given point.

        Args:
            x: An integer, representing the first coordinate of the point.

        Returns:
            An integer, representing the value of the function in the given point.
        """
        if self.operator_vector is not None:
            return self.operator_vector[x]
        elif self.operator_expression is not None:
            return self.operator_expression(x, self.n)

    def plot_operator(self, figure_size: Tuple[int, int]):
        """
        Plots the discrete operator.

        Args:
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
        """
        x = [i for i in range(0, self.n+1)]
        figure = plot_express.scatter(x=x, y=self.operator_vector)
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1])
        figure.show()
