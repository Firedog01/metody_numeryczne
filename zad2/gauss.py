import numpy as np


def gauss(A: np.array, b: np.array):
    if det(A) == 0 or A[0][0] == 0:
        return None


def det(A: np.array):
    # Is the array NxN?
    x, y = A.shape
    if x != y:
        return None
    ret = 0
    # For each row in matrix
    for i in range(x):
        plus_elements = []
        minus_elements = []
        # For each column in matrix
        for n in range(x):
            plus_elements.append(A[(i+n) % x, n])
            minus_elements.append(A[(i-n) % x, n])
        # Multiply each list and add to ret
        ret += np.prod(plus_elements)
        ret -= np.prod(minus_elements)
    return ret


if __name__ == "__main__":
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
    print(a[2])
    print(a.shape)
    print(det(a))
