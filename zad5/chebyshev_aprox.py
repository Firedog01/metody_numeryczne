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
        return [Polymonial([1])]
    elif m == 2:
        return [Polymonial([1, 0])]
    else:
        coefs = [[1], [1, 0]]
        ret = [Polymonial([1]), Polymonial([1, 0])]
        for i in range(2, m):
            newc = [a * 2 for a in coefs[i - 1]]
            newc += [0]
            for j in range(1, i):  # Not sure about range xd
                newc[j + 1] -= coefs[i - 2][j - 1]
            ret.append(Polymonial(newc))
            coefs.append(newc)
    return ret


# I hate everything about this
# def chebyshev_aproximation(x: float, a: float, b: float, fun, m: int, int_prec: float = 0.1):
#     x = (2 * x - a - b) / (b - a)
#     ret = 0
#     g = chebyshev_polymonials(m)
#     p = Polymonial([1, 2, 3])
#     p.value(2)
#     print(type(g), type(g[0]), type(g[3]))
#     wg = [lambda xx: 1 / np.sqrt(1 - (xx*0.999)**2) * gi.value(xx) for gi in g]
#     for k in range(0, m):
#         print("coasds", wg[k](1))
#         wfg = lambda xx: wg[k](xx) * fun.value(xx)
#         ck_1 = newton_cotes(a, b, wfg, int_prec)
#         if k == 0:
#             ck_2 = math.pi
#         else:
#             ck_2 = math.pi * 0.5
#         # ck_2 = newton_cotes(-1, 1, lambda xx: wg[k](xx) * g[k](xx), int_prec)
#         print(k, ck_1, ck_2, g[k].value(x))
#         ret += ck_1 / ck_2 * g[k].value(x)
#         print(k, ret)
#     return ret
def chebyshev_aprox(x: float, a: float, b: float, f, m: int, precision=0.1):
    ret = 0
    #x = (2 * x - a - b) / (b - a)
    g_list = chebyshev_polymonials(m)
    for k in range(m):
        wfg = lambda val: 1 / math.sqrt(1.000001 - val*val) * f(val) * g_list[k].value(val)
        ck_1 = newton_cotes(-1, 1, wfg, precision)
        if k == 0:
            ck_2 = math.pi
        else:
            ck_2 = math.pi * 0.5

        ret += ck_1 / ck_2 * g_list[k].value(x)

    return ret




if __name__ == "__main__":
    f = lambda x: 2 * x + 1
    print(chebyshev_aprox(1, -2, 5, f, 5))
