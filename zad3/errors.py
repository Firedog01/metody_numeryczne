from newton import *


def errors(X: list, Y: list = None, fun: function = None):
    if Y is not None:
        pass
    elif fun is not None:
        Y = [fun.value(x) for x in X]
    else:
        raise Exception("errors needs 2 args")

    errs = []
    for x in X:
        mul = 1
        for xi in X:
            mul *= (x-xi)
        errs.append(diff_quot(X, Y) * mul)
    return sum(errs)/len(errs)
