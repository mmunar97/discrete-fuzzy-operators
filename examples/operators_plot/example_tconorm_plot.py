from discrete_fuzzy_operators.builtin_operators.discrete.negations import get_negation, Negation
from discrete_fuzzy_operators.builtin_operators.discrete.tconorms import get_tconorm, Tconorm

if __name__ == "__main__":

    # EXAMPLE: Plot of some known t-conorms.
    lukasiewicz_operator = get_tconorm(tconorm=Tconorm.LUKASIEWICZ, n=7)
    lukasiewicz_operator.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz t-conorm")

    drastic_operator = get_tconorm(tconorm=Tconorm.DRASTIC, n=7)
    drastic_operator.plot_operator(figure_size=(700, 700), figure_title="Drastic t-conorm")

    nilpotent_operator = get_tconorm(tconorm=Tconorm.NILPOTENT_MAXIMUM, n=7)
    nilpotent_operator.plot_operator(figure_size=(700, 700), figure_title="Nilpotent maximum t-conorm")

    classic_negation = get_negation(negation=Negation.CLASSIC, n=8)
    classic_negation.plot_operator(figure_size=(700, 700))