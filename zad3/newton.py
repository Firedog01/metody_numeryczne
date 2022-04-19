# Newton interpolation
from function import function


def newton(x: float, X: list, Y: list = None, fun: function = None):
    if Y is not None:
        pass
    elif fun is not None:
        Y = [fun.value(x) for x in X]
    else:
        raise Exception("newton needs 3 args")

    ret = Y[0]
    for i in range(1, len(X)):
        mul = 1
        for j in range(0, i):
            mul *= (x-X[j])
        ret += diff_quot([X[j] for j in range(0, i+1)], [Y[j] for j in range(0, i+1)]) * mul
    return ret


def diff_quot(X: list, Y: list = None, fun: function = None):
    if Y is not None:
        diffs = Y
    elif fun is not None:
        diffs = [fun.value(x) for x in X]
    else:
        raise Exception("diff_quot needs 2 args")

    new_diffs = []
    xstep = 1
    while len(diffs) > 1:
        for i in range(0, len(diffs) - 1):
            new_diffs.append((diffs[i+1] - diffs[i]) / (X[i+xstep] - X[i]))
        diffs = new_diffs
        new_diffs = []
        xstep += 1
    return diffs[0]


if __name__ == "__main__":
    f = function("x^3+3x")
    print(diff_quot([1, 2], fun=f))
