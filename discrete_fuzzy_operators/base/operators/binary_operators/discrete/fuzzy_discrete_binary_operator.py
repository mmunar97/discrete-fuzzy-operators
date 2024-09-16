import numpy
import plotly.graph_objects as go

from discrete_fuzzy_operators.base.exceptions.operators.operator_bad_definition import FuzzyOperatorBadDefinition
from discrete_fuzzy_operators.base.exceptions.operators.operator_range_invalid import FuzzyOperatorImageRangeException
from discrete_fuzzy_operators.base.exceptions.operators.operator_size_exception import FuzzyOperatorSizeException

from typing import Callable, List, Tuple


class DiscreteBinaryOperator:

    def __init__(self, n: int, operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the base object representing the operator from its matrix expression or its analytical expression.

        Args:
            n: An integer, representing the size of the finite chain.
            operator_matrix: A numpy array, representing the operator in its matrix expression.
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the properties that define that class of operators.
                                      By default, is set to True, indicating that the properties have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
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

    def is_commutative(self) -> bool:
        """
        Checks if the operator is commutative; that is, if satisfies that for all x,y in L, then F(x,y)=F(y,x). In terms
        of matrices, the operator is commutative if the associated matrix is symmetric.

        Returns:
            A boolean, indicating if the operator is commutative.
        """
        return numpy.allclose(self.operator_matrix, self.operator_matrix.T)

    def is_associative(self) -> bool:
        """
        Checks if the operator is associative; that is, if satisfies that for all x,y,z in L, then
        F(F(x,y),z)=F(x,F(y,z)).

        Returns:
            A boolean, indicating if the operator is associative.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                for z in range(0, self.n+1):
                    if not(self.evaluate_operator(self.evaluate_operator(x, y), z) ==
                           self.evaluate_operator(x, self.evaluate_operator(y, z))):
                        return False
        return True

    def is_idempotent_free(self) -> bool:
        """
        Checks if the operator is idempotent-free; that is, if the unique idempotent elements are 0 and n.

        Returns:
            A boolean, indicating if the operator is idempotent-free.
        """
        for x in range(1, self.n):
            if self.evaluate_operator(x, x) == x:
                return False
        return True

    def is_idempotent(self) -> bool:
        """
        Checks if the operator is idempotent; that is, if F(x,x)=x for all x in Lm.

        Returns:
            A boolean, indicating if the operator is idempotent.
        """
        for x in range(0, self.n+1):
            if not self.evaluate_operator(x,x) == x:
                return False
        return True

    # region Increasing property
    def is_increasing_first_argument(self) -> bool:
        """
        Checks if the operator is increasing in the first variable.

        Returns:
            A boolean, indicating if the operator is increasing in the first variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if not self.evaluate_operator(y, x) <= self.evaluate_operator(z, x):
                            return False
        return True

    def is_increasing_second_argument(self) -> bool:
        """
        Checks if the operator is increasing in the second variable.

        Returns:
            A boolean, indicating if the operator is increasing in the second variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if not self.evaluate_operator(x, y) <= self.evaluate_operator(x, z):
                            return False
        return True

    def is_decreasing_first_argument(self) -> bool:
        """
        Checks if the operator is decreasing in the first variable.

        Returns:
            A boolean, indicating if the operator is decreasing in the first variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if not self.evaluate_operator(y, x) >= self.evaluate_operator(z, x):
                            return False
        return True

    def is_decreasing_second_argument(self) -> bool:
        """
        Checks if the operator is decreasing in the second variable.

        Returns:
            A boolean, indicating if the operator is decreasing in the second variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if not self.evaluate_operator(x, y) >= self.evaluate_operator(x, z):
                            return False
        return True

    def is_increasing(self) -> bool:
        """
        Checks if the operator is increasing in each variable; that is, given any x in L, then for all y,z in L such
        that y<=z, then F(x,y)<=F(x,z) and  F(y,x)<=F(z,x). Note that if the operator is commutative, only the first
        inequality must be checked.

        Returns:
            A boolean, indicating if the operator is increasing in each variable.
        """
        if self.is_commutative():
            return self.is_increasing_first_argument()
        else:
            return self.is_increasing_first_argument() and self.is_increasing_second_argument()

    def is_decreasing(self) -> bool:
        """
        Checks if the operator is decreasing in each variable; that is, given any x in L, then for all y,z in L such
        that y<=z, then F(x,y)>=F(x,z) and  F(y,x)>=F(z,x). Note that if the operator is commutative, only the first
        inequality must be checked.

        Returns:
            A boolean, indicating if the operator is decreasing in each variable.
        """
        if self.is_commutative():
            return self.is_decreasing_first_argument()
        else:
            return self.is_decreasing_first_argument() and self.is_decreasing_second_argument()

    # endregion

    # region Smoothness property
    def is_smooth_argument(self, step: int = 1, first_argument: bool = True) -> bool:
        """
        Checks if the operator is smooth in the first variable (if first_argument is set to True) or smooth
        in the second variable (if first_argument is set to False).

        Args:
            step: An integer, representing the step of smoothness.
            first_argument: A boolean, indicating if the argument to check is the first one (if True) or the
                            second one (if False).

        Returns:
            A boolean, indicating if the operator is smooth in the selected variable.
        """
        for y in range(0, self.n + 1):
            for x in range(0, self.n):
                if first_argument:
                    if not abs(self.evaluate_operator(x + 1, y) - self.evaluate_operator(x, y)) <= step:
                        return False
                else:
                    if not abs(self.evaluate_operator(y, x + 1) - self.evaluate_operator(y, x)) <= step:
                        return False
        return True

    def is_smooth(self, step: int = 1) -> bool:
        """
        Checks if the operator is smooth in each variable; that is, given any y in L, then for all x in L is satisfied
        that |F(x+1, y)-F(x,y)| <= k and |F(y, x+1)-F(y,x+1)| <= k, where k is the step. Note that if the operator is
        commutative, only the first inequality must be checked.

        Args:
            step: An integer, representing the step of smoothness.

        Returns:
            A boolean, indicating if the operator is smooth in each variable.
        """
        if self.is_commutative():
            return self.is_smooth_argument(step=step, first_argument=True)
        else:
            return self.is_smooth_argument(step=step, first_argument=True) and \
                   self.is_smooth_argument(step=step, first_argument=False)

    # endregion

    # region Lipschitz property
    def is_lipschitz_argument(self, first_argument: bool = True) -> bool:
        """
        Checks if the operator is Lipschitz with respect to the first argument (if first_argument is set to True) or
        to the second argument (is first_argument is set to False).

        Args:
            first_argument: A boolean, indicating if the argument to check is the first one (if True) or the
                            second one (if False).

        Returns:
            A boolean, indicating if the operator is Lipschitz in the selected variable.
        """
        for x in range(0, self.n + 1):
            for z in range(0, self.n + 1):
                if z >= x:
                    for y in range(0, self.n + 1):
                        if first_argument:
                            if not self.evaluate_operator(z, y) - self.evaluate_operator(x, y) <= z - x:
                                return False
                        else:
                            if not self.evaluate_operator(y, z) - self.evaluate_operator(y, x) <= z - x:
                                return False
                else:
                    continue
        return True

    def is_lipschitz(self) -> bool:
        """
        Checks if the operator is Lipschitz in each variable; that is, for all x,y,z in L such that z>=x, then
        F(z,y)-F(x,y) <= z-x and F(y,z)-F(y,x) <= x-z. Note that if the operator is commutative, only the first
        inequality must be checked.

        Returns:
            A boolean, indicating if the operator is Lipschitz in each variable.
        """
        if self.is_commutative():
            return self.is_lipschitz_argument(first_argument=True)
        else:
            return self.is_lipschitz_argument(first_argument=True) and self.is_lipschitz_argument(
                first_argument=False)
    # endregion

    # region Plot generation
    def plot_operator(self, figure_size: Tuple[int, int] = (700, 700), figure_title: str = "Discrete operator"):
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
                operator_values.append(self.evaluate_operator(x, y))

        discrete_scatter = go.Scatter3d(
            x=x_disc,
            y=y_disc,
            z=operator_values,
            mode="markers",
            name=figure_title,
            marker=dict(size=12, color=['rgb(0,0,0)'], opacity=0.9)
        )

        figure = go.Figure(data=[discrete_scatter]+self.generate_discrete_cube_contour(draw_diagonal=False))
        figure.update_layout(autosize=True, width=figure_size[0], height=figure_size[1],
                             legend=dict(yanchor="bottom", xanchor="center"),
                             scene=dict(xaxis_title=r'X',
                                        yaxis_title=r'Y',
                                        zaxis_title=r'Z')
                             )
        figure.show()

    def plot_three_dimensional_operator(self,
                                        draw_diagonal: bool,
                                        figure_size: Tuple[int, int] = (700, 700),
                                        figure_title: str = "Three dimensional operator"):
        """
        Draw the binary operator as a cube in three dimensions. The operator is given by a function F(x,y) and the
        function G(x,y,z)=F(x, F(y,z)) is being drawn.

        So that it can be visualised, at each point (x,y,z) in space the value corresponding to evaluate the function
        G is placed.

        Args:
            draw_diagonal: A boolean, indicating if the main diagonal of the cube has to be drawn; that is, if the
                           line which joins the point (n, n, n) with (0, 0, 0).
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
            figure_title: A string, representing the label of the operator.
        """
        x_disc = []
        y_disc = []
        z_disc = []
        values = []

        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    x_disc.append(x)
                    y_disc.append(y)
                    z_disc.append(z)

                    values.append(self.evaluate_operator(x, self.evaluate_operator(y, z)))

        discrete_scatter = go.Scatter3d(
            x=x_disc,
            y=y_disc,
            z=z_disc,
            text=values,
            mode="markers+text",
            name=figure_title,
            marker=dict(size=12, color=values, opacity=0.9)
        )

        figure = go.Figure(data=[discrete_scatter]+self.generate_discrete_cube_contour(draw_diagonal=draw_diagonal))
        figure.update_layout(autosize=True,
                             width=figure_size[0], height=figure_size[1],
                             legend=dict(yanchor="bottom", xanchor="center"))
        figure.show()

    def generate_discrete_cube_contour(self, draw_diagonal: bool) -> List[go.Scatter3d]:
        """
        Generates the contour of the cube which embeds the plot inside.

        Args:
            draw_diagonal: A boolean, indicating if the main diagonal of the cube has to be drawn; that is, if the
                           line which joins the point (n, n, n) with (0, 0, 0).

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

    def generate_unit_cube_contour(self, draw_diagonal: bool) -> List[go.Scatter3d]:
        """
        Generates the contour of the cube which embeds the plot inside.

        Args:
            draw_diagonal: A boolean, indicating if the main diagonal of the cube has to be drawn; that is, if the
                           line which joins the point (n, n, n) with (0, 0, 0).

        Returns:
            A Scatter3d object, representing the shape of the cube.
        """
        n = self.n
        coordinates_x = [0, n, n, 0, 0, 0, n, n, n, n, n, n, 0, 0, 0, 0]
        coordinates_x = [x / n for x in coordinates_x]
        coordinates_y = [0, 0, n, n, 0, 0, 0, 0, 0, n, n, n, n, n, n, 0]
        coordinates_y = [y / n for y in coordinates_y]
        coordinates_z = [0, 0, 0, 0, 0, n, n, 0, n, n, 0, n, n, 0, n, n]
        coordinates_z = [z / n for z in coordinates_z]

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
    # endregion