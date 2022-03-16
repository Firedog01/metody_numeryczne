# 0 - error, 1 - iterations
def bisection(f, a: int, b: int, mode=0, epsilon=1, iterations=10):
    i = 0
    while i * mode < iterations:
        x0 = (a+b)/2
        if f(x0) and abs(f(x0)) < epsilon:
            return x0
        elif f(x0) * f(b) < 0:
            a = x0
        elif f(x0) * f(a) < 0:
            b = x0
        i += 1
    return x0
