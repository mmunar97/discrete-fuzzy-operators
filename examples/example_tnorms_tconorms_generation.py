"""
# IMPORT FOR ITERATIVE GENERATION
from discrete_fuzzy_operators.generators.tconorms.fuzzy_tconorms_generator import generate_tconorms_from_tnorms
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_iterative_generator import generate_tnorms
"""

# IMPORT FOR RECURSIVE GENERATION
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_recursive_generator import generate_tnorms

import numpy
import time
import os
import pandas


if __name__ == "__main__":

    r"""
    # EXAMPLE: Number of t-norms and t-conorms in L (size n) with additional properties.
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
    saving_path = "/home/marc/Escritorio/operators2"
    results_dataframe = pandas.DataFrame(columns=["N", "NUMBER_TNORMS", "ELAPSED_TIME"])

    initial_seed = [numpy.array([[0, 0], [0, 1]])]
    generation_limit = 80
    n = 1

    tnorms = initial_seed

    while n != generation_limit:
        t = time.time()
        new_generation = []

        for new_tnorm in generate_tnorms(n=n+1, tnorms_previous_step=tnorms):
            new_generation.append(new_tnorm)
        print(f"WITH N={n+1} THERE ARE {len(new_generation)} T-NORMS. ELAPSED TIME: {round(time.time()-t, 4)}")
        results_dataframe.loc[len(results_dataframe)] = [n, len(new_generation), round(time.time()-t, 4)]

        experiment_path = os.path.join(saving_path, f"N={n}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "tnorms.npy"), new_generation)
        results_dataframe.to_csv(saving_path+"/summary.txt", index=False)

        n = n+1
        tnorms = new_generation
