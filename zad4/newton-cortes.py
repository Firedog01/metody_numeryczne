# złożoną kwadraturę Newtona-Cotesa opartą na trzech węzłach (wzór Simpsona)
from function import function


def newton_cortes(a: float, b: float, fun: function, precision: float):
    old_ret = 0
    ret = 0
    N = 2
    while abs(ret - old_ret) < precision or N == 2:
        old_ret = ret
        h = (b - a) / N
        x = [a + h*i for i in range(0, N)]
        ret = fun.value(x[0]) + fun.value(x[N-1])
        for i in range(1, N, 2):
            ret += 4 * fun.value(x[i])
        for i in range(2, N-1, 2):
            ret += 2 * fun.value(x[i])
        ret *= h / 3
        N += 2
    return ret

# TODO:
#  1. Granica
#  2. Funkcja wagowa
#  bo tak jest napisane w poleceniu