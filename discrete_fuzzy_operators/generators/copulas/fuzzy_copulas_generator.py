import itertools
import numpy
import os

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import DiscreteFuzzyAggregationBinaryOperator

from typing import List, Tuple


def generate_copula_template(n: int) -> numpy.ndarray:
    """
    Generates an empty copula, win the sense of  only boundary conditions have been written.

    Args:
        n: The dimension of the matrix.

    Returns:
        A numpy array, representing the matrix.
    """
    operator_matrix = numpy.empty((n + 1, n + 1))
    operator_matrix[:] = 0

    operator_matrix[:, 0] = 0
    operator_matrix[0, :] = 0
    operator_matrix[:, n] = numpy.arange(0, n + 1)
    operator_matrix[n, :] = numpy.arange(0, n + 1)

    return operator_matrix.astype(int)


def generate_copulas(n: int, save_results: bool, saving_path: str) -> Tuple[
                                                    List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray],
                                                    List[numpy.ndarray], List[numpy.ndarray], List[numpy.ndarray]]:
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
    copulas_archimedean = []
    copulas_archimedean_divisible = []

    template = generate_copula_template(n)
    for kernel in itertools.product(numpy.arange(0, n + 1), repeat=(n - 1) * (n - 1)):

        matrix_kernel = numpy.array(kernel).reshape((n - 1, n - 1))

        operator_matrix = template.copy()
        operator_matrix[1:n, 1:n] = matrix_kernel

        operator = DiscreteFuzzyAggregationBinaryOperator(operator_matrix=operator_matrix)

        # The follwing condition filters for the operators that verifies the double boundary condition and the
        # two-increasing condition; that is, searches all the copulas.
        if operator.checks_double_boundary_condition() and operator.checks_two_increasing_condition():
            copulas.append(operator_matrix)

            if operator.is_divisible():
                copulas_divisible.append(operator_matrix)

                if operator.is_archimedean():
                    copulas_archimedean_divisible.append(operator_matrix)

            if operator.is_commutative():
                copulas_commutatuve.append(operator_matrix)

            if operator.is_associative():
                copulas_associative.append(operator_matrix)

            if operator.is_archimedean():
                copulas_archimedean.append(operator_matrix)

    if save_results:
        experiment_path = os.path.join(saving_path, f"N={n}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "copulas.npy"), copulas)
        numpy.save(os.path.join(experiment_path, "copulas_divisible.npy"), copulas_divisible)
        numpy.save(os.path.join(experiment_path, "copulas_commutatuve.npy"), copulas_commutatuve)
        numpy.save(os.path.join(experiment_path, "copulas_associative.npy"), copulas_associative)
        numpy.save(os.path.join(experiment_path, "copulas_archimedean.npy"), copulas_archimedean)
        numpy.save(os.path.join(experiment_path, "copulas_archimedean_divisible.npy"), copulas_archimedean_divisible)

    return copulas, copulas_divisible, copulas_commutatuve, copulas_associative, copulas_archimedean, \
           copulas_archimedean_divisible
