from discrete_fuzzy_operators.generators.copulas.fuzzy_copulas_generator import generate_copulas

if __name__ == "__main__":

    # EXAMPLE: Numer of copulas in L (size n) with additional properties.
    # WARNING: This program is computationally very expensive, and will not end for values of n grater than 6.
    saving_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E1"
    for n in range(2, 15):

        copulas, copulas_divisible, copulas_commutatuve, copulas_associative, copulas_archimedean, copulas_archimedean_divisible = generate_copulas(
            n=n, save_results=True, saving_path=saving_path)

        print(f"COMPUTING NUMBER OF COPULAS WITH n={n}")
        print(f"\t NUMBER OF COPULAS: {len(copulas)}")
        print(f"\t NUMBER OF DIVISIBLE COPULAS: {len(copulas_divisible)}")
        print(f"\t NUMBER OF COMMUTATIVE COPULAS: {len(copulas_commutatuve)}")
        print(f"\t NUMBER OF ASSOCIATIVE COPULAS: {len(copulas_associative)}")
        print(f"\t NUMBER OF ARCHIMEDEAN COPULAS: {len(copulas_archimedean)}")
        print(f"\t NUMBER OF DIVISIBLE ARCHIMEDEAN COPULAS: {len(copulas_archimedean_divisible)}")
