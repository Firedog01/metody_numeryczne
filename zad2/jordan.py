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


# TODO: sensownie nazwać xd
def is_nieoznaczony(a, b):
    lst = []
    for i in range(0, len(b)):
        lst.append(tuple(a[i] + [b[i]]))

    # Does matrix have duplicate rows?
    if len(set(lst)) != len(lst):
        print("safd")
        return True

    # Does matrix have 0 = 0 rows?
    for row in lst:
        result = all(element == row[0] for element in row)
        if result:
            return True
    return False


# TODO: nie wykrywa dla e)
def is_inconsistent(a, b):
    lst = []
    for i in range(0, len(b)):
        lst.append(tuple(a[i] + [b[i]]))

    # Does matrix have 0 = not 0 rows?
    for i in range(0, len(b)):
        result = all(element == a[i][0] for element in a[i])
        if result and b[i] != 0:
            return True
    return False


def jordan(a, b):
    n = len(b)
    for k in range(0, n):
        if is_nieoznaczony(a, b):
            return "Układ nieoznaczony!"
        if is_inconsistent(a, b):
            return "Układ sprzeczny!"
        print(k)
        print(a, b)
        a, b = find_main_elem(a, b, k)
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
        print(np.array(a), b)
    return b


if __name__ == "__main__":
    a = [[3, 2, 1, -1],
         [5, -1, 1, 2],
         [1, -1, 1, 2],
         [7, 8, 1, -7]]
    b = [0, -4, 4, 6]
    print("Wynik: ", jordan(a, b))
