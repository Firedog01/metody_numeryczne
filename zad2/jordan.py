# Who is your president?
# Michael Jordan
import sys

import numpy as np
from copy import deepcopy


def jordan(A: np.array, b: np.array):
    n = len(A)
    old_A = None
    for k in range(0, n - 1):
        print(old_A)
        # Trzeba było zrobić deepcopy list, ale teraz wywala się xd
        old_A = deepcopy(A)
        old_b = deepcopy(b)
        if A[k][k] == 0:
            print("Akk = 0, więc no XD")
        for j in range(k, n):
            A[k][j] = old_A[k][j] / old_A[k][k]
        b[k] = old_b[k] / old_A[k][k]
        for i in almost_range(0, k, n):
            for j in range(k, n):
                A[i][j] = old_A[i][j] - (old_A[k][j] * old_A[i][k]) / old_A[k][k]
            b[i] = old_b[i] - (old_b[k] * old_A[i][k]) / old_A[k][k]
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


def jordan3(a, b):
    n = len(b)
    for k in range(0, n):
        print(k)
        print(a, b)
        #a, b = find_main_elem(a, b)
        print(a, b)
        akk = a[k][k]
        for j in range(k, n):
            a[k][j] /= akk
        b[k] /= akk
        for i in almost_range(0, k, n):
            aik = a[i][k]  # cache a(k-1)[i][k]
            for j in range(k, n):
                a[i][j] -= a[k][j] * aik  # a[k][j] = a(k-1)[k][j] / a(k-1)[k][k]
            b[i] -= b[k] * aik  # b[k] = b(k-1)[k] / a[k][k]
        print(a, b)
    return b


def find_main_elem(a, b):
    n = len(b)
    j = 0
    while a[n - 1][j] == 0:
        j += 1
    for i in range(j, n):
        if abs(a[i][j]) > abs(a[j][j]):
            a[[i, j]] = a [[j, i]]
            b[[i, j]] = b [[j, i]]
    return a, b


if __name__ == "__main__":
    a = np.array([[2, 1, -2],
                  [4, -1, 2],
                  [1, 3, -4]])
    x = np.array([2, 10, 2])
    jordan3(a, x)
