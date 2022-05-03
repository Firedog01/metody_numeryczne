# złożoną kwadraturę Newtona-Cotesa opartą na trzech węzłach (wzór Simpsona)
from numpy import exp


def newton_cotes_inf(a: float, func, precision: float):
    # zakładamy, że a = ro
    ret = 0
    value = 0

    # (0, inf)
    p = 0
    while abs(value) > precision or p == 0:
        value = newton_cotes(p, p + a, func, precision)
        # print(f"{value=}")
        ret += value
        p += a

    # (-inf, 0)
    # print("minus")
    p = 0
    while abs(value) > precision or p == 0:
        value = newton_cotes(p - a, p, func, precision)
        # print(f"{value=}")
        ret += value
        p -= a
    return ret


def newton_cotes(a: float, b: float, func, precision: float):
    old_ret = 0.0
    ret = 0.0
    N = 2
    while abs(ret - old_ret) > precision or ret == 0.0 or old_ret == 0.0:
        old_ret = ret
        ret = newton_cotes_single(a, b, func, N)
        # print(f"{N=} {ret=} {old_ret=}")
        N *= 2
    return ret


def newton_cotes_single(a: float, b: float, func, N: int):
    h = (b - a) / (N - 1)
    x = [a + h * i for i in range(0, N)]
    ret = 0
    for i in range(0, N):
        y = func(x[i]) * weight_function(x[i])
        if i == 0 or i == N - 1:
            ret += y
        elif i % 2 == 0:
            ret += 2 * y
        else:
            ret += 4 * y
    return ret * h / 3