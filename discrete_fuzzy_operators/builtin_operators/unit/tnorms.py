from enum import Enum

from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_aggregation_suboperators.unit_tnorm import \
    FuzzyUnitTnorm


class UnitTnormExamples(Enum):
    """
    Object that stores the values of the most known tnorms defined in [0, 1].
    """

    MINIMUM = "unit_minimum_tnorm"
    PRODUCT = "unit_product_tnorm"
    LUKASIEWICZ = "unit_lukasiewicz_tnorm"
    DRASTICPRODUCT = "unit_drasticproduct_tnorm"
    NILPOTENTMINIMUM = "unit_nilpotentminimum_tnorm"

    @staticmethod
    def get_unit_tnorm(tnorm: "UnitTnormExamples") -> FuzzyUnitTnorm:

        """
        Returns a UnitTnormExamples object representing the selected tnorm.

        Args:
            tnorm: A UnitTnormExamples value, representing the chosen tnorm.

        Returns:
            FuzzyUnitTnorm object.
        """
        if tnorm == UnitTnormExamples.MINIMUM:
            return FuzzyUnitTnorm(UnitTnormExamples.__minimum_tnorm)
        elif tnorm == UnitTnormExamples.PRODUCT:
            return FuzzyUnitTnorm(UnitTnormExamples.__product_tnorm)
        elif tnorm == UnitTnormExamples.LUKASIEWICZ:
            return FuzzyUnitTnorm(UnitTnormExamples.__lukasiewicz_tnorm)
        elif tnorm == UnitTnormExamples.DRASTICPRODUCT:
            return FuzzyUnitTnorm(UnitTnormExamples.__drasticproduct_tnorm)
        elif tnorm == UnitTnormExamples.NILPOTENTMINIMUM:
            return FuzzyUnitTnorm(UnitTnormExamples.__nilpotentminimum_tnorm)


    @staticmethod
    def __minimum_tnorm(x: float, y: float) -> float:
        """
        Implementation of the minimum tnorm.

        Args:
            x: A float, representing the first argument of the tnorm.
            y: A float, representing the second argument of the tnorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        return min(x, y)

    @staticmethod
    def __product_tnorm(x: float, y: float) -> float:
        """
        Implementation of the product tnorm.

        Args:
            x: A float, representing the first argument of the tnorm.
            y: A float, representing the second argument of the tnorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        return x*y

    @staticmethod
    def __lukasiewicz_tnorm(x: float, y: float) -> float:
        """
        Implementation of the lukasiewicz tnorm.

        Args:
            x: A float, representing the first argument of the tnorm.
            y: A float, representing the second argument of the tnorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        return max(x+y-1,0)

    @staticmethod
    def __drasticproduct_tnorm(x: float, y: float) -> float:
        """
        Implementation of the drastic product tnorm.

        Args:
            x: A float, representing the first argument of the tnorm.
            y: A float, representing the second argument of the tnorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        if 0 <= x < 1 and 0 <= y < 1:
            return 0
        else:
            return min(x, y)

    @staticmethod
    def __nilpotentminimum_tnorm(x: float, y: float) -> float:
        """
        Implementation of the drastic nilpotent minimum tnorm.

        Args:
            x: A float, representing the first argument of the tnorm.
            y: A float, representing the second argument of the tnorm.

        Returns:
            A float, representing the value of the tnorm in the point (x,y).
        """
        if x+y <= 1:
            return 0
        else:
            return min(x, y)
