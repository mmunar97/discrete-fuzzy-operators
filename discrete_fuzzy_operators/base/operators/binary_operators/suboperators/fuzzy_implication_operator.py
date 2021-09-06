import numpy
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.fuzzy_discrete_binary_operator import \
    FuzzyDiscreteBinaryOperator
from typing import Callable

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import \
    DiscreteFuzzyAggregationBinaryOperator
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.fuzzy_negation_operator import \
    DiscreteFuzzyNegation


class DiscreteFuzzyImplicationOperator(FuzzyDiscreteBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int], int] = None):
        """
        Initializes the object that represents a binary fuzzy implication I: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of I(x, y).
        """
        super(DiscreteFuzzyImplicationOperator, self).__init__(n, operator_matrix, operator_expression)

    # region Basic properties of implications
    def is_implication(self) -> bool:
        """Checks if the defined operator is an implication; that is, if it is decreasing inf the first argument,
        increasing in the second argument and verifies some boundary conditions.

        Returns:
            A boolean, indicating if the operator is an implication function.
        """
        return (self.is_decreasing_first_argument() and self.is_increasing_first_argument() and
                self.verifies_boundary_conditions())

    def is_decreasing_first_argument(self) -> bool:
        """
        Checks if the operator is decreasing in the first variable.

        Returns:
            A boolean, indicating if the operator is decreasing in the selected variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if x <= z:
                        if not self.evaluate_operator(x, y) >= self.evaluate_operator(z, y):
                            return False
                    else:
                        continue
        return True

    def is_increasing_first_argument(self) -> bool:
        """
        Checks if the operator is increasing in the first variable.

        Returns:
            A boolean, indicating if the operator is increasing in the selected variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if not self.evaluate_operator(x, y) <= self.evaluate_operator(x, z):
                            return False
                    else:
                        continue
        return True

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of an implication; that is, if I(0,0)=I(n,n)=n and
        I(n,0)=0.

        Returns:
            A boolean, indicating if the operator verifies the boundary conditions.
        """
        if self.evaluate_operator(0, 0) == self.evaluate_operator(self.n, self.n) == self.n and \
                self.evaluate_operator(self.n, 0) == 0:
            return True
        else:
            return False

    # endregion

    # region Additional properties of implications
    def verifies_exchange_principle(self) -> bool:
        """
        Checks if the operator verifies the exchange principle; that is, if I(x,I(y,z)) = I(y, I(x,z)) for all x,y,z
        in the domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if not self.evaluate_operator(x, self.evaluate_operator(y, z)) == \
                           self.evaluate_operator(y, self.evaluate_operator(x, z)):
                        return False
        return True

    def verifies_neutrality_principle(self) -> bool:
        """
        Checks if the operator verifies the neutrality principle; that is, if I(n,x)=x for all x in the domain.
        """
        for x in range(0, self.n + 1):
            if self.evaluate_operator(self.n, x) != x:
                return False
        return True

    def verifies_contrapositive_symmetry(self, negation: DiscreteFuzzyNegation) -> bool:
        """
        Checks if the operator verifies the contrapositive symmetry with respect to a fuzzy negation; that is, if
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

    def verifies_identity_principle(self) -> bool:
        """
        Checks if the operator verifies the identity principle; that is, if I(x,x)=n for all x in the domain.
        """
        for x in range(0, self.n + 1):
            if self.evaluate_operator(x, x) != self.n:
                return False
        return True

    def verifies_ordering_principle(self) -> bool:
        """
        Checks if the operator verifies the ordering principle; that is, if I(x,y)=n if and only if x<=y, for all x,y
        in the domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                if not (self.evaluate_operator(x, y) == self.n and x <= y):
                    return False
        return True

    def verifies_consequent_boundary(self) -> bool:
        """
        Checks if the operator verifies the consequent boundary property; that is, if I(x,y) >= y, for all x,y in the
        domain.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                if not (self.evaluate_operator(x, y) >= y):
                    return False
        return True

    def verifies_modus_ponens(self, t_norm: DiscreteFuzzyAggregationBinaryOperator) -> bool:
        """
        Checks if the operator verifies the modus ponens with respect to a discrete t-norm; that is, if T(x,I(x,y)) <= y.

        Args:
            t_norm: A DiscreteFuzzyAggregationBinaryOperator object, representing a discrete t-norm.
        """
        for x in range(0, self.n +1):
            for y in range(0, self.n +1):
                if not(t_norm.evaluate_operator(x, self.evaluate_operator(x, y)) <= y):
                    return False
        return True

    def verifies_modus_tollens(self, negation: DiscreteFuzzyNegation,
                               t_norm: DiscreteFuzzyAggregationBinaryOperator) -> bool:
        """
        Checks if the operator verifies the modus tollens with respect to a discrete t-norm T and a discrete negation N;
        that is, if T(N(y),I(x,y)) <= N(x).

        Args:
            negation: A DiscreteFuzzyNegationOperator object, representing a discrete negation.
            t_norm: A DiscreteFuzzyAggregationBinaryOperator object, representing a discrete t-norm.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n +1):
                if not(t_norm.evaluate_operator(negation.evaluate_operator(y), self.evaluate_operator(x, y)) <= negation.evaluate_operator(x)):
                    return False
        return True

    def verifies_law_importation(self, t_norm: DiscreteFuzzyAggregationBinaryOperator) -> bool:
        """
        Checks if the operator verifies the law of importation with respect to a discrete t-norm; that is, if
        I(T(x,y),z) = I(x, I(y,z)).

        Args:
            t_norm: A DiscreteFuzzyAggregationBinaryOperator object, representing a discrete t-norm.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                for z in range(0, self.n+1):
                    if not(self.evaluate_operator(t_norm.evaluate_operator(x, y), z) ==
                           self.evaluate_operator(x, self.evaluate_operator(y, z))):
                        return False
        return True
    # endregion
