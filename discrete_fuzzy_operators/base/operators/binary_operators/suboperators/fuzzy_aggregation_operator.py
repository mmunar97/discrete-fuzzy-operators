import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.fuzzy_discrete_binary_operator import FuzzyDiscreteBinaryOperator
from typing import Callable


class DiscreteFuzzyAggregationBinaryOperator(FuzzyDiscreteBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int], int] = None):
        """
        Initializes the object that represents a binary fuzzy aggregation function F: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
        """
        super(DiscreteFuzzyAggregationBinaryOperator, self).__init__(n, operator_matrix, operator_expression)

    def checks_annihilator_element(self, element: int) -> bool:
        """
        Checks if the given element is an annihilator; that is, if for all x in L it is verified that
        F(x,element)=F(element,x)=element.

        Args:
            element: An integer, representing the element to check if is an annihilator.

        Returns:
            A boolean, indicating if the given element is an annihilator.
        """
        for x in range(0, self.n+1):
            if not (self.evaluate_operator(x, element) == self.evaluate_operator(element, x) == element):
                return False
        return True

    def checks_boundary_condition(self, element: int) -> bool:
        """
        Checks if the given element verifies the boundary condition: that is, if F(x,element)=x.

        Args:
            element: An integer, representing the element to check if verifies the boundary condition.

        Returns:
            A boolean, indicating if the given element verifies the boundary condition.
        """
        for x in range(0, self.n+1):
            if not (self.evaluate_operator(x, element) == x):
                return False
        return True

    def checks_two_increasing_condition(self) -> bool:
        """
        Checks if the operator verifies the 2-increasing condition; that is, for all x1,x2,y1,y2 in L such that x1<=x2
        and y1<=y2, then F(x1,y1)+F(x2,y2) >= F(x1,y2)+F(x2,y1).

        Returns:
            A boolean, indicating if the operator verifies the 2-increasing condition.
        """
        for x1 in range(0, self.n+1):
            for y1 in range(0, self.n+1):
                for x2 in range(x1, self.n+1):
                    for y2 in range(y1, self.n+1):
                        if not self.evaluate_operator(x1, y1)+self.evaluate_operator(x2, y2) >= \
                               self.evaluate_operator(x1, y2)+self.evaluate_operator(x2, y1):
                            return False
        return True

    def checks_double_boundary_condition(self) -> bool:
        """
        Checks if the operator verifies the double boundary condition (the boundary condition of copulas); that is,
        for all x in L, then F(x,0)=F(0,x)=0 and F(x,n)=F(n,x)=x.

        Returns:
            A boolean, indicating if the operator verifies the double boundary condition.
        """
        for x in range(0, self.n+1):
            if not self.evaluate_operator(x, 0) == self.evaluate_operator(0, x) == 0 and \
                    self.evaluate_operator(x, self.n) == self.evaluate_operator(self.n, x) == x:
                return False
        return True

    def is_commutative(self) -> bool:
        """
        Checks if the operator is commutative; that is, if verifies that for all x,y in L, then F(x,y)=F(y,x). In terms
        of matrices, the operator is commutative if the associated matrix is symmetric.

        Returns:
            A boolean, indicating if the operator is commutative.
        """
        return numpy.allclose(self.operator_matrix, self.operator_matrix.T)

    def is_associative(self) -> bool:
        """
        Checks if the operator is associative; that is, if verifies that for all x,y,z in L, then
        F(F(x,y),z)=F(x,F(y,z)).

        Returns:
            A boolean, indicating if the operator is associative.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                for z in range(0, self.n+1):
                    if not self.evaluate_operator(self.evaluate_operator(x, y), z) == \
                           self.evaluate_operator(x, self.evaluate_operator(y, z)):
                        return False
        return True

    # region Increasing property
    def is_increasing_argument(self, first_argument: bool = True) -> bool:
        """
        Checks if the operator is increasing in the first variable (if first_argument is set to True) or increasing
        in the second variable (if first_argument is set to False).

        Args:
            first_argument: A boolean, indicating if the argument to check is the first one (if True) or the
                            second one (if False).

        Returns:
            A boolean, indicating if the operator is increasing in the selected variable.
        """
        for x in range(0, self.n + 1):
            for y in range(0, self.n + 1):
                for z in range(0, self.n + 1):
                    if y <= z:
                        if first_argument:
                            if not self.evaluate_operator(x, y) <= self.evaluate_operator(x, z):
                                return False
                        else:
                            if not self.evaluate_operator(y, x) <= self.evaluate_operator(z, x):
                                return False
                    else:
                        continue
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
            return self.is_increasing_argument(first_argument=True)
        else:
            return self.is_increasing_argument(first_argument=True) and \
                   self.is_increasing_argument(first_argument=False)
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
                    if not abs(self.evaluate_operator(x+1, y)-self.evaluate_operator(x, y)) <= step:
                        return False
                else:
                    if not abs(self.evaluate_operator(y, x+1)-self.evaluate_operator(y, x)) <= step:
                        return False
        return True

    def is_smooth(self, step: int = 1) -> bool:
        """
        Checks if the operator is smooth in each variable; that is, given any y in L, then for all x in L is verified
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

    def is_divisible(self, tnorm_condition: bool = True) -> bool:
        """
        Checks if the operator is divisible; that is, if for all x,y in L with x<=y, there is z in L such that
        x=F(y,z) (with tnorm condition) or y=F(x,z) (with tconorm condition).

        Args:
            tnorm_condition: A boolean, indicating if the t-norm condition must be used (if True) or the t-conorm must
            be used (if False).

        Returns:
            A boolean, indicating if the operator is divisible.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                if x <= y:
                    found = False
                    for z in range(0, self.n+1):
                        if tnorm_condition:
                            if x == self.evaluate_operator(y, z):
                                found = True
                                break
                        else:
                            if y == self.evaluate_operator(x, z):
                                found = True
                                break
                    if not found:
                        return False
                else:
                    continue
        return True

    def is_archimedean(self, tnorm_condition: bool = True, integer_limit: int = 100) -> bool:
        """
        Checks if the operator is archimedean; that is, if for all x,y in L, there is a natural number m such that
        x^m < y, where x^m represents the archimedean operator.

        Args:
            tnorm_condition: A boolean, indicating if the t-norm condition must be used (if True) or the t-conorm must
            be used (if False).
            integer_limit: An integer, representing the maximum number to try when checking the archimedean property.

        Returns:
            A boolean, indicating if the operator is archimedean.
        """
        def archimedean_operator(x: int, m: int):
            """
            Computes the archimedean operator, defined by induction.
            """
            if m == 1:
                return x
            else:
                return self.evaluate_operator(archimedean_operator(x, m-1), x)

        for x in range(1, self.n):
            for y in range(1, self.n):
                found = False
                for m in range(1, integer_limit+1):
                    if tnorm_condition:
                        if archimedean_operator(x, m) < y:
                            found = True
                            break
                    else:
                        if archimedean_operator(x, m) > y:
                            found = True
                            break
                if not found:
                    return False
        return True

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
            for z in range(0, self.n +1):
                if z >= x:
                    for y in range(0, self.n + 1):
                        if first_argument:
                            if not self.evaluate_operator(z, y) - self.evaluate_operator(x, y) <= z-x:
                                return False
                        else:
                            if not self.evaluate_operator(y, z) - self.evaluate_operator(y, x) <= z-x:
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
