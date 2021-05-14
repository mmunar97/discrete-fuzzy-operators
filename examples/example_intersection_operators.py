from typing import Set

import numpy

if __name__ == "__main__":

    # EXAMPLE: Load the generated data as a set in order to be able to find intersections, unions and complements.
    def load_set(file_path: str) -> Set:
        example_operators = list(numpy.load(file_path))
        example_operators = [operator_matrix.flatten() for operator_matrix in example_operators]
        example_operators = {tuple(operator) for operator in example_operators}

        return example_operators

    root_path = r"Experiments\E1\N=4\\"

    copulas = load_set(file_path=root_path+"copulas.npy")
    copulas_associative = load_set(file_path=root_path+"copulas_associative.npy")
    copulas_commutative = load_set(file_path=root_path+"copulas_commutatuve.npy")
    copulas_divisible = load_set(file_path=root_path+"copulas_divisible.npy")
    copulas_archimedean = load_set(file_path=root_path+"copulas_archimedean.npy")
    copulas_archimedean_divisible = load_set(file_path=root_path+"copulas_archimedean.npy")

    tnorms = load_set(file_path=root_path+"tnorms.npy")
    tnorms_archimedean = load_set(file_path=root_path+"t_norms_archimedean.npy")
    tnorms_divisible = load_set(file_path=root_path+"t_norms_divisible.npy")



