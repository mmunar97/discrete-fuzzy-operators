from enum import Enum


# region Declaration of some implications
class ContinuousImplication(Enum):
    """
    Object that stores the values of the most known implications defined in [0, 1]^2.

    Note: Although the name of the object is ContinuousImplication, it does not mean that the defined implications are
          continuous functions. The name is taken to differentiate them from discrete implication functions.
    """
    LUKASIEWICZ = "continuous_lukasiewicz_implication"
    GODEL = "continuous_godel_implication"
    REICHENBACH = "continous_reichenbach_implication"
    KLEENE_DIENES = "continous_kleenedienes_implication"
    GOGUEN = "continuous_goguen_implication"
    RESCHER = "continuous_rescher_implication"
    YAGER = "continuous_yager_implication"
    WEBER = "continuous_weber_implication"
    FODOR = "continuous_fodor_implication"
# endregion

# region Implications
def get_continuous_implication(implication: ContinuousImplication, n: int):
    """
    Returns a DiscreteFuzzyImplicationOperator object representing the selected implication.

    Args:
        implication: An DiscreteImplication value, representing the chosen implication.
        n: An integer, representing the dimension of the domain where the t-norm is defined.

    Returns:
        A DiscreteFuzzyImplicationOperator object.
    """
    pass



# endregion
