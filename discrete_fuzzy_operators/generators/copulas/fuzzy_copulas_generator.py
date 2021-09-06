import itertools
import numpy
import os

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_suboperators.copula import \
    Copula
from typing import List, Tuple


def generate_copulas(n: int, save_results: bool, saving_path: str) -> Tuple[
                                                    List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray],
                                                    List[numpy.ndarray], List[numpy.ndarray]]:
    """
    Generates all possible copulas over a finite chain L={0,1,...,n}.

    Args:
        n: An integer, representing the size of the finite space where the copula is defined.
        save_results: A boolean, indicating if the results have to be saved in a file.
        saving_path: A string, representing the saving path where the results have to be saved.

    Returns:
        A tuple of four lists, each one containing numpy arrays.
    """
    copulas = []
    copulas_divisible = []
    copulas_commutatuve = []
    copulas_associative = []
    copulas_archimedean_divisible = []

    for permutation in itertools.permutations([x for x in range(1, n + 1)]):

        copula = Copula(n=n, permutation=list(permutation))

        copulas.append(copula.operator_matrix)
        if copula.is_divisible():
            copulas_divisible.append(copula.operator_matrix)

            if copula.is_archimedean():
                copulas_archimedean_divisible.append(copula.operator_matrix)

        if copula.is_commutative():
            copulas_commutatuve.append(copula.operator_matrix)

        if copula.is_associative():
            copulas_associative.append(copula.operator_matrix)

    if save_results:
        experiment_path = os.path.join(saving_path, f"N={n}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "copulas.npy"), copulas)
        numpy.save(os.path.join(experiment_path, "copulas_divisible.npy"), copulas_divisible)
        numpy.save(os.path.join(experiment_path, "copulas_commutatuve.npy"), copulas_commutatuve)
        numpy.save(os.path.join(experiment_path, "copulas_associative.npy"), copulas_associative)
        numpy.save(os.path.join(experiment_path, "copulas_archimedean_divisible.npy"), copulas_archimedean_divisible)

    return copulas, copulas_divisible, copulas_commutatuve, copulas_associative, copulas_archimedean_divisible
