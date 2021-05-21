import numpy
from typing import List

from discrete_fuzzy_operators.generators.tnorms.tnorms_recursive_generator_utils.tnorms_recursive_generator_utils import \
    generate_tnorm_candidate, check_fixed_associativity


def generate_tnorms(n: int, tnorms_previous_step: List[numpy.ndarray]) -> List[numpy.ndarray]:
    """
    Generates all possible t-norms over the finite chain L={0,1,...,n,n+1} from all the t-norms defined over the
    finite chain of size n.

    Given any t-norm T on L_{n}, all rows and columns are considered except the last row and column, representing the
    identity. Then, a new t-norm is created (represented in matrix expression) and only the penultimate column and row
    must be filled from the given t-norm.

    Args:
        n: An integer, representing the size of the chain where the given t-norms are defined.
        tnorms_previous_step: A list of numpy arrays, representing the set of all t-norms defined over the finite
                              chain of size n.

    Returns:
        A numpy array, representing the matrix expression of a t-norm.
    """
    for tnorm in tnorms_previous_step:
        submatrix = tnorm[0:(n-1), 0:(n-1)]

        tnorm_template = numpy.zeros((n + 1, n + 1), dtype=int)
        tnorm_template[0:(n - 1), 0:(n - 1)] = submatrix
        tnorm_template[:, n] = numpy.arange(n + 1)
        tnorm_template[n, :] = numpy.arange(n + 1)

        for matrix in generate_tnorm_candidate(matrix=tnorm_template, n=n):
            if check_fixed_associativity(tnorm_candidate_matrix=matrix, n=n):
                yield matrix
