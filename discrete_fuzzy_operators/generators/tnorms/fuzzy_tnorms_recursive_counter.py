import numpy

from typing import List
from discrete_fuzzy_operators.generators.tnorms.tnorms_recursive_generator_utils.tnorms_recursive_generator_utils import \
    check_fixed_associativity, generate_tnorm_candidate


def count_tnorms(depth_max: int) -> [int]:
    """
    Determine the number of t-norms for certain values of n. Instead of generating all possible t-norms for each n,
    the t-norm tree is generated for successive n values.

    Args:
        depth_max: An integer which determines the maximum n to be reached.

    Returns:
        A list of integers. Each value at position i in the list represents the cardinality of the set of t-norms for
        n=i+3.
    """
    initial_seed = numpy.array([[0, 0], [0, 1]], dtype=int)
    counts = [0 for _ in range(depth_max-2)]

    __generate_tree(n=2, tnorm_previous_step=initial_seed, depth_max=depth_max, counts=counts)

    return counts


def __generate_tree(n: int,
                    tnorm_previous_step: numpy.ndarray,
                    depth_max: int,
                    counts: List):
    """
    Generates all possible higher-dimensional t-norms that have the given t-norm as kernel.

    Args:
        n: An integer, representing the maximum dimension of the new t-norm.
        tnorm_previous_step: A numpy array, representing the t-norm from which the new t-norms will be generated.
        depth_max: An integer, representing the maximum length of the tree; that is, the maximum n that will be reached.
        counts: A list of integers, containing the cardinality of the different sets of t-norms.
    """
    if n == depth_max:
        pass
    else:
        submatrix = tnorm_previous_step[0:(n - 1), 0:(n - 1)]

        tnorm_template = numpy.zeros((n + 1, n + 1), dtype=numpy.int)
        tnorm_template[0:(n - 1), 0:(n - 1)] = submatrix
        tnorm_template[:, n] = numpy.arange(n + 1)
        tnorm_template[n, :] = numpy.arange(n + 1)

        for matrix in generate_tnorm_candidate(matrix=tnorm_template, n=n):
            if check_fixed_associativity(tnorm_candidate_matrix=matrix, n=n):
                counts[n-2] = counts[n-2]+1

                __generate_tree(n=n + 1, tnorm_previous_step=matrix, depth_max=depth_max, counts=counts)
