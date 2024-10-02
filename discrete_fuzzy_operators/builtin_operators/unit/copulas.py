from enum import Enum
from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_copula import \
    FuzzyUnitCopula


class CopulaExamples(Enum):
    """
    Object that stores the values of the most known negations.
    """

    FGM = "unit_fgm_copula"

    @staticmethod
    def get_copula(copula: "CopulaExamples", **kwargs) -> FuzzyUnitCopula:
        """
        Returns a FuzzyUnitCopula object representing the selected copula.

        Args:
            copula: A Copula value, representing the chosen copula.
            **kwargs: Parameters

        Returns:
            A FuzzyUnitCopula object.
        """

        if copula == CopulaExamples.FGM:
            return FuzzyUnitCopula(lambda x, y: CopulaExamples.__fgm_copula(x=x, y=y, **kwargs))

    @staticmethod
    def __fgm_copula(x: float, y: float, k: float) -> float:
        """
        Implementation of the Farlie-Gumbel-Morgenstern (FGM) copula

        Args:
            x: A float, representing the first argument of the copula.
            y: A float, representing the second argument of the copula.
            k: A float, representing the parameter of the FGM copula.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """

        if not -1 <= k <= 1:
            raise Exception("To define a FM copula, the parameter should be in the interval [-1,1]")

        return x * y + k * x * (1 - x) * y * (1 - y)
