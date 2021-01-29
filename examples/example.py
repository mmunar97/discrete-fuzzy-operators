from discrete_fuzzy_operators.base.fuzzy_operator import DiscreteFuzzyOperator
from discrete_fuzzy_operators.utils.fuzzy_implication_template_generator import generate_tnorms, generate_copulas

if __name__ == "__main__":

    """
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

    # EXAMPLE 2: Number of t-norms in L (size n) with properties
    saving_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E1"
    for n in range(2, 15):
        t_norms, t_norms_divisible, t_norms_archimedean, t_norms_archimedean_divisible = generate_tnorms(n=n, save_results=True, saving_path=saving_path)
        copulas, copulas_divisible, copulas_commutatuve, copulas_associative, copulas_archimedean, copulas_archimedean_divisible = generate_copulas(n=n, save_results=True, saving_path=saving_path)

        print(f"COMPUTING NUMBER OF FUZZY OPERATORS WITH n={n}")
        print(f"\t NUMBER OF T-NORMS: {len(t_norms)}")
        print(f"\t NUMBER OF DIVISIBLE T-NORMS: {len(t_norms_divisible)}")
        print(f"\t NUMBER OF ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean)}")
        print(f"\t NUMBER OF DIVISIBLE ARCHIMEDEAN T-NORMS: {len(t_norms_archimedean_divisible)}")
        print(f"\t NUMBER OF COPULAS: {len(copulas)}")
        print(f"\t NUMBER OF DIVISIBLE COPULAS: {len(copulas_divisible)}")
        print(f"\t NUMBER OF COMMUTATIVE COPULAS: {len(copulas_commutatuve)}")
        print(f"\t NUMBER OF ASSOCIATIVE COPULAS: {len(copulas_associative)}")
        print(f"\t NUMBER OF ARCHIMEDEAN COPULAS: {len(copulas_archimedean)}")
        print(f"\t NUMBER OF DIVISIBLE ARCHIMEDEAN COPULAS: {len(copulas_archimedean_divisible)}")


