from function import *
from newton_cotes import *


# Scale this? It's only for x = [-1, 1]
# Also these lambdas look shitty af
def chebyshev_polymonials(m: int):
    if m == 1:
        return [lambda x: 1]
    elif m == 2:
        return [lambda x: 1, lambda x: x]
    else:
        ret = [lambda x: 1, lambda x: x]
        for i in range(2, m+1):
            ret.append(lambda x: 2 * x * ret[i-1](x) - ret[i-2](x))
        return ret


# I hate everything about this
def chebushev_aproximation(x: float, a: float, b: float, fun, m: int, int_prec: float = 0.1):
    ret = 0
    g = chebyshev_polymonials(m)
    wg = [lambda xx: 1/np.sqrt(1-xx*xx) * gi(xx) for gi in g]
    for k in range(0, m):
        ck_1 = newton_cotes(a, b, lambda xx: wg[k](xx) * fun(xx), int_prec)
        ck_2 = newton_cotes(a, b, lambda xx: wg[k](xx) * g[k](xx), int_prec)
        ret += ck_1 / ck_2 * g[k](x)
    return ret
