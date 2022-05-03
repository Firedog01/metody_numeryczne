# wariant kwadratury Gaussa (wielomiany Hermite'a)


# Nodes
X = [
    [-0.707107, 0.707107],
    [-1.22475, 0, 1.22475],
    [-1.65068, -0.524648, 0.524648, 1.65068],
    [-2.02018, -0.958573, 0, 0.958573, 2.02018]
]


# Weights
A = [
    [0.886227, 0.886227],
    [0.295409, 1.181636, 0.295409],
    [0.081313, 0.804914, 0.804914, 0.081313],
    [0.019953, 0.393619, 0.945309, 0.393619, 0.019953]
]


def gauss_hermite(fun, nodes: int):
    if not 2 <= nodes <= 5:
        raise Exception("Node count out of range!")
    ret = 0
    for i in range(0, nodes):
        ret += A[nodes - 2][i] * fun(X[nodes - 2][i])
    return ret
