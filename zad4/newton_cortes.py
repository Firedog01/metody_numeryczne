# złożoną kwadraturę Newtona-Cotesa opartą na trzech węzłach (wzór Simpsona)
# from function import function


def newton_cortes(a: float, b: float, func, precision: float, weight_func):
    old_ret = 0
    ret = 0
    N = 2
    while abs(ret - old_ret) > precision or N <= 4:
        old_ret = ret
        h = (b - a) / (N - 1)
        x = [a + h*i for i in range(0, N)]
        ret = 0
        for i in range(0, N):
            y = func(x[i]) * weight_func(x[i])
            if i == 0 or i == N - 1:
                ret += func(x[i])
            elif i % 2 == 0:
                ret += 2 * y
            else:
                ret += 4 * y
        ret *= h / 3
        print(f"{N=} {old_ret=} {ret=}")
        N *= 2
    return ret

# TODO:
#  1. Granica
#  2. Funkcja wagowa
#  bo tak jest napisane w poleceniu
