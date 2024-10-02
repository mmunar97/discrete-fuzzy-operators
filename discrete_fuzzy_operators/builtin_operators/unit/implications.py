from enum import Enum

from discrete_fuzzy_operators.base.operators.binary_operators.unit.suboperators.fuzzy_unit_implication_operator import \
    FuzzyUnitImplicationOperator


class UnitImplicationExamples(Enum):
    """
    Object that stores the values of the most known implications defined in [0, 1].
    """
    LUKASIEWICZ = "unit_lukasiewicz_implication"
    GODEL = "unit_godel_implication"
    REICHENBACH = "unit_reichenbach_implication"
    KLEENE_DIENES = "unit_kleenedienes_implication"
    GOGUEN = "unit_goguen_implication"
    RESCHER = "unit_rescher_implication"
    YAGER = "unit_yager_implication"
    WEBER = "unit_weber_implication"
    FODOR = "unit_fodor_implication"
    LEAST = "unit_least_implication"
    GREATEST = "unit_greatest_implication"

    @staticmethod
    def get_unit_implication(implication: "UnitImplicationExamples") -> FuzzyUnitImplicationOperator:
        """
        Returns a UnitImplicationExamples object representing the selected implication.

        Args:
            implication: A UnitImplicationExamples value, representing the chosen implication.

        Returns:
            A FuzzyUnitImplicationOperator object.
        """
        if implication == UnitImplicationExamples.LUKASIEWICZ:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__lukasiewicz_implication)
        elif implication == UnitImplicationExamples.GODEL:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__godel_implication)
        elif implication == UnitImplicationExamples.REICHENBACH:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__reichenbach_implication)
        elif implication == UnitImplicationExamples.KLEENE_DIENES:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__kleene_dienes_implication)
        elif implication == UnitImplicationExamples.GOGUEN:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__goguen_implication)
        elif implication == UnitImplicationExamples.RESCHER:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__rescher_implication)
        elif implication == UnitImplicationExamples.YAGER:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__yager_implication)
        elif implication == UnitImplicationExamples.WEBER:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__weber_implication)
        elif implication == UnitImplicationExamples.FODOR:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__fodor_implication)
        elif implication == UnitImplicationExamples.LEAST:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__least_implication)
        elif implication == UnitImplicationExamples.GREATEST:
            return FuzzyUnitImplicationOperator(UnitImplicationExamples.__greatest_implication)

    @staticmethod
    def __lukasiewicz_implication(x: float, y: float) -> float:
        """
        Implementation of the Lukasiewicz implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        return min(1.0, 1.0 - x + y)

    @staticmethod
    def __godel_implication(x: float, y: float) -> float:
        """
        Implementation of the Godel implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x <= y:
            return 1
        else:
            return y

    @staticmethod
    def __reichenbach_implication(x: float, y: float) -> float:
        """
        Implementation of the Reichenbach implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        return 1 - x + x * y

    @staticmethod
    def __kleene_dienes_implication(x: float, y: float) -> float:
        """
        Implementation of the Kleene-Dienes implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        return max(1.0 - x, y)

    @staticmethod
    def __goguen_implication(x: float, y: float) -> float:
        """
        Implementation of the Goguen implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x <= y:
            return 1
        else:
            return y / x

    @staticmethod
    def __rescher_implication(x: float, y: float) -> float:
        """
        Implementation of the Rescher implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x <= y:
            return 1
        else:
            return 0

    @staticmethod
    def __yager_implication(x: float, y: float) -> float:
        """
        Implementation of the Yager implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x == 0 and y == 0:
            return 1
        else:
            return y ** x

    @staticmethod
    def __weber_implication(x: float, y: float) -> float:
        """
        Implementation of the Weber implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x < 1:
            return 1
        else:
            return y

    @staticmethod
    def __fodor_implication(x: float, y: float) -> float:
        """
        Implementation of the Fodor implication.

        Args:
            x: A float, representing the first argument of the implication.
            y: A float, representing the second argument of the implication.

        Returns:
            A float, representing the value of the implication in the point (x,y).
        """
        if x <= y:
            return 1
        else:
            return max(1.0 - x, y)

    @staticmethod
    def __least_implication(x: float, y: float) -> float:
        """
        Implementation of the Least fuzzy implication.

        Args:
            x: A float, representing the first argument of the fuzzy implication.
            y: A float, representing the second argument of the fuzzy implication.

        Returns:
            A float, representing the value of the fuzzy implication in the point (x,y).
        """
        if x == 0 or y == 1:
            return 1
        else:
            return 0

    @staticmethod
    def __greatest_implication(x: float, y: float) -> float:
        """
        Implementation of the Greatest fuzzy implication.

        Args:
            x: A float, representing the first argument of the fuzzy implication.
            y: A float, representing the second argument of the fuzzy implication.

        Returns:
            A float, representing the value of the fuzzy implication in the point (x,y).
        """
        if x < 1 or y > 0:
            return 1
        else:
            return 0
