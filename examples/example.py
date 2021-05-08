from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_generator import generate_tnorms

if __name__ == "__main__":

    r"""
    # EXAMPLE 1 : Check if Lukasiewicz and minimum t-norms verify some of the properties.
    lukasiewicz = numpy.array([[0, 0, 0, 0],
                               [0, 0, 0, 1],
                               [0, 0, 1, 2],
                               [0, 1, 2, 3]])
    minimum = numpy.array([[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 1, 2, 2],
                           [0, 1, 2, 3]])

    operator = DiscreteFuzzyOperator(operator_matrix=minimum)

    print(f"Annihilator: {operator.checks_annihilator_element(element=0)}")
    print(f"Boundary condition: {operator.checks_boundary_condition(element=3)}")
    print(f"Commutative: {operator.is_commutative()}")
    print(f"Associative: {operator.is_associative()}")
    print(f"Increasing: {operator.is_increasing()}")
    print(f"Smooth: {operator.is_smooth(step=1)}")
    print(f"Idempotent-free: {operator.is_idempotent_free()}")
    print(f"Divisible: {operator.is_divisible(tnorm_condition=True)}")
    print(f"Archimedean: {operator.is_archimedean(tnorm_condition=True, integer_limit=100)}")
    print(f"Lipschitz: {operator.is_lipschitz()}")
    print(f"2-increasing: {operator.checks_two_increasing_condition()}")
    """

    # EXAMPLE 2: Number of t-norms in L (size n) with additional properties.
    # WARNING: This program is computationally intensive for large n values.
    saving_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E3 (Python)"
    for n in range(2, 15):
        t_norms, t_norms_divisible, t_norms_archimedean, t_norms_archimedean_divisible = generate_tnorms(n=n, save_results=True, saving_path=saving_path)

        print(f"COMPUTING NUMBER OF T-NORMS WITH n={n}")
        print(f"\t NUMBER OF T-NORMS: {len(t_norms)}")
        print(f"\t NUMBER OF DIVISIBLE T-NORMS: {len(t_norms_divisible)}")
        print(f"\t NUMBER OF ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean)}")
        print(f"\t NUMBER OF DIVISIBLE ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean_divisible)}")

    r"""
    # EXAMPLE 3: Numer of copulas in L (size n) with additional properties.
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
    """

    r"""
    # EXAMPLE 4: Load the generated data as a set in order to be able to find intersections, unions and complements.
    def load_set(file_path: str) -> Set:
        operators = list(numpy.load(file_path))
        operators = [operator_matrix.flatten() for operator_matrix in operators]
        operators = {tuple(operator) for operator in operators}

        return operators

    root_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E1\N=4\\"

    copulas = load_set(file_path=root_path+"copulas.npy")
    copulas_associative = load_set(file_path=root_path+"copulas_associative.npy")
    copulas_commutative = load_set(file_path=root_path+"copulas_commutatuve.npy")
    copulas_divisible = load_set(file_path=root_path+"copulas_divisible.npy")
    copulas_archimedean = load_set(file_path=root_path+"copulas_archimedean.npy")
    copulas_archimedean_divisible = load_set(file_path=root_path+"copulas_archimedean.npy")

    tnorms = load_set(file_path=root_path+"tnorms.npy")
    tnorms_archimedean = load_set(file_path=root_path+"t_norms_archimedean.npy")
    tnorms_divisible = load_set(file_path=root_path+"t_norms_divisible.npy")
    """


