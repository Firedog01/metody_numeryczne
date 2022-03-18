# Function returns 0x and iterations
# 0 - epsilon, 1 - iterations
def bisection(f, a: float, b: float, mode=0, epsilon=0.1, iterations=10):
    i = 0
    while i < iterations or not mode:
        x0 = (a+b)/2
        print(x0, b, f.value(x0), f.value(b), f.value(x0) * f.value(b))
        print(x0, a, f.value(x0), f.value(a), f.value(x0) * f.value(a))
        if f.value(x0) == 0 or (abs(f.value(x0)) < epsilon and not mode):
            return x0, i
        elif f.value(x0) * f.value(b) < 0:
            a = x0
        elif f.value(x0) * f.value(a) < 0:
            b = x0
        i += 1
    return x0, i
