import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.fuzzy_discrete_binary_operator import \
    FuzzyDiscreteBinaryOperator
from discrete_fuzzy_operators.builtin_operators.discrete.tnorms import TnormExamples

if __name__ == "__main__":

    # EXAMPLE: Plot of some known t-norms.
    lukasiewicz_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.LUKASIEWICZ, n=7)
    lukasiewicz_operator.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz t-norm")
    lukasiewicz_operator.plot_three_dimensional_operator(draw_diagonal=True,
                                                         figure_size=(700, 700), figure_title="Lukasiewicz tensor")

    drastic_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.DRASTIC, n=7)
    drastic_operator.plot_operator(figure_size=(700, 700), figure_title="Drastic t-norm")

    nilpotent_operator = TnormExamples.get_tnorm(tnorm=TnormExamples.NILPOTENT_MINIMUM, n=7)
    nilpotent_operator.plot_operator(figure_size=(700, 700), figure_title="Nilpotent minimum t-norm")
