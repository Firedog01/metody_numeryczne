# złożoną kwadraturę Newtona-Cotesa opartą na trzech węzłach (wzór Simpsona)
# from function import function


def newton_cotes(a: float, b: float, func, precision: float, weight_func):
    old_ret = 0.0
    ret = 0.0
    N = 2
    while abs(ret - old_ret) > precision or ret == 0.0 or old_ret == 0.0:
        old_ret = ret
        ret = newton_cotes_single(a, b, func, N, weight_func)
        ret = round(ret, 10)
        print(f"{N=} {old_ret=} {ret=}")
        N *= 2
    return ret


def newton_cotes_inf(a: float, ro: float, func, precision: float, weight_func):
    ret = 0
    minus_a = -a

    print("--- PLUS ---")
    # (0, inf)
    ret += newton_cotes_single(0, a, func, 3, weight_func)
    print(newton_cotes_single(0, a, func, 3, weight_func))
    while True:
        a_ro = newton_cotes_single(a, a + ro, func, 3, weight_func)
        print(a_ro)
        if abs(a_ro) < precision:
            break
        ret += a_ro
        a += ro

    print("--- MINUS ---")
    # (-inf, 0)
    ret += newton_cotes_single(minus_a, 0, func, 3, weight_func)
    print(newton_cotes_single(minus_a, 0, func, 3, weight_func))
    while True:
        a_ro = newton_cotes_single(minus_a - ro, minus_a, func, 3, weight_func)
        print(a_ro)
        if abs(a_ro) < precision:
            break
        ret += a_ro
        minus_a -= ro
    return ret


def newton_cotes_single(a: float, b: float, func, N: int, weight_func, not__first=False):
    h = (b - a) / (N - 1)
    x = [a + h * i for i in range(0, N)]
    ret = 0
    for i in range(0, N):
        y = func(x[i]) * weight_func(x[i])
        if i == 0 or i == N - 1:
            ret += y
        elif i % 2 == 0:
            ret += 2 * y
        else:
            ret += 4 * y
    ret *= h / 3
    return ret


# TODO:
#  1. Granica
#  2. Funkcja wagowa
#  bo tak jest napisane w poleceniu
