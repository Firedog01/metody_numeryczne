from numpy import cos


# n - amount of nodes
def чебышёв(n, a, b):
    ret = []
    for k in range(0, n):
        x = cos((2 * k + 1) / (2 * n + 1))
        t = (a + b) / 2 + x * (b - a) / 2
        ret.append(t)
    return ret


if __name__ == "__main__":
    print(чебышёв(10, 2, 5))
