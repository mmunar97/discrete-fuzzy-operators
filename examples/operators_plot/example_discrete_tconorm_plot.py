from discrete_fuzzy_operators.base.operators.binary_operators.discrete.fuzzy_discrete_binary_operator import DiscreteBinaryOperator
from discrete_fuzzy_operators.builtin_operators.discrete.tconorms import TconormExamples

if __name__ == "__main__":

    # EXAMPLE: Plot of some known t-conorms.
    lukasiewicz_operator = TconormExamples.get_tconorm(tconorm=TconormExamples.LUKASIEWICZ, n=5)
    #lukasiewicz_operator.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz t-conorm")
    lukasiewicz_operator.plot_three_dimensional_operator(draw_diagonal=True)

    # drastic_operator = TconormExamples.get_tconorm(tconorm=TconormExamples.DRASTIC, n=7)
    # drastic_operator.plot_operator(figure_size=(700, 700), figure_title="Drastic t-conorm")
    #
    # nilpotent_operator = TconormExamples.get_tconorm(tconorm=TconormExamples.NILPOTENT_MAXIMUM, n=7)
    # nilpotent_operator.plot_operator(figure_size=(700, 700), figure_title="Nilpotent maximum t-conorm")