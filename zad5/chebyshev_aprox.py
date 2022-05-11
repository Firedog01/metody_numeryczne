import math

from function import *
from newton_cotes import *


class Polymonial:

    coefs: list

    def __init__(self, coefs):
        self.coefs = coefs

    def value(self, x: float):
        ret = self.coefs[0]
        for i in range(1, len(self.coefs)):
            ret = self.coefs[i] + x * ret
        return ret


def chebyshev_polymonials(m: int):
    if m == 1:
        return [lambda x: 1]
    elif m == 2:
        return [lambda x: 1, lambda x: x]
    else:
        coefs = [[1], [1, 0]]
        ret = [lambda x: 1, lambda x: x]
        for i in range(2, m):
            newc = [a * 2 for a in coefs[i-1]]
            newc += [0]
            for j in range(1, i):  # Not sure about range xd
                newc[j] -= coefs[i-2][j-1]
            ret.append(Polymonial(newc).value)
            coefs.append(newc)
    return ret


# I hate everything about this
def chebyshev_aproximation(x: float, fun, m: int, int_prec: float = 0.1):
    ret = 0
    g = chebyshev_polymonials(m)
    wg = [lambda xx: 1/np.sqrt(1-xx*xx) * gi(xx) for gi in g]
    for k in range(0, m):
        wfg = lambda xx: 1/np.sqrt(1-xx**xx) * g[k](xx) * fun.value(xx)
        ck_1 = newton_cotes(-1, 1, wfg, int_prec)
        if k == 0:
            ck_2 = math.pi
        else:
            ck_2 = math.pi * 0.5
        #ck_2 = newton_cotes(-1, 1, lambda xx: wg[k](xx) * g[k](xx), int_prec)
        ret += ck_1 / ck_2 * g[k](x)
        print(k, ret)
    return ret


if __name__ == "__main__":
    p = Polymonial([1, 1, 1])
    print(p.value(2))
    fun = function("x + 2")
    ret = chebyshev_aproximation(1, fun, 5)
    print(ret)
