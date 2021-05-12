import numpy
import os

from discrete_fuzzy_operators.base.fuzzy_aggregation_operator import DiscreteFuzzyAggregationOperator
from discrete_fuzzy_operators.generators.tnorms.tnorms_generator_utils.tnorms_generator_utils import generate_increasing_rows, \
    generate_symmetric_matrix
from typing import List, Tuple


def generate_tnorms(n: int, save_results: bool, saving_path: str) -> Tuple[List, List, List, List]:
    """
    Generates all possible t-norms over a finite chain L={0,1,...,n}.

    Args:
        n: An integer, representing the size of the finite space where the t-norm is defined.
        save_results: A boolean, indicating if the results have to be saved in a file.
        saving_path: A string, representing the saving path where the results have to be saved.

    Returns:
        A tuple of four lists, each one containing numpy arrays. The tuples are returned in the following order:
            1. All possible t-norms defined over L_n.
            2. The subset of divisible t-norms.
            3. The subset of Archimedean t-norms.
            4. The intersection of divisible and Archimedean sets of t-norms.
    """
    t_norms = []
    t_norms_divisible = []
    t_norms_archimedean = []
    t_norms_archimedean_divisible = []

    for candidate_tnorm in generate_candidate_tnorms(n):

        operator = DiscreteFuzzyAggregationOperator(operator_matrix=candidate_tnorm)

        # All matrices generated by generate_candidate_tnorms are increasing, commutative and verifies the boundary
        # conditions. Indeed, only the associativity of the operator must be checked.
        if operator.is_associative():
            t_norms.append(candidate_tnorm)

            if operator.is_divisible():
                t_norms_divisible.append(candidate_tnorm)

                if operator.is_archimedean():
                    t_norms_archimedean_divisible.append(candidate_tnorm)

            if operator.is_archimedean():
                t_norms_archimedean.append(candidate_tnorm)

    if save_results:
        experiment_path = os.path.join(saving_path, f"N={n}")
        if not os.path.exists(experiment_path):
            os.mkdir(experiment_path)

        numpy.save(os.path.join(experiment_path, "tnorms.npy"), t_norms)
        numpy.save(os.path.join(experiment_path, "t_norms_divisible.npy"), t_norms_divisible)
        numpy.save(os.path.join(experiment_path, "t_norms_archimedean.npy"), t_norms_archimedean)
        numpy.save(os.path.join(experiment_path, "t_norms_archimedean_divisible.npy"), t_norms_archimedean_divisible)

    return t_norms, t_norms_divisible, t_norms_archimedean, t_norms_archimedean_divisible


def generate_candidate_tnorms(n: int, recursive_step: int = 1, matrix: List[List] = None) -> numpy.ndarray:
    """
    Generates all possible matrices which represent a t-norm, in terms of increasingness and symmetry. Associativity
    must be checked.

    Args:
        n: An integer, representing the size of the finite chain.
        recursive_step: An integer, representing the number of recursive calls and also the row where the possibilities
                        are being computed.
        matrix: A list of lists, containing the possibilities of rows.

    Returns:
        A numpy array, representing the matrix representation of a candidate to be a t-norm.
    """
    if matrix is None:
        matrix = []

    if recursive_step == n:
        # In this last step, matrix contains the final list of lists, each of them representing the row of the matrix.
        # The list of lists is converted into a symmetric matrix.
        yield generate_tnorm_matrix(n=n, inner_matrix=matrix)
    else:
        previous_row = []
        if matrix != []:
            previous_row = matrix[-1]
        for row in generate_increasing_rows(previous_row=previous_row, min_value=0, max_value=recursive_step,
                                            max_vector_size=n - recursive_step):
            mat1 = matrix.copy()
            mat1.append(row)

            previous_row = row

            yield from generate_candidate_tnorms(n, recursive_step + 1, mat1)


def generate_tnorm_matrix(n: int, inner_matrix: List[List]) -> numpy.ndarray:
    """
    Generates the matrix representation of a t-norm. It must be symmetric, with boundary conditions T(x,0)=0 and
    T(x,n)=n for all x.

    Args:
        n: The size of the finite chain.
        inner_matrix: A list of lists, containing the rows of the inner matrix (without the boundary conditions).

    Returns:
        A numpy array, representing the matrix representation of a candidate to be a t-norm.
    """
    tnorm = numpy.zeros((n+1, n+1), dtype=numpy.int)
    tnorm[:, n] = numpy.arange(0, n + 1)
    tnorm[n, :] = numpy.arange(0, n + 1)

    tnorm[1:n, 1:n] = generate_symmetric_matrix(inner_matrix)
    return tnorm