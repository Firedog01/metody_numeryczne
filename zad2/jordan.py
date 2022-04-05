# Who is your president?
# Michael Jordan
from util import *


def find_main_elem(a, b, j):
    n = len(b)
    for i in range(j, n):
        if abs(a[i][j]) > abs(a[j][j]):
            swap_pos(a, i, j)
            swap_pos(b, i, j)
    return a, b


def is_nieoznaczony(a, b):
    n = len(b)
    for i in range(0, n):
        round_row = [round(a[i][j], 10) for j in range(0, n)] + [round(b[i])]
        if set(round_row) == {0}:
            return True
    return False


def is_inconsistent(a, b):
    n = len(b)
    for i in range(0, n):
        round_row = [round(a[i][j], 10) for j in range(0, n)]
        if set(round_row) == {0} and b[i] != 0:
            return True
    return False


def jordan(a, b, verbose=False):
    n = len(b)
    for k in range(0, n):
        a, b = find_main_elem(a, b, k)
        if is_nieoznaczony(a, b):
            return "Układ nieoznaczony!"
        if is_inconsistent(a, b):
            return "Układ sprzeczny!"

        # For k-row
        akk = a[k][k]
        for j in range(k, n):
            a[k][j] /= akk
        b[k] /= akk

        # For other rows
        for i in almost_range(0, k, n):
            aik = a[i][k]  # cache a(k-1)[i][k]
            for j in range(k, n):
                a[i][j] -= a[k][j] * aik  # a[k][j] = a(k-1)[k][j] / a(k-1)[k][k]
            b[i] -= b[k] * aik  # b[k] = b(k-1)[k] / a[k][k]

        if verbose:
            print("Dla k =", k, ":")
            print("A:\n", np.array(a))
            print("b:", b)
    return b
