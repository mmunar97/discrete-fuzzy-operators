from discrete_fuzzy_operators.generators.tconorms.fuzzy_tconorms_generator import generate_tconorms_from_tnorms
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_generator import generate_tnorms

if __name__ == "__main__":

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