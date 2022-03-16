# 0 - epsilon, 1 - iterations
def falsi(f, a: int, b: int, mode=0, epsilon=1, iterations=10):
    i = 0
    while i * mode < iterations:
        x0 = a - f(a)/(f(b) - f(a)) * (b - a)
        if f(x0) == 0 or (abs(f(x0)) < epsilon and not mode):
            return x0
        elif f(x0) * f(b) < 0:
            a = x0
        elif f(x0) * f(a) < 0:
            b = x0
        i += 1
    return x0
