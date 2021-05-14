from discrete_fuzzy_operators.example_operators.implications import get_implication, Implication

if __name__ == "__main__":

    # EXAMPLE: Plot of some known implications.
    largest_implication = get_implication(implication=Implication.LARGEST, n=8)
    largest_implication.plot_operator(figure_size=(700, 700), figure_title="Largest implication")

    lukasiewicz_implication = get_implication(implication=Implication.LUKASIEWICZ, n=8)
    lukasiewicz_implication.plot_operator(figure_size=(700, 700), figure_title="Lukasiewicz implication")

    godel_implication = get_implication(implication=Implication.GODEL, n=8)
    godel_implication.plot_operator(figure_size=(700, 700), figure_title="Godel implication")

    rescher_implication = get_implication(implication=Implication.RESCHER, n=8)
    rescher_implication.plot_operator(figure_size=(700, 700), figure_title="Rescher implication")

    weber_implication = get_implication(implication=Implication.WEBER, n=8)
    weber_implication.plot_operator(figure_size=(700, 700), figure_title="Weber implication")

    fodor_implication = get_implication(implication=Implication.FODOR, n=8)
    fodor_implication.plot_operator(figure_size=(700, 700), figure_title="Fodor implication")
