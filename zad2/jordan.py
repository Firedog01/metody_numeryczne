# Who is your president?
# Michael Jordan
import sys

import numpy as np
from copy import deepcopy


def jordan(A: np.array, b: np.array):
    n = len(A)
    old_A = None
    for k in range(0, n-1):
        print(old_A)
        # Trzeba było zrobić deepcopy list, ale teraz wywala się xd
        old_A = deepcopy(A)
        old_b = deepcopy(b)
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
        print(A)
    return b


def almost_range(i, k, n):
    ret = [*range(i, n)]
    ret.remove(k)
    return ret

# Chyba to jest to i działa XDDD
# https://www.pythonpool.com/gaussian-elimination-python/
def jordan2(n, a, x):
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                print(i, j, k)
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    print('\nThe solution is: ')
    for i in range(n):
        print('X%d = %0.2f' % (i, x[i]), end='\t')


if __name__ == "__main__":
    A = [[3, 2, 1],
         [3, 5, 2],
         [1, 7, 1]]
    x = [12, 33, 8]
    a = [[3, 2, 1, 12],
         [3, 5, 2 , 33],
         [1, 7, 1, 8]]

    jordan2(3, a, x)

    print(jordan(A, x))


