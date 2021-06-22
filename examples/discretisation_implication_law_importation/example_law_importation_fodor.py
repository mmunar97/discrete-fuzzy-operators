from math import ceil, floor
from typing import Callable, Tuple
import numpy
import pandas


def lower_discretization(x: int, y: int, n: int, continuous_implication: Callable[[float, float], float]) -> int:
    return int(floor(n*continuous_implication(x/n, y/n)))


def upper_discretization(x: int, y: int, n: int, continuous_implication: Callable[[float, float], float]) -> int:
    return int(ceil(n*continuous_implication(x/n, y/n)))


def check_law_importation(tnorm_matrix: numpy.ndarray, n: int,
                          continuous_implication: Callable[[float, float], float],
                          discretization_method: int) -> Tuple[bool, pandas.DataFrame]:
    law_importation_summmary = pandas.DataFrame(columns=["N", "VERIFIED", "X", "Y", "Z",
                                                         "T(X,Y)", "N*I(T(X,Y)/N,Z/N)", "I_D(T(X,Y),Z)",
                                                         "N*I(Y/N, Z/N)", "I_D(Y,Z)", "N*I(X/N, I_D(Y,Z)/N)", "I_D(X,I_D(Y,Z))"])
    verified_law_importation = True

    if discretization_method == 1:
        discretization_method = lower_discretization
    else:
        discretization_method = upper_discretization

    for x in range(0, n+1):
        for y in range(0, n+1):
            for z in range(0, n+1):

                t_xy = tnorm_matrix[x, y]
                disc1 = n*continuous_implication(t_xy/n, z/n)
                left = discretization_method(x=tnorm_matrix[x, y], y=z, n=n, continuous_implication=continuous_implication)

                disc2 = n*continuous_implication(y/n, z/n)
                disc3 = discretization_method(x=y, y=z, n=n, continuous_implication=continuous_implication)
                disc4 = n*continuous_implication(x/n, disc3/n)
                right = discretization_method(x=x, y=discretization_method(x=y, y=z, n=n, continuous_implication=continuous_implication),
                                              n=n, continuous_implication=continuous_implication)

                if left != right:
                    law_importation_summmary.loc[len(law_importation_summmary)] = [n, False, x, y, z, t_xy, disc1, left, disc2, disc3, disc4, right]
                    verified_law_importation = False
                else:
                    law_importation_summmary.loc[len(law_importation_summmary)] = [n, True, x, y, z, t_xy, disc1, left,
                                                                                   disc2, disc3, disc4, right]
    return verified_law_importation, law_importation_summmary


def implication(x: float, y: float) -> float:
    # Fodor implication
    if x <= y:
        return 1
    else:
        return max(1-x, y)


def generate_nilpotent_minimum(n):
    mat = numpy.zeros((n+1, n+1), dtype=int)
    for x in range(0, n+1):
        for y in range(0, n+1):
            if x+y <= n:
                mat[y, x] = 0
            else:
                mat[y, x] = min(x, y)
    return mat


if __name__ == "__main__":

    saving_path = r"C:\Users\Usuario\OneDrive - Universitat de les Illes Balears\UIB\Tesi\Experiments\E4 (Python)\IMPLICATION=fodor_TNORM=nilpotentmin"

    for n in range(2, 91):
        nilpotent_minimum_matrix = generate_nilpotent_minimum(n)
        verifies_li, result = check_law_importation(tnorm_matrix=nilpotent_minimum_matrix,
                                                    n=n,
                                                    continuous_implication=implication,
                                                    discretization_method=1)

        result.to_csv(saving_path+f"/N={n}_VERIFIED={verifies_li}.txt", index=False)
