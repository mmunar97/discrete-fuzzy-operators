import numpy
from numba import jit


def generate_tnorm_candidate(matrix: numpy.ndarray, n: int, recursive_step: int = 1) -> numpy.ndarray:
    """
    Generates all possible matrices which are candidates to be t-norms filling the penultimate row and column.

    Args:
        matrix: A numpy array, representing the matrix of the t-norm.
        n: An integer, representing the size of the finite chain where the t-norm is defined.
        recursive_step: An integer, representing the step of recursion and, therefore, the row/column that is being +
                        filled.

    Returns:
        A numpy array, representing the filled matrix which is candidate to be a t-norm. Is an increasing and symmetric
        matrix.
    """
    if recursive_step == n:
        yield matrix
    else:
        if recursive_step == n - 1:
            for i in range(matrix[recursive_step - 1, n - 1], matrix[recursive_step, n] + 1):
                candidate_matrix = matrix.copy()
                candidate_matrix[recursive_step, n - 1] = i
                candidate_matrix[n - 1, recursive_step] = i
                yield from generate_tnorm_candidate(matrix=candidate_matrix, n=n, recursive_step=recursive_step + 1)
        else:
            for i in range(max(matrix[recursive_step, n - 2], matrix[recursive_step - 1, n - 1]),
                           matrix[recursive_step, n] + 1):
                candidate_matrix = matrix.copy()
                candidate_matrix[recursive_step, n - 1] = i
                candidate_matrix[n - 1, recursive_step] = i
                yield from generate_tnorm_candidate(matrix=candidate_matrix, n=n, recursive_step=recursive_step + 1)


@jit
def check_fixed_associativity(tnorm_candidate_matrix: numpy.ndarray, n: int) -> bool:
    """
    Verifies if the new matrix is associative, only checking the associativity in the new row/column of the matrix,
    which is the penultimate row/column. The other rows/columns of the matrix not need to be checked since they come
    from a t-norm and hence associative. For this reason, check the associativity only needs a quadratic complexity.

    Args:
        tnorm_candidate_matrix: A numpy array, representing the new expression of the t-norm.
        n: An integer, representing the size of the finite chain where the new t-norm is defined.

    Returns:

    """
    for x in range(0, n + 1):
        for y in range(0, n + 1):
            if not tnorm_candidate_matrix[x, tnorm_candidate_matrix[n - 1, y]] == tnorm_candidate_matrix[n - 1, tnorm_candidate_matrix[x, y]]:
                return False
    return True
