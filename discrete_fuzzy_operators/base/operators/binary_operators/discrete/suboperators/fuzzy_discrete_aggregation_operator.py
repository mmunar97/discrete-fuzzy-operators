import numpy
import warnings

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import DiscreteBinaryOperator
from typing import Callable


class DiscreteAggregationBinaryOperator(DiscreteBinaryOperator):

    def __init__(self, n: int,
                 operator_matrix: numpy.ndarray = None,
                 operator_expression: Callable[[int, int, int], int] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a binary fuzzy aggregation function F: L x L -> L over a finite chain
        L={0, 1, ..., n} from its matrix.

        Args:
            operator_matrix: A two-dimensional matrix of integers, representing the images of the operator; that is,
                             in the row x and column y, the entry (x,y) represents the value of F(x, y).
            operator_expression: A Callable method with three integer arguments (x,y,n) returning an integer value.
        """
        super(DiscreteAggregationBinaryOperator, self).__init__(n, operator_matrix, operator_expression, check_properties_in_load)

        if check_properties_in_load and not(self.is_increasing() and self.evaluate_operator(0, 0) == 0 and self.evaluate_operator(self.n, self.n) == self.n):
            warnings.warn("With the input arguments, the generated operator is not a discrete aggregation function "
                          "since is not increasing or the the boundary conditions are not satisfied.")

    def checks_annihilator_element(self, element: int) -> bool:
        """
        Checks if the given element is an annihilator; that is, if for all x in L it is satisfied that
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

    def absorbing_element(self, element: int) -> bool:
        """
        Checks if the given element is an absorbing element; that is, if G(x,k)=k for all x in L, and satisfies
        G(0,x)=x for all x <= k and G(n, x)=x for all x>=k.

        Args:
            element: An integer, representing the element to check if is absorbing.

        Returns:
            A boolean, indicating if the given element is absorbing.
        """
        for x in range(0, self.n+1):
            if not self.evaluate_operator(x, element) == element:
                return False

            if x <= element:
                if not self.evaluate_operator(0, x) == x:
                    return False
            else:
                if not self.evaluate_operator(self.n, x) == x:
                    return False
        return True

    def checks_boundary_condition(self, element: int) -> bool:
        """
        Checks if the given element satisfies the boundary condition: that is, if F(x,element)=x, for all x in L.

        Args:
            element: An integer, representing the element to check if satisfies the boundary condition.

        Returns:
            A boolean, indicating if the given element satisfies the boundary condition.
        """
        for x in range(0, self.n+1):
            if not (self.evaluate_operator(x, element) == x):
                return False
        return True

    def checks_two_increasing_condition(self) -> bool:
        """
        Checks if the operator satisfies the 2-increasing condition; that is, for all x1,x2,y1,y2 in L such that x1<=x2
        and y1<=y2, then F(x1,y1)+F(x2,y2) >= F(x1,y2)+F(x2,y1).

        Returns:
            A boolean, indicating if the operator satisfies the 2-increasing condition.
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
        Checks if the operator satisfies the double boundary condition (the boundary condition of copulas); that is,
        for all x in L, then F(x,0)=F(0,x)=0 and F(x,n)=F(n,x)=x.

        Returns:
            A boolean, indicating if the operator satisfies the double boundary condition.
        """
        for x in range(0, self.n+1):
            if not (self.evaluate_operator(x, 0) == self.evaluate_operator(0, x) == 0 and
                    self.evaluate_operator(x, self.n) == self.evaluate_operator(self.n, x) == x):
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

    def is_minimum_internal(self) -> bool:
        """
        Checks if the operator is minimum-internal; that is, if for all x,y in L, it satisfies that M(x,y)<=min(x,y).

        Returns:
            A boolean, representing if the operator is minimum-internal.
        """
        for x in range(0, self.n+1):
            for y in range(0, self.n+1):
                if not self.evaluate_operator(x, y) <= min(x, y):
                    return False
        return True
