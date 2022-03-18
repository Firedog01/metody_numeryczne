from Function import *
from bisection import *
from falsi import *


def test(f_str, a, b, mode=0, epsilon=0.1, iterations=10):
    print("------------------------------------------------")
    print("function:", f_str, "a =", a, "b =", b)
    if not mode:
        print("epsilon =", epsilon)
    else:
        print("iterations =", iterations)
    f = Function(f_str)
    x0bi, ibi = bisection(f, a, b, mode, epsilon, iterations)
    x0falsi, ifalsi = falsi(f, a, b, mode, epsilon, iterations)
    print("bisection:", x0bi, ibi)
    print("falsi:    ", x0falsi, ifalsi)
    print("true x0:  ", x0true)


if __name__ == '__main__':

    x0true = 0
    print("------------------------------------------------")
    test("x", -10, 20, mode=0, epsilon=0.1)
    test("x", -10, 20, mode=0, epsilon=0.01)
    test("x", -10, 20, mode=0, epsilon=0.001)

    test("x", -10, 20, mode=1, iterations=10)
    test("x", -10, 20, mode=1, iterations=100)
    test("x", -10, 20, mode=1, iterations=1000)


    x0true = -1.61803398874989484
    print("------------------------------------------------")
    test("x^3+x^2-x", -10, -0.5, mode=0, epsilon=0.1)
    test("x^3+x^2-x", -10, -0.5, mode=0, epsilon=0.01)
    test("x^3+x^2-x", -10, -0.5, mode=0, epsilon=0.001)

    test("x^3+x^2-x", -10, -0.5, mode=1, iterations=10)
    test("x^3+x^2-x", -10, -0.5, mode=1, iterations=100)
    test("x^3+x^2-x", -10, -0.5, mode=1, iterations=1000)
