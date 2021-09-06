import numpy

from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_recursive_generator import generate_tnorms


import time
import pandas

if __name__ == "__main__":

    # EXAMPLE: Generation of t-norms and t-conorms in L (size n) generated recursively.
    # WARNING: This program is computationally intensive for large n values (n>15).
    saving_path = r"C:\Users\Usuario\Desktop\operators"
    tnorms_results_dataframe = pandas.DataFrame(columns=["N", "NUMBER_TNORMS", "ELAPSED_TIME"])
    non_associative_results_dataframe = pandas.DataFrame(columns=["N", "NUMBER_NON_ASSOCIATIVE", "ELAPSED_TIME"])

    initial_seed = [numpy.array([[0, 0],
                                 [0, 1]])]
    generation_limit = 80
    n = 5

    tnorms = initial_seed

    while n != generation_limit:
        t = time.time()
        new_generation = []

        for new_tnorm, is_associative in generate_tnorms(n=n + 1, tnorms_previous_step=tnorms):
            if is_associative:
                new_generation.append(new_tnorm)

        print(f"WITH N={n + 2} THERE ARE {len(new_generation)} T-NORMS. ELAPSED TIME: {round(time.time() - t, 4)}")

        n = n + 1
        tnorms = new_generation