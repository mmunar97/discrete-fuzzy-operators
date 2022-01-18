import numpy
import plotly.graph_objects as go
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import \
    FuzzyDiscreteBinaryOperator
from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.tnorm import \
    Tnorm
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.fuzzy_negation_operator import \
    DiscreteFuzzyNegation
from typing import Callable, List, Tuple


class DiscreteFuzzyImplicationOperator(FuzzyDiscreteBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None):
        """
        Initializes the object that represents a binary fuzzy implication I: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of I(x, y).
        """
        super(DiscreteFuzzyImplicationOperator, self).__init__(n, operator_matrix, operator_expression)

        if not self.is_implication():
            warnings.warn("With the given parameters, the initialized operator is not a discrete implication.")

    # region Basic properties of implications
    def is_implication(self) -> bool:
        """
        Checks if the defined operator is an implication; that is, if it is decreasing in the first argument,
        increasing in the second argument and satisfies some boundary conditions.

        Returns:
            A boolean, indicating if the operator is an implication function.
        """
        return (self.is_decreasing_first_argument() and self.is_increasing_second_argument() and
                self.satisfies_boundary_conditions())

    def satisfies_boundary_conditions(self) -> bool:
        """
        Checks if the operator satisfies the boundary conditions of an implication; that is, if I(0,0)=I(n,n)=n and
        I(n,0)=0.

        Returns:
            A boolean, indicating if the operator satisfies the boundary conditions.
        """
        if self.evaluate_operator(0, 0) == self.evaluate_operator(self.n, self.n) == self.n and \
                self.evaluate_operator(self.n, 0) == 0:
            return True
        else:
            return False

    # endregion

    # region Additional properties of implications
    def satisfies_exchange_principle(self) -> bool:
        """
        Checks if the operator satisfies the exchange principle; that is, if I(x,I(y,z)) = I(y, I(x,z)) for all x,y,z
        in the domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if not self.evaluate_operator(x, self.evaluate_operator(y, z)) == \
                           self.evaluate_operator(y, self.evaluate_operator(x, z)):
                        return False
        return True

    def satisfies_neutrality_principle(self) -> bool:
        """
        Checks if the operator satisfies the neutrality principle; that is, if I(n,x)=x for all x in the domain.
        """
        for x in range(0, self.n + 1):
            if self.evaluate_operator(self.n, x) != x:
                return False
        return True

    def satisfies_contrapositive_symmetry(self, negation: DiscreteFuzzyNegation) -> bool:
        """
        Checks if the operator satisfies the contrapositive symmetry with respect to a fuzzy negation; that is, if
        I(x,y)=I(N(y),N(x)) for all x,y in the domain.
        """
        if not negation.is_negation():
            warnings.warn("The selected negation operator is not a fuzzy discrete negation. "
                          "Some results may not be correct.")

        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                if self.evaluate_operator(x, y) != self.evaluate_operator(x=negation.evaluate_operator(y),
                                                                          y=negation.evaluate_operator(x)):
                    return False
        return True

    def satisfies_identity_principle(self) -> bool:
        """
        Checks if the operator satisfies the identity principle; that is, if I(x,x)=n for all x in the domain.
        """
        for x in range(0, self.n + 1):
            if self.evaluate_operator(x, x) != self.n:
                return False
        return True

    def satisfies_ordering_principle(self) -> bool:
        """
        Checks if the operator satisfies the ordering principle; that is, if I(x,y)=n if and only if x<=y, for all x,y
        in the domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                if not (self.evaluate_operator(x, y) == self.n and x <= y):
                    return False
        return True

    def satisfies_consequent_boundary(self) -> bool:
        """
        Checks if the operator satisfies the consequent boundary property; that is, if I(x,y) >= y, for all x,y in the
        domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                if not (self.evaluate_operator(x, y) >= y):
                    return False
        return True

    def satisfies_modus_ponens(self, t_norm: Tnorm) -> bool:
        """
        Checks if the operator satisfies the modus ponens with respect to a discrete t-norm; that is, if T(x,I(x,y)) <= y.

        Args:
            t_norm: A Tnorm object, representing a discrete t-norm.
        """
        for x in range(0, self.n +1):
            for y in range(0, self.n +1):
                if not(t_norm.evaluate_operator(x, self.evaluate_operator(x, y)) <= y):
                    return False
        return True

    def satisfies_modus_tollens(self, negation: DiscreteFuzzyNegation,
                                t_norm: Tnorm) -> bool:
        """
        Checks if the operator satisfies the modus tollens with respect to a discrete t-norm T and a discrete negation N;
        that is, if T(N(y),I(x,y)) <= N(x).

        Args:
            negation: A DiscreteFuzzyNegationOperator object, representing a discrete negation.
            t_norm: A Tnorm object, representing a discrete t-norm.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n +1):
                if not(t_norm.evaluate_operator(negation.evaluate_operator(y), self.evaluate_operator(x, y)) <= negation.evaluate_operator(x)):
                    return False
        return True

    def satisfies_law_importation(self, t_norm: Tnorm) -> bool:
        """
        Checks if the operator satisfies the law of importation with respect to a discrete t-norm; that is, if
        I(T(x,y),z) = I(x, I(y,z)).

        Args:
            t_norm: A Tnorm object, representing a discrete t-norm.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                for z in range(0, self.n+1):
                    if not(self.evaluate_operator(t_norm.evaluate_operator(x, y), z) ==
                           self.evaluate_operator(x, self.evaluate_operator(y, z))):
                        return False
        return True
    # endregion

    # region Plot of the unit extension
    def __generate_discrete_points(self) -> Tuple[List[float], List[float], List[float]]:
        """
        Generates the three-dimensional points of the implications and applies a linear transformation to embed the 
        points in the unit cube.
        
        Returns:
            A tuple of three lists, containing the pairs of points (x,y,z) to be plotted.
        """
        x = []
        y = []
        z = []
        for i in range(0, self.n+1):
            for j in range(0, self.n+1):
                x.append(i/self.n)
                y.append(j/self.n)
                z.append(self.evaluate_operator(i, j)/self.n)

        return x, y, z

    def __extend_continually_implication(self, x_point: int, y_point: int, intermediate_steps: int = 20) -> Tuple[List[float], List[float], numpy.ndarray]:
        """
        Computes the unit extension of a discrete implication. In the square generated with the point
        (x_point/n, y_point/n) and size 1/n, two planes are computed; the first one is located in the upper triangle
        respect the diagonal, and the second one is located in the lower triangle respect the diagonal.

        Args:
            x_point: An integer, representing the first component of the point to carry out the interpolation.
            y_point: An integer, representing the second component of the point to carry out the interpolation.
            intermediate_steps: An integer, representing the number of steps to plot the unit plot.

        Returns:
            A tuple of three elements: two lists containing the components of the points and a matrix representing the
            mapping to be plotted.
        """
        x_values = numpy.linspace(x_point/self.n, (x_point+1)/self.n, intermediate_steps)
        y_values = numpy.linspace(y_point/self.n, (y_point+1)/self.n, intermediate_steps)
        continuous_function_values = numpy.zeros((len(x_values), len(y_values)))
        for x_idx, x in enumerate(x_values):
            for y_idx, y in enumerate(y_values):
                adv_i1_j1 = self.evaluate_operator(x_point+1, y_point+1)/self.n
                adv_i_j1 = self.evaluate_operator(x_point, y_point+1)/self.n
                adv_i1_j = self.evaluate_operator(x_point+1, y_point)/self.n
                adv_i_j = self.evaluate_operator(x_point, y_point)/self.n

                if y-y_point/self.n >= x-x_point/self.n:
                    z = adv_i_j + self.n * (x - x_point / self.n) * (adv_i1_j1 - adv_i_j1) + self.n * (
                                y - y_point / self.n) * (adv_i_j1 - adv_i_j)
                else:
                    z = adv_i_j + self.n * (x - x_point / self.n) * (adv_i1_j - adv_i_j) + self.n * (
                                y - y_point / self.n) * (adv_i1_j1 - adv_i1_j)

                continuous_function_values[y_idx, x_idx] = z

        return x_values, y_values, continuous_function_values

    def plot_continuous_extension(self, figure_size: Tuple[int, int], figure_title: str,
                                  show_contour: bool = True, **kwargs):
        """
        Plots the unit extension of a discrete implication; that is, the unit implication defined in the
        unit interval such that its discretization is the given discrete implication.

        Args:
            figure_size: A tuple of two integers, representing the size of the figure. The order is WIDTH and HEIGHT.
            figure_title: A string, representing the label of the operator.
            show_contour: A boolean, indicating if the contour of the cube has to be shown.
        """
        x_discrete, y_discrete, z_discrete = self.__generate_discrete_points()

        plot = []

        for i in range(0, self.n):
            for j in range(0, self.n):
                x_continuous, y_continuous, z_continuous = self.__extend_continually_implication(x_point=i, y_point=j, **kwargs)
                plot.append(go.Surface(x=x_continuous, y=y_continuous, z=z_continuous, showscale=False, cmin=0, cmax=1))

        plot.append(go.Scatter3d(x=x_discrete, y=y_discrete, z=z_discrete,
                                 mode="markers", name=figure_title,
                                 marker=dict(size=12, color=['rgb(0,0,0)'], opacity=0.9)))

        if show_contour:
            plot = plot+self.generate_unit_cube_contour(draw_diagonal=False)

        fig = go.Figure(data=plot)
        fig.update_layout(
            autosize=True,
            width=figure_size[0],
            height=figure_size[1]
        )

        fig.show()
    # endregion
