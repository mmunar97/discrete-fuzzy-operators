from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_implication_operator import \
    DiscreteFuzzyImplicationOperator
from discrete_fuzzy_operators.builtin_operators.discrete.implications import DiscreteImplicationExamples

import math


def upper_implication(x: int, y: int, n: int) -> int:
    return math.ceil(n-x+(x*y)/n)


def lower_implication(x: int, y: int, n: int) -> int:
    return math.floor(n-x+(x*y)/n)


if __name__ == "__main__":

    # EXAMPLE: Plot of some known implications.
    lukasiewicz_implication = DiscreteImplicationExamples.get_discrete_implication(
        implication=DiscreteImplicationExamples.GODEL, n=8)
    #lukasiewicz_implication.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz implication")
    lukasiewicz_implication.plot_continuous_extension(figure_size=(900, 700),
                                                      figure_title="Lukasiewicz implication", show_contour=True)

    """
    largest_implication = DiscreteImplicationExamples.get_discrete_implication(implication=DiscreteImplicationExamples.LARGEST, n=8)
    largest_implication.plot_operator(figure_size=(700, 700), figure_title="Largest implication")

    godel_implication = DiscreteImplicationExamples.get_discrete_implication(implication=DiscreteImplicationExamples.GODEL, n=8)
    godel_implication.plot_operator(figure_size=(700, 700), figure_title="Godel implication")

    rescher_implication = DiscreteImplicationExamples.get_discrete_implication(implication=DiscreteImplicationExamples.RESCHER, n=8)
    rescher_implication.plot_operator(figure_size=(700, 700), figure_title="Rescher implication")

    weber_implication = DiscreteImplicationExamples.get_discrete_implication(implication=DiscreteImplicationExamples.WEBER, n=8)
    weber_implication.plot_operator(figure_size=(700, 700), figure_title="Weber implication")

    fodor_implication = DiscreteImplicationExamples.get_discrete_implication(implication=DiscreteImplicationExamples.FODOR, n=8)
    fodor_implication.plot_operator(figure_size=(700, 700), figure_title="Fodor implication")
    """