import math
import numpy
from typing import List, Tuple

from discrete_fuzzy_operators.generators.tnorms.tnorms_recursive_generator_utils.tnorms_recursive_generator_utils import \
    generate_tnorm_candidate, check_fixed_associativity


def generate_tnorms(n: int, tnorms_previous_step: List[numpy.ndarray]) -> Tuple[numpy.ndarray, bool]:
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
        A numpy array, representing the matrix expression of a t-norm and a boolean, representing if the operator
        is associative.
    """
    for tnorm in tnorms_previous_step:
        submatrix = tnorm[0:(n-1), 0:(n-1)]

        tnorm_template = numpy.zeros((n + 1, n + 1), dtype=numpy.byte)
        tnorm_template[0:(n - 1), 0:(n - 1)] = submatrix
        tnorm_template[:, n] = numpy.arange(n + 1)
        tnorm_template[n, :] = numpy.arange(n + 1)

        for matrix in generate_tnorm_candidate(matrix=tnorm_template, n=n):
            if check_fixed_associativity(tnorm_candidate_matrix=matrix, n=n):
                yield matrix, True
            else:
                yield matrix, False


def generate_tnorms_from_codification(n: int, encoded_tnorms_previous_step: List[numpy.ndarray]) -> Tuple[numpy.ndarray, bool]:
    """
    Generates all possible t-norms over the finite chain L={0,1,...,n,n+1} from all the t-norms defined over the
    finite chain of size n.

    Given any t-norm T on L_{n}, all rows and columns are considered except the last row and column, representing the
    identity. Then, a new t-norm is created (represented in matrix expression) and only the penultimate column and row
    must be filled from the given t-norm.

    Args:
        n: An integer, representing the size of the chain where the given t-norms are defined.
        encoded_tnorms_previous_step: A list of numpy arrays, representing the set of all t-norms defined over the finite
                              chain of size n and its matrix expression is codified.

    Returns:
        A numpy array, representing the matrix expression of a t-norm.
    """
    for codified_tnorm in encoded_tnorms_previous_step:
        tnorm = decode_tnorm(codified_tnorm)
        submatrix = tnorm[0:(n-1), 0:(n-1)]

        tnorm_template = numpy.zeros((n + 1, n + 1), dtype=numpy.byte)
        tnorm_template[0:(n - 1), 0:(n - 1)] = submatrix
        tnorm_template[:, n] = numpy.arange(n + 1)
        tnorm_template[n, :] = numpy.arange(n + 1)

        for matrix in generate_tnorm_candidate(matrix=tnorm_template, n=n):
            if check_fixed_associativity(tnorm_candidate_matrix=matrix, n=n):
                yield matrix, True
            else:
                yield matrix, False


def encode_matrix(matrix: numpy.ndarray) -> numpy.ndarray:
    """
    Converts a symmetric matrix into a one-dimensional vector, considering only the upper triangle part. In addition,
    since "matrix" represents the matrix representation of a symmetric operator with boundary conditions, only the inner
    matrix is considered.

    Args:
        matrix: A numpy array, representing the matrix representation of the operator.

    Returns:
        A numpy array, representing the one-dimensional codification of the given matrix.
    """
    shape = matrix.shape
    submatrix = matrix[1:shape[0]-1, 1:shape[1]-1]
    return submatrix[numpy.triu_indices(submatrix.shape[0], k=0)]


def decode_tnorm(codified_matrix: numpy.ndarray) -> numpy.ndarray:
    """
    Converts a one-dimensional vector into its matrix expression. "codified_matrix" contains the upper part of the
    original matrix converted into vector. Since in the conversion the length of the vector is (n-1)*n/2=l, n can be
    computed from that expression.

    Args:
        codified_matrix: A one dimensional matrix, containing the vector representation.

    Returns:

    """
    l = codified_matrix.shape[0]
    n = int((-1+math.sqrt(1+8*l))/2)

    matrix = numpy.zeros((n, n))
    matrix[numpy.triu_indices(matrix.shape[0], k=0)] = codified_matrix
    matrix = matrix + matrix.T - numpy.diag(numpy.diag(matrix))

    final_matrix = numpy.zeros((n+2, n+2), dtype=numpy.byte)
    final_matrix[1:n+1, 1:n+1] = matrix
    final_matrix[:, n+1] = numpy.arange(n + 2)
    final_matrix[n+1, :] = numpy.arange(n + 2)
    return final_matrix