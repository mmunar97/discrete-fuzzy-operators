from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_sheffer_stoke_operator import \
    DiscreteFuzzyShefferStrokeOperator
from discrete_fuzzy_operators.base.operators.unary_operators.suboperators.fuzzy_negation_operator import \
    DiscreteFuzzyNegation
from discrete_fuzzy_operators.builtin_operators.discrete.sheffer_stroke import ShefferStroke

import numpy

if __name__ == "__main__":

    minimum_sheffer = ShefferStroke.get_sheffer_stroke(ShefferStroke.MIN, n=7)
    minimum_sheffer.plot_operator()