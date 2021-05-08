import os
from typing import List, Tuple

import numpy

from discrete_fuzzy_operators.base.fuzzy_operator import DiscreteFuzzyOperator
from discrete_fuzzy_operators.generators.tnorms.fuzzy_tnorms_generator import generate_candidate_tnorms


def generate_tconorms(n: int, save_results: bool, saving_path: str) -> Tuple[List, List, List, List]:
    """
    Generates all possible t-conorms over a finite chain L={0,1,...,n}. The t-conorms are constructed under the idea
    of duality with respect to the only strong discrete fuzzy negation: if T is a t-norm, S(x,y)=n-T(n-x,n-y) is a
    t-conorm.

    Args:
        n: An integer, representing the size of the finite space where the t-conorm is defined.
        save_results: A boolean, indicating if the results have to be saved in a file.
        saving_path: A string, representing the saving path where the results have to be saved.

    Returns:
        A tuple of four lists, each one containing numpy arrays. The tuples are returned in the following order:
            1. All possible t-conorms defined over L_n.
            2. The subset of divisible t-conorms.
            3. The subset of Archimedean t-conorms.
            4. The intersection of divisible and Archimedean sets of t-conorms.
    """
    t_conorms = []
    t_conorms_divisible = []
    t_conorms_archimedean = []
    t_conorms_archimedean_divisible = []

    for candidate_tnorm in generate_candidate_tnorms(n):

        t_conorm_matrix = convert_tnorm_tconorm(t_norm_matrix=candidate_tnorm, n=n)
        t_norm_operator = DiscreteFuzzyOperator(operator_matrix=candidate_tnorm)

        # All matrices generated by generate_candidate_tnorms are increasing, commutative and verifies the boundary
        # conditions. Indeed, only the associativity of the operator must be checked.
        if t_norm_operator.is_associative():
            t_conorms.append(t_conorm_matrix)

            if t_norm_operator.is_divisible():
                t_conorms_divisible.append(t_conorm_matrix)

                if t_norm_operator.is_archimedean():
                    t_conorms_archimedean_divisible.append(t_conorm_matrix)

            if t_norm_operator.is_archimedean():
                t_conorms_archimedean.append(t_conorm_matrix)

    if save_results:
        experiment_path = os.path.join(saving_path, f"N={n}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "tconorms.npy"), t_conorms)
        numpy.save(os.path.join(experiment_path, "t_conorms_divisible.npy"), t_conorms_divisible)
        numpy.save(os.path.join(experiment_path, "t_conorms_archimedean.npy"), t_conorms_archimedean)
        numpy.save(os.path.join(experiment_path, "t_conorms_archimedean_divisible.npy"), t_conorms_archimedean_divisible)

    return t_conorms, t_conorms_divisible, t_conorms_archimedean, t_conorms_archimedean_divisible


def convert_tnorm_tconorm(t_norm_matrix: numpy.ndarray, n: int) -> numpy.ndarray:
    """
    Converts a t-norm with its matrix expression given by t_norm_matrix into a t-conorm using the duality.

    Args:
        t_norm_matrix: A numpy array, representing the matrix expression of the t-norm.
        n: An integer, representing the size of the finite chain.

    Returns:
        A numpy array, representing the matrix expression of the dual t-conorm of the given t-norm.
    """
    return n-numpy.flip(numpy.flip(t_norm_matrix, 1), 0)
