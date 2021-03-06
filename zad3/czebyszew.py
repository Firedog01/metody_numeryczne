from numpy import cos, pi


# n - amount of nodes
# a,b - range
def czebyszew(n, a, b):
    ret = []
    for k in range(0, n):
        x = cos((2 * k + 1) / (2 * n + 1) * pi)
        t = (a + b) / 2 + x * (b - a) / 2
        ret.append(t)
    return ret


if __name__ == "__main__":
    print(czebyszew(10, 2, 5))
