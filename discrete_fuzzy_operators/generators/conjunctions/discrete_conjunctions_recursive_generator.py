import numpy

from discrete_fuzzy_operators.base.generators.discrete_operator_generator import DiscreteOperatorGenerator
from typing import Generator, List


class DiscreteConjunctionsRecursiveGenerator(DiscreteOperatorGenerator):

    def __init__(self, n: int):
        """
        Initializes the object that generates all possible discrete conjunctions over the finite chain Ln.

        Args:
            n: An integer, representing the dimension of the finite chain.
        """
        super(DiscreteConjunctionsRecursiveGenerator, self).__init__(n)
        self.n = n

    def generate_operators(self) -> Generator:
        """
        Generates recursively all possible discrete conjunctions defined over the finite chain Ln.

        Returns:
            A Generator of numpy arrays, representing the object that recursively generates all possible conjunctions.
        """
        return self.__recursive_conjunction_generator(n=self.n)

    @staticmethod
    def __recursive_conjunction_generator(n: int, k: int = 1, previous_conjunction_matrix: numpy.ndarray = None) -> Generator[numpy.ndarray, None, None]:
        """
        Generates all possible matrices which are increasing in each direction and whose elements are taken from the finite
        chain Ln, and also satisfy that the first row and column are zeros and the last element in the diagonal is equal
        to n; that is, generates all possible matrix representations of a discrete conjunction.

        Args:
            n: An integer, representing the size of the finite chain where the conjunctions are defined.
            k: An integer, representing the recursive step.
            previous_conjunction_matrix: A numpy array, representing the temporal matrix which is candidate
                                        to be a conjunction.

        Returns:
            A Generator of numpy arrays, representing the object that recursively generates all possible conjunctions.
        """
        if previous_conjunction_matrix is None:
            previous_conjunction_matrix = numpy.zeros(shape=(n + 1, n + 1), dtype=int)
            previous_conjunction_matrix[n, n] = n

        if n == 1:
            yield previous_conjunction_matrix
        else:
            if k == 1:
                for w in range(0, n + 1):
                    conjunction_matrix = previous_conjunction_matrix.copy()
                    conjunction_matrix[k, k] = w

                    yield from DiscreteConjunctionsRecursiveGenerator.__recursive_conjunction_generator(n=n, k=k + 1, previous_conjunction_matrix=conjunction_matrix)

            elif k == 2:
                restrictions_column = [previous_conjunction_matrix[1, 1]]
                restrictions_row = [previous_conjunction_matrix[1, 1]]

                for increasing_vector_row in DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=0, n=n,
                                                                                                                            restrictions=restrictions_row):
                    for increasing_vector_column in DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=0, n=n,
                                                                                                                                   restrictions=restrictions_column):
                        next_step_conjunction_template = previous_conjunction_matrix.copy()

                        next_step_conjunction_template[k - 1:k, k] = increasing_vector_column
                        next_step_conjunction_template[k, k - 1:k] = increasing_vector_row

                        if k < n:
                            lower_bound = max(max(increasing_vector_row), max(increasing_vector_column))
                            for w in range(lower_bound, n + 1):
                                next_step_conjunction = next_step_conjunction_template.copy()
                                next_step_conjunction[k, k] = w

                                yield from DiscreteConjunctionsRecursiveGenerator.__recursive_conjunction_generator(n=n, k=k + 1, previous_conjunction_matrix=next_step_conjunction)
                        else:
                            yield next_step_conjunction_template

            else:
                restrictions_column = previous_conjunction_matrix[1:k, k - 1]
                restrictions_row = previous_conjunction_matrix[k - 1, 1:k]

                for increasing_vector_row in DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=0, n=n,
                                                                                                                            restrictions=restrictions_row):
                    for increasing_vector_column in DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=0, n=n,
                                                                                                                                   restrictions=restrictions_column):
                        next_step_conjunction_template = previous_conjunction_matrix.copy()

                        next_step_conjunction_template[1:k, k] = increasing_vector_column
                        next_step_conjunction_template[k, 1:k] = increasing_vector_row

                        if k < n:
                            lower_bound = max(max(increasing_vector_row), max(increasing_vector_column))
                            for w in range(lower_bound, n + 1):
                                next_step_conjunction = next_step_conjunction_template.copy()
                                next_step_conjunction[k, k] = w

                                yield from DiscreteConjunctionsRecursiveGenerator.__recursive_conjunction_generator(n=n, k=k + 1,
                                                                                                                    previous_conjunction_matrix=next_step_conjunction)
                        else:
                            yield next_step_conjunction_template

    @staticmethod
    def __recursive_increasing_vector_generator(position: int, n: int, restrictions: List[int], vector: List[int] = None) -> Generator[List[int], None, None]:
        """
        From a given list of restrictions, constructs all possible vectors of length n such that are increasing and each
        component is less than or equal to the restriction at the same index.

        The increasing vectors are generated using the recurrence established by M. Munar et al.

        Args:
            position: An integer, representing the type of expression to be used in the generation of the vectors.
            n: An integer, representing the maximum size of the vector to be generated.
            restrictions: A list of integers, representing the upper restrictions to consider while positioning the elements
                          of the generated vector.
            vector: A list of integers, representing the temporal vector to be yield at the end of the process. Is a vector
                    whose elements are taken from the finite chain Ln, it is increasing and satisfies the restrictions given
                    by "restrictions".

        Returns:
            A generator object, which generates lists of increasing integers.
        """
        if vector is None:
            vector = [0] * (len(restrictions))

        if position == 0:
            for x in range(restrictions[0], n + 1):
                temp_vec = vector.copy()
                temp_vec[0] = x

                if len(vector) == 1:
                    yield temp_vec
                else:
                    yield from DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=position + 1, n=n,
                                                                                                              restrictions=restrictions, vector=temp_vec)
        elif 1 <= position < len(restrictions) - 1:
            for x in range(max(restrictions[position], vector[position - 1]), n + 1):
                temp_vec = vector.copy()
                temp_vec[position] = x

                yield from DiscreteConjunctionsRecursiveGenerator.__recursive_increasing_vector_generator(position=position + 1, n=n,
                                                                                                          restrictions=restrictions, vector=temp_vec)
        elif position == len(restrictions) - 1:
            for x in range(max(restrictions[position], vector[position - 1]), n + 1):
                vector[len(restrictions) - 1] = x
                yield vector
