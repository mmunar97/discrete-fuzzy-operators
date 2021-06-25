"""
# IMPORT FOR ITERATIVE GENERATION
from discrete_fuzzy_operators.generators.tconorms.fuzzy_tconorms_generator import generate_tconorms_from_tnorms
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_iterative_generator import generate_tnorms
"""

# IMPORT FOR RECURSIVE GENERATION
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_recursive_generator import generate_tnorms

import math
import numpy
import time
import os
import pandas

if __name__ == "__main__":

    r"""
    # EXAMPLE: Number of t-norms and t-conorms in L (size n) with additional properties generated iteratively.
    # WARNING: This program is computationally intensive for large n values.
    saving_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E3 (Python)"
    for n in range(2, 15):
        t_norms, t_norms_divisible, t_norms_archimedean, t_norms_archimedean_divisible = generate_tnorms(n=n, save_results=True, saving_path=saving_path)
        t_conorms, t_conorms_divisible, t_conorms_archimedean, t_conorms_archimedean_divisible = generate_tconorms_from_tnorms(t_norms=t_norms, n=n, save_results=True, saving_path=saving_path)

        print(f"COMPUTING NUMBER OF T-NORMS WITH n={n}")
        print(f"\t NUMBER OF T-NORMS: {len(t_norms)}")
        print(f"\t NUMBER OF DIVISIBLE T-NORMS: {len(t_norms_divisible)}")
        print(f"\t NUMBER OF ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean)}")
        print(f"\t NUMBER OF DIVISIBLE ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean_divisible)}")
    """

    # EXAMPLE: Number of t-norms and t-conorms in L (size n) generated recursively.
    # WARNING: This program is computationally intensive for large n values.
    saving_path = r"C:\Users\Usuario\Desktop\operators"
    tnorms_results_dataframe = pandas.DataFrame(columns=["N", "NUMBER_TNORMS", "ELAPSED_TIME"])
    non_associative_results_dataframe = pandas.DataFrame(columns=["N", "NUMBER_NON_ASSOCIATIVE", "ELAPSED_TIME"])

    initial_seed = [numpy.array([[0, 0], [0, 1]])]
    generation_limit = 80
    n = 1

    tnorms = initial_seed

    while n != generation_limit:
        t = time.time()
        new_generation = []
        non_associative = []

        for new_tnorm, is_associative in generate_tnorms(n=n+1, tnorms_previous_step=tnorms):
            if is_associative:
                new_generation.append(new_tnorm)
            else:
                non_associative.append(new_tnorm)
        print(f"WITH N={n+2} THERE ARE {len(new_generation)} T-NORMS. ELAPSED TIME: {round(time.time()-t, 4)}")
        tnorms_results_dataframe.loc[len(tnorms_results_dataframe)] = [n+2, len(new_generation), round(time.time()-t, 4)]
        non_associative_results_dataframe.loc[len(non_associative_results_dataframe)] = [n+2, len(non_associative), round(time.time()-t, 4)]

        experiment_path = os.path.join(saving_path, f"N={n+2}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "tnorms.npy"), new_generation)
        numpy.save(os.path.join(experiment_path, "non_associative.npy"), non_associative)

        tnorms_results_dataframe.to_csv(saving_path+"/summary_tnorms.txt", index=False)
        non_associative_results_dataframe.to_csv(saving_path + "/summary_non_associative.txt", index=False)

        n = n+1
        tnorms = new_generation
