from enum import Enum

from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_tconorm import \
    FuzzyUnitTconorm


class UnitTconormExamples(Enum):
    """
    Object that stores the values of the most known tconorms defined in [0, 1].
    """

    MAXIMUM = "unit_maximum_tconorm"
    PROBABILISTICSUM = "unit_probabilisticsum_tconorm"
    LUKASIEWICZ = "unit_lukasiewicz_tconorm"
    DRASTICSUM = "unit_drasticsum_tconorm"
    NILPOTENTMAXIMUM = "unit_nilpotentmaximum_tconorm"

    @staticmethod
    def get_unit_tconorm(tconorm: "UnitTconormExamples") -> FuzzyUnitTconorm:

        """
        Returns a UnitTconormExamples object representing the selected tconorm.

        Args:
            tconorm: A UnitTconormExamples value, representing the chosen tconorm.

        Returns:
            FuzzyUnitTconorm object.
        """
        if tconorm == UnitTconormExamples.MAXIMUM:
            return FuzzyUnitTconorm(UnitTconormExamples.__maximum_tconorm)
        elif tconorm == UnitTconormExamples.PROBABILISTICSUM:
            return FuzzyUnitTconorm(UnitTconormExamples.__probabilisticsum_tconorm)
        elif tconorm == UnitTconormExamples.LUKASIEWICZ:
            return FuzzyUnitTconorm(UnitTconormExamples.__lukasiewicz_tconorm)
        elif tconorm == UnitTconormExamples.DRASTICSUM:
            return FuzzyUnitTconorm(UnitTconormExamples.__drasticsum_tconorm)
        elif tconorm == UnitTconormExamples.NILPOTENTMAXIMUM:
            return FuzzyUnitTconorm(UnitTconormExamples.__nilpotentmaximum_tconorm)


    @staticmethod
    def __maximum_tconorm(x: float, y: float) -> float:
        """
        Implementation of the maximum tconorm.

        Args:
            x: A float, representing the first argument of the tconorm.
            y: A float, representing the second argument of the tconorm.

        Returns:
            A float, representing the value of the tconorm in the point (x,y).
        """
        return max(x, y)

    @staticmethod
    def __probabilisticsum_tconorm(x: float, y: float) -> float:
        """
        Implementation of the probabilistic sum tconorm.

        Args:
            x: A float, representing the first argument of the tconorm.
            y: A float, representing the second argument of the tconorm.

        Returns:
            A float, representing the value of the tconorm in the point (x,y).
        """
        return x+y-x*y

    @staticmethod
    def __lukasiewicz_tconorm(x: float, y: float) -> float:
        """
        Implementation of the lukasiewicz tconorm.

        Args:
            x: A float, representing the first argument of the tconorm.
            y: A float, representing the second argument of the tconorm.

        Returns:
            A float, representing the value of the tconorm in the point (x,y).
        """
        return min(x+y, 1)

    @staticmethod
    def __drasticsum_tconorm(x: float, y: float) -> float:
        """
        Implementation of the drastic sum tconorm.

        Args:
            x: A float, representing the first argument of the tconorm.
            y: A float, representing the second argument of the tconorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        if 0 < x <= 1 and 0 < y <= 1:
            return 1
        else:
            return max(x, y)

    @staticmethod
    def __nilpotentmaximum_tconorm(x: float, y: float) -> float:
        """
        Implementation of the drastic nilpotent maximum tconorm.

        Args:
            x: A float, representing the first argument of the tconorm.
            y: A float, representing the second argument of the tconorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        if x+y >= 1:
            return 1
        else:
            return max(x, y)