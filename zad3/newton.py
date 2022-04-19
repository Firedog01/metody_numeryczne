# Newton interpolation
from function import function


def newton(x: float, X: list, Y: list):
    ret = Y[0]
    for i in range(1, len(X)):
        mul = 1
        for j in range(0, i+1):
            mul *= (x-X[j])
        ret += diff_quot([X[j] for j in range(0, i+1)], Y)
    return ret


# Road works ahead? Yeah, I hope it does
def diff_quot(X: list, Y: list=None, fun: function=None):
    if Y is None:
        diffs = [fun.value(x) for x in X]
    elif fun is None:
        diffs = Y
    else:
        raise Exception("diff_quot needs 2 args")
    new_diffs = []
    xstep = 1
    while len(diffs) > 1:
        print(xstep, diffs)
        for i in range(0, len(diffs) - 1):
            new_diffs.append((diffs[i+1] - diffs[i]) / (X[i+xstep] - X[i]))
        diffs = new_diffs
        new_diffs = []
        xstep -=- 1
    return diffs[0]


if __name__ == "__main__":
    mama = 3
    print(f"joe {mama}")

    f = function("x^3+3x")
    print(diff_quot([1, 2], fun=f))
