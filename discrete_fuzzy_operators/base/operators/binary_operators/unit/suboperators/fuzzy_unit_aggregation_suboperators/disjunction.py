import warnings
from typing import Callable
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_operator import \
    FuzzyUnitAggregationBinaryOperator
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.conjunction import \
    FuzzyUnitConjunction
from discrete_fuzzy_operators.base.operators.unary_operators.unit.suboperators.fuzzy_negation_operator import FuzzyNegation


class FuzzyUnitDisjunction(FuzzyUnitAggregationBinaryOperator):

    def __init__(self, operator_expression: Callable[[float, float], float] = None,
                 check_properties_in_load: bool = True):
        """
        Initializes the object that represents a fuzzy disjunction D: [0,1]x[0,1] -> [0,1] from its analytical
        expression.

        Args:
            operator_expression: A function, representing the analytical expression.
            check_properties_in_load: A boolean, indicating if the operator has to be loaded without checking the
            properties that define that class of operators. By default, is set to True, indicating that the properties
            have to be checked.
        """
        self.check_properties_in_load = check_properties_in_load
        super(FuzzyUnitDisjunction, self).__init__(operator_expression, check_properties_in_load)

        if check_properties_in_load and not self.is_fuzzy_disjunction():
            warnings.warn("With the input arguments, the generated operator is not a fuzzy disjunction since "
                          "it is not increasing and/or satisfies the boundary conditions.")

    def is_fuzzy_disjunction(self) -> bool:
        """
        Checks if the operator is a fuzzy disjunction; that is, if it is an aggregation function and satisfies
        the boundary conditions.
        """
        return self.is_fuzzy_aggregation() and self.verifies_boundary_conditions()

    def verifies_boundary_conditions(self) -> bool:
        """
        Checks if the operator verifies the boundary conditions of a fuzzy disjunction; that is, if D(1,0)=D(0,1)=1.
        """
        if self.evaluate_operator(1, 0) == 1 and self.evaluate_operator(0, 1) == 1:
            return True
        return False

    def get_dual_conjunction(self) -> FuzzyUnitConjunction:
        """
        Computes the dual fuzzy conjunction associated to the disjunction; that is, the discrete binary operator C
        given by C(x,y)=1-D(1-x,1-y), for all x,y in [0,1].

        Returns:
            A FuzzyUnitConjunction object, representing the dual operator.
        """
        return FuzzyUnitConjunction(lambda x, y: 1 - self.evaluate_operator(1 - x, 1 - y))

    def get_Ndual_conjunction(self, fuzzy_negation: FuzzyNegation) -> FuzzyUnitConjunction:
        """
        Computes the N-dual fuzzy conjunction associated to the disjunction with respect to a strong negation N; that is,
        the discrete binary operator C given by C(x,y)=N(D(N(x),N(y))), for all x,y in [0,1].

        Args:
       fuzzy_negation: A FuzzyNegation object, representing the strong fuzzy negation.

        Returns:
            A FuzzyUnitConjunction object, representing the N-dual operator.
        """
        if not fuzzy_negation.is_strong():
            warnings.warn("In order to compute the N-dual of a fuzzy disjunction a strong negation is needed.")
        return FuzzyUnitConjunction(lambda x, y: fuzzy_negation.evaluate_operator(self.evaluate_operator(fuzzy_negation.evaluate_operator(x),
                                                                                                         fuzzy_negation.evaluate_operator(y))))