# Function returns x0 and iterations
# 0 - epsilon, 1 - iterations
def falsi(f, a: float, b: float, mode=0, epsilon=0.1, iterations=10):
    i = 0
    while i * mode < iterations:
        i += 1
        x0 = a - f.value(a)/(f.value(b) - f.value(a)) * (b - a)
        if f.value(x0) == 0 or (abs(f.value(x0)) < epsilon and not mode):
            return x0, i
        elif f.value(x0) * f.value(b) < 0:
            a = x0
        else:
            b = x0

    return x0, i
