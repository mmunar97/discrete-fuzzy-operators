from discrete_fuzzy_operators.example_operators.tnorms import get_tnorm, Tnorm

if __name__ == "__main__":

    # EXAMPLE: Plot of some known t-norms.
    lukasiewicz_operator = get_tnorm(tnorm=Tnorm.LUKASIEWICZ, n=7)
    lukasiewicz_operator.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz t-norm")

    drastic_operator = get_tnorm(tnorm=Tnorm.DRASTIC, n=7)
    drastic_operator.plot_operator(figure_size=(700, 700), figure_title="Drastic t-norm")

    nilpotent_operator = get_tnorm(tnorm=Tnorm.NILPOTENT_MINIMUM, n=7)
    nilpotent_operator.plot_operator(figure_size=(700, 700), figure_title="Nilpotent minimum t-norm")
