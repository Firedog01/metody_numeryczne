from Function import *
from bisection import *
from falsi import *
from main import plot


def test_block(f_str, a, b):
    print("------------------------------------------------")
    print("Funkcja:", f_str, "a =", a, "b =", b)
    # test(f_str, a, b, mode=0, epsilon=0.01)
    test(f_str, a, b, mode=0, epsilon=0.001)
    test(f_str, a, b, mode=0, epsilon=0.0001)

    # test(f_str, a, b, mode=1, iterations=10)
    test(f_str, a, b, mode=1, iterations=100)
    test(f_str, a, b, mode=1, iterations=1000, do_plot=True)
    print("")


def test(f_str, a, b, mode=0, epsilon=0.1, iterations=10, do_plot=False):
    print("------------------------------------------------")
    if not mode:
        print("epsilon =", epsilon)
    else:
        print("iteracje =", iterations)
    f = Function(f_str)
    x0bi, ibi = bisection(f, a, b, mode, epsilon, iterations)
    print('bisection: %.7f' % x0bi, 'iteracje:', ibi)
    # print('bisection:', x0bi, 'iteracje:', ibi)
    if do_plot:
        plot(f, (a, b), x0bi, f.value(x0bi))
    del f
    f = Function(f_str)
    x0falsi, ifalsi = falsi(f, a, b, mode, epsilon, iterations)
    print('falsi: %.7f' % x0falsi, '   iteracje:', ifalsi)
    # print('falsi:', x0falsi, 'iteracje:', ifalsi)
    if do_plot:
        plot(f, (a, b), x0falsi, f.value(x0falsi))
    del f


if __name__ == '__main__':

    # Funkcje liniowe
    # Falsi!
    # test_block("30x", -1 ,2)
    # test_block("30x", -10 ,10)
    # test_block("2x+5", -5, 4) # Sprawko
    # test_block("2x+5", -5000, 4000) # Sprawko
    # test_block("23x+13", -50, 30) # Sprawko
    # test_block("23x+13", -5000, 3000) # Sprawko
    # test_block("-100x+123", -456, 789)
    # Falsi dla liniowych od razu znajduje

    # Wielomiany
    # Falsi
    # test_block("x^2-2", -2, 0)
    # Bi!
    # test_block("x^2-2", -2000, 0)
    # Falsi!
    # test_block("x^3-x^2-2x+1", -1, 1) # Sprawko
    # Bi?
    # test_block("x^3-x^2-2x+1", -2, 0) # Sprawko
    # Bi!!!
    test_block("x^3-x^2-2x+1", -100, 0) # Sprawko
    # Falsi
    # test_block("0.1x^3+x^2+2x", -3, -2)
    # Falsi
    # test_block("0.1x^3+x^2+2x", -7, -2)
    # Bi
    # test_block("0.5x^6+x^5-0.2x^4+x^3-12x^2-12x+2", -2, 0)
    # Bi!
    # test_block("0.5x^6+x^5-0.2x^4+x^3-12x^2-12x+2", -6, -2)
    # Bi do wielomianów, chyba że wykres funkcji łagodny

    # Trygonometria
    # Falsi
    # test_block("sin+1.5x", -5, 4)
    # test_block("sin+1.5x", -500, 400)
    # Bi
    # test_block("3sin^3", -2.2, 1.8)
    # Falsi
    # test_block("tan+3sin", 2, 4) # Sprawko
    # Falsi
    # test_block("50sin", -0.002, 0.001)
    # test_block("sin", -2, 1)
    # Bi
    # test_block("3sin^5", -2, 1)
    # test_block("3sin^5", -0.0002, 0.0001)
    # Falsi
    # test_block("sin^11+cos", 1.8, 2.1)
    # test_block("sin^11+cos", -1, 5) # Sprawko
    # Bi
    # test_block("sin^11", -0.5, 0.4)
    # test_block("sin^11", -2, 1.6) # Sprawko
    # Raczej falsi, chyba, że potęgi duże

    # Bardzo złożone funkcje
    # Bi
    # test_block("2^x+x^2+e^x+9sin-12x+0.1tan+cos-3", -1, 2)
    # Falsi
    # test_block("2^x+x^2+e^x+9sin-12x+0.1tan+cos-3", -0.2, 0.15)
    # Falsi
    # test_block("2^x+x^2+e^x+9sin-12x+1tan+cos-4", -1, 0)
    # test_block("2^x+x^2+e^x+9sin-12x+1tan+cos-4", -0.7, -0.6)
    # test_block("2^x+x^2+e^x+9sin-12x+1tan+cos-4", -2, -1)
    # Falsi
    # test_block("sin-cos-x^4+2", -1, 1)
    # Bi!!!
    # test_block("sin-cos-x^4+2", -10, 0)
    # Raczej fali, chyba że mega ostro leci

    # Przedziały
    # Falsi
    # test_block("sin+1.5x+2", -200, 200)
    # test_block("sin+1.5x+2", -399, 1)
    # test_block("sin+1.5x+2", -10, 390)
    # Bi!
    # test_block("0.1x^2+x", -9, 90)
    # test_block("0.1x^2+10x", -90, 850)
    # Bi
    # test_block("0.1x^2+x", -9, 10)
    # test_block("0.1x^2+10x", -90, 85)
    # test_block("0.1x^2+10x", -90, 850)
    # Chyba nic z tego nie wynika XD

    # Wykładnicze
    # Bi
    # test_block("2^x-1", -1000, 5)
    # test_block("2^x-1", -2, 1)
    # test_block("2^x-1", -1, 10)
    # Falsi
    # test_block("2^x-1", -1000, 1)
    pass
