from discrete_fuzzy_operators.builtin_operators.discrete.sheffer_stroke import ShefferStroke

if __name__ == "__main__":

    minimum_sheffer = ShefferStroke.get_sheffer_stroke(ShefferStroke.MIN, n=7)
    minimum_sheffer.plot_operator()