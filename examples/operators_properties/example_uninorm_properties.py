import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_suboperators.uninorm import \
    Uninorm
from discrete_fuzzy_operators.builtin_operators.discrete.tconorms import TconormExamples
from discrete_fuzzy_operators.builtin_operators.discrete.tnorms import TnormExamples

if __name__ == "__main__":

    n = 7
    e = 3
    lukasiewicz_tnorm = TnormExamples.get_tnorm(TnormExamples.LUKASIEWICZ, n=e)
    maximum_tconorm = TconormExamples.get_tconorm(TconormExamples.MAXIMUM, n=n-e)

    # Left compensation mapping
    lcm = numpy.ndarray(shape=(n-e, e), dtype=int)
    for x in range(0, e):
        for y in range(e, n):
            lcm[y-e, x] = min(x, y)
    # Right compensation mapping
    rcm = numpy.ndarray(shape=(e, n-e), dtype=int)
    for x in range(e, n):
        for y in range(0, e):
            rcm[y, x-e] = min(x, y)

    uninorm = Uninorm(n=n, e=e, operator_components={"TNORM": lukasiewicz_tnorm.operator_matrix,
                                                     "TCONORM": maximum_tconorm.operator_matrix+e,
                                                     "CE_LEFT": lcm,
                                                     "CE_RIGHT": rcm})
    uninorm.plot_operator(figure_size=(900, 600))
