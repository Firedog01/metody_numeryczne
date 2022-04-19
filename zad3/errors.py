from function import function
from newton import newton
import numpy as np


def errors(p: float, q: float, X: list, fun: function):
    step = 0.001
    errs = []
    for i in np.arange(p, q, step):
        errs.append(error(i, X, fun))
    return sum(errs)/len(errs)


def error(x: float, X: list, fun: function):
    return abs(fun.value(x) - newton(x, X, fun=fun))
