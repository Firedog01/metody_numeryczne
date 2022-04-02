# Who is your president?
# Michael Jordan
import numpy as np
from copy import deepcopy


def jordan(A: np.array, b: np.array):
    n = len(A)
    old_A = None
    for k in range(0, n):
        print(old_A)
        # Trzeba było zrobić deepcopy list, ale teraz wywala się xd
        old_A = deepcopy(A)
        old_b = deepcopy(b)
        print(old_A)
        if A[k][k] == 0:
            print("Akk = 0, więc no XD")
        for j in range(k, n):
            A[k][j] = old_A[k][j]/old_A[k][k]
        b[k] = old_b[k]/old_A[k][k]
        for i in almost_range(0, k, n):
            for j in range(k, n):
                A[i][j] = old_A[i][j] - (old_A[k][j] * old_A[i][k])/old_A[k][k]
            b[i] = old_b[i] - (old_b[k] * old_A[i][k])/old_A[k][k]
            print(old_b[i], old_b[k], old_A[i][k], old_A[k][k])
        print("---------")
        # print(k, b)
        # print(A)
    return b


def almost_range(i, k, n):
    ret = [*range(i, n)]
    ret.remove(k)
    return ret


if __name__ == "__main__":
    A = [[1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]]
    b = [3, 6, 9]
    print(jordan(A, b))


