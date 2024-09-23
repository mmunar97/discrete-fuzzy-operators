from enum import Enum
from discrete_fuzzy_operators.base.operators.unary_operators.unit.suboperators.fuzzy_negation_operator import \
    FuzzyNegation


class NegationExamples(Enum):
    """
    Object that stores the values of the most known negations.
    """
    CLASSIC = "classic_negation"
    LEAST = "least_negation"
    GREATEST = "greatest_negation"
    SUGENO = "sugeno"
    YAGER = "yager"

    @staticmethod
    def get_negation(negation: "NegationExamples", k=float) -> FuzzyNegation:
        """
        Returns a FuzzyNegation object representing the selected negation.

        Args:
            negation: A Negation value, representing the chosen negation.
            k: A float value, representing the corresponding parameter for sugeno or yagers negation

        Returns:
            A FuzzyNegation object.
        """
        if negation == NegationExamples.CLASSIC:
            return FuzzyNegation(operator_expression=NegationExamples.__classical_negation)
        elif negation == NegationExamples.LEAST:
            return FuzzyNegation(operator_expression=NegationExamples.__least_negation)
        elif negation == NegationExamples.GREATEST:
            return FuzzyNegation(operator_expression=NegationExamples.__greatest_negation)
        elif negation == NegationExamples.SUGENO:
            return FuzzyNegation(operator_expression=lambda x: NegationExamples.__sugeno(x=x, k=k))
        elif negation == NegationExamples.YAGER:
            return FuzzyNegation(operator_expression=lambda x: NegationExamples.__yager(x=x, k=k))

    @staticmethod
    def __classical_negation(x: float) -> float:
        """
        Implementation of the classical fuzzy negation.

        Args:
            x: A float, representing the coordinate of the evaluation point.

        Returns:
            A float, representing the value of the negation in the point.
        """
        return 1 - x

    @staticmethod
    def __least_negation(x: float) -> float:
        """
        Implementation of the least fuzzy negation.

        Args:
            x: A float, representing the coordinate of the evaluation point.

        Returns:
            An integer, representing the value of the negation in the point.
        """
        if x == 0:
            return 1
        else:
            return 0

    @staticmethod
    def __greatest_negation(x: float) -> float:
        """
        Implementation of the greatest fuzzy negation.

        Args:
            x: A float, representing the coordinate of the evaluation point.

        Returns:
            A float, representing the value of the negation in the point.
        """
        if x == 1:
            return 0
        else:
            return 1

    @staticmethod
    def __sugeno(x: float, k: float) -> float:
        """
        Implementation of a fuzzy negation in the sugeno's class.

        Args:
            x: A float, representing the coordinate of the evaluation point.
            k: A float, representing the parameter of the sugeno fuzzy negation.

        Returns:
            A float, representing the value of the negation in the point.
        """

        if not k < 1:
            raise Exception("To define a fuzzy negation in the sugeno's class, the parameter should be less than 1.")

        return (1 - x) / (1 - k * x)

    @staticmethod
    def __yager(x: float, k: float) -> float:
        """
        Implementation of a fuzzy negation in the yager's class.

        Args:
            x: A float, representing the coordinate of the evaluation point.
            k: A float, representing the parameter of the yager fuzzy negation.

        Returns:
            A float, representing the value of the negation in the point.
        """

        if not k > 0:
            raise Exception("To define a fuzzy negation in the yager's class, the parameter should be greater than 0.")

        return (1 - x ** k) ** (1 / k)
