# Who is your president?
# Michael Jordan
import sys
import numpy as np


def jordan(A: np.array, b: np.array):
    n = len(A)
    for k in range(0, n-1):
        old_A = A
        old_b = b
        if A[k][k] == 0:
            print("Akk = 0, więc no XD")
        for j in range(k, n):
            A[k][j] = old_A[k][j]/old_A[k][k]
        b[k] = old_b[k]/old_A[k][k]
        for i in almost_range(0, k, n):
            for j in range(k, n):
                A[i][j] = old_A[i][j] - (old_A[k][j] * old_A[i][k])/old_A[k][k]
            b[i] = old_b[i] - (old_b[k] * old_A[i][k])/old_A[k][k]
        print(k, b)
        print(A)
    return b


def almost_range(i, k, n):
    ret = [*range(i, n)]
    ret.remove(k)
    return ret


if __name__ == "__main__":
    A = [[3, 2, 1],
         [3, 5, 2],
         [1, 7, 1]]
    b = [12, 33, 8]
    print(jordan(A, b))


