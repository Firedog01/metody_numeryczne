from Function import *
from bisection import *
from falsi import *

def test_block(f_str, a, b):
    print("------------------------------------------------")
    print("Funkcja:", f_str, "a =", a, "b =", b)
    test(f_str, a, b, mode=0, epsilon=0.1)
    test(f_str, a, b, mode=0, epsilon=0.01)
    test(f_str, a, b, mode=0, epsilon=0.001)

    test(f_str, a, b, mode=1, iterations=10)
    test(f_str, a, b, mode=1, iterations=100)
    test(f_str, a, b, mode=1, iterations=1000)
    print("")


def test(f_str, a, b, mode=0, epsilon=0.1, iterations=10):
    print("------------------------------------------------")
    if not mode:
        print("epsilon =", epsilon)
    else:
        print("iteracje =", iterations)
    f = Function(f_str)
    x0bi, ibi = bisection(f, a, b, mode, epsilon, iterations)
    print("bisection:", x0bi, "iteracje:", ibi)
    del f
    f = Function(f_str)
    x0falsi, ifalsi = falsi(f, a, b, mode, epsilon, iterations)
    print("falsi:    ", x0falsi, "iteracje:", ifalsi)
    del f

if __name__ == '__main__':

    # Przyklady
    test_block("x", -50, 50),
    test_block("x^3-x^2-2x+1", -10, 10)
    test_block("2^x-3x", 2, 10)
    test_block("3x+sin-e^x", -1, 1)
    test_block("x^3-x+1", -10, 10)
    test_block("tan-1", -1, 1.5)
    test_block("cos-2x", -10, 10)
    test_block("cos-sin^2", 0, 4)
    test_block("5x^3 - 5.8sin*x^3 + cos^3*x^2", 1, 2)
    test_block("3sin*x^3 + cos^3*x^2", 1, 3.1)
    test_block("2x", -1, 1)

    # Inne
    test_block("sin+3cos^2-tan", -1, 1.3)
    #
    # # Funkcje liniowe
    #
    # x0true = 0
    # f_str = "x"
    # print("------------------------------------------------")
    # test(f_str, -1, 2, mode=0, epsilon=0.1)
    # test(f_str, -1, 2, mode=0, epsilon=0.01)
    # test(f_str, -1, 2, mode=0, epsilon=0.001)
    #
    # test(f_str, -1, 2, mode=1, iterations=10)
    # test(f_str, -1, 2, mode=1, iterations=100)
    # test(f_str, -1, 2, mode=1, iterations=1000)
    #
    # x0true = 0
    # f_str = "x"
    # print("------------------------------------------------")
    # test(f_str, -100, 200, mode=0, epsilon=0.1)
    # test(f_str, -100, 200, mode=0, epsilon=0.01)
    # test(f_str, -100, 200, mode=0, epsilon=0.001)
    #
    # test(f_str, -100, 200, mode=1, iterations=10)
    # test(f_str, -100, 200, mode=1, iterations=100)
    # test(f_str, -100, 200, mode=1, iterations=1000)
    #
    # x0true = -0.5
    # f_str = "100x+50"
    # print("------------------------------------------------")
    # test(f_str, -1, 1, mode=0, epsilon=0.1)
    # test(f_str, -1, 1, mode=0, epsilon=0.01)
    # test(f_str, -1, 1, mode=0, epsilon=0.001)
    #
    # test(f_str, -1, 1, mode=1, iterations=10)
    # test(f_str, -1, 1, mode=1, iterations=100)
    # test(f_str, -1, 1, mode=1, iterations=1000)
    #
    # x0true = -1.61803398874989484
    # f_str = "x^3+x^2-x"
    # print("------------------------------------------------")
    # test(f_str, -10, -0.5, mode=0, epsilon=0.1)
    # test(f_str, -10, -0.5, mode=0, epsilon=0.01)
    # test(f_str, -10, -0.5, mode=0, epsilon=0.001)
    #
    # test(f_str, -10, -0.5, mode=1, iterations=10)
    # test(f_str, -10, -0.5, mode=1, iterations=100)
    # test(f_str, -10, -0.5, mode=1, iterations=1000)
    #
    # x0true = 4.19155
    # f_str = "0.1sin+0.01x^4-3"
    # print("------------------------------------------------")
    # test(f_str, 4, 5, mode=0, epsilon=0.1)
    # test(f_str, 4, 5, mode=0, epsilon=0.01)
    # test(f_str, 4, 5, mode=0, epsilon=0.001)
    #
    # test(f_str, 4, 5, mode=1, iterations=10)
    # test(f_str, 4, 5, mode=1, iterations=100)
    # test(f_str, 4, 5, mode=1, iterations=1000)
    #
    # x0true = 0
    # f_str = "x^3"
    # print("------------------------------------------------")
    # test(f_str, -10, 50, mode=0, epsilon=0.1)
    # test(f_str, -10, 50, mode=0, epsilon=0.01)
    # test(f_str, -10, 50, mode=0, epsilon=0.001)
    #
    # test(f_str, -10, 50, mode=1, iterations=10)
    # test(f_str, -10, 50, mode=1, iterations=100)
    # test(f_str, -10, 50, mode=1, iterations=1000)
    #
    # x0true = 0
    # f_str = "x^3"
    # print("------------------------------------------------")
    # test(-1, 2, mode=0, epsilon=0.1)
    # test(-1, 2, mode=0, epsilon=0.01)
    # test(-1, 2, mode=0, epsilon=0.001)
    # test(-1, 2, mode=0, epsilon=0.0001)
    # test(-1, 2, mode=0, epsilon=0.00001)
    #
    # test(-1, 2, mode=1, iterations=10)
    # test(-1, 2, mode=1, iterations=100)
    # test(-1, 2, mode=1, iterations=1000)
