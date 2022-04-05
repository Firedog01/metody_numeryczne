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


# TODO: wip, nazwa xd
def is_nieoznaczony(a, b, k):
    lst = []
    n = len(b)
    for i in range(0, n):
        lst.append(tuple(a[i] + [b[i]]))
    for i in range(k, n):
        for j in range(i+1, n):
            div_row = []
            for p in range(k, n+1):
                if lst[j][p] != 0:
                    div_row.append(lst[i][p]/lst[j][p])
            if len(div_row) > 2 and len(set(div_row)) <= 1:
                print("Duplicate!")
                return True
    return False


# TODO: wip
def is_inconsistent(a, b, k):
    n = len(b)
    lst = []
    for i in range(0, n):
        lst.append(tuple(a[i] + [b[i]]))

    for i in range(k, n):
        for j in range(i+1, n):
            div_row = []
            for p in range(k, n+1):
                if lst[j][p] != 0:
                    div_row.append(lst[i][p]/lst[j][p])
            if len(div_row) > 2 and len(set(div_row[:-1])) <= 1 and div_row[0] != div_row[-1]:
                print("Inconsistance!")
                return True

    return False


def jordan(a, b):
    n = len(b)
    for k in range(0, n):
        print(k)
        print(a, b)
        a, b = find_main_elem(a, b, k)
        print(a, b)
        if is_nieoznaczony(a, b, k):
            return "Układ nieoznaczony!"
        if is_inconsistent(a, b, k):
            return "Układ sprzeczny!"
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
    A = [[0, 0, 1],
         [1, 0, 0],
         [0, 1, 0]]
    B = [3, 7, 5]
    print("Wynik: ", jordan(A, B))
