import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.discrete.suboperators.fuzzy_discrete_aggregation_operator import \
    DiscreteAggregationBinaryOperator

if __name__ == "__main__":

    # EXAMPLE: Check if Lukasiewicz and minimum t-norms verify some of the properties.
    lukasiewicz = numpy.array([[0, 0, 0, 0],
                               [0, 0, 0, 1],
                               [0, 0, 1, 2],
                               [0, 1, 2, 3]])
    minimum = numpy.array([[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 1, 2, 2],
                           [0, 1, 2, 3]])

    operator = DiscreteAggregationBinaryOperator(n=3, operator_matrix=minimum)

    print(f"Annihilator: {operator.checks_annihilator_element(element=0)}")
    print(f"Boundary condition: {operator.checks_boundary_condition(element=3)}")
    print(f"Commutative: {operator.is_commutative()}")
    print(f"Associative: {operator.is_associative()}")
    print(f"Increasing: {operator.is_increasing()}")
    print(f"Smooth: {operator.is_smooth(step=1)}")
    print(f"Idempotent-free: {operator.is_idempotent_free()}")
    print(f"Divisible: {operator.is_divisible(tnorm_condition=True)}")
    print(f"Archimedean: {operator.is_archimedean(tnorm_condition=True, integer_limit=100)}")
    print(f"Lipschitz: {operator.is_lipschitz()}")
    print(f"2-increasing: {operator.checks_two_increasing_condition()}")