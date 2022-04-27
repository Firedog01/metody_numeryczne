import matplotlib.pyplot as plt
import numpy as np
from function import function
from newton import newton
from errors import errors
from czebyszew import *


def print_help():
    print("""Parametry:
    e - wyświetl dostępne przykłady
    e0 .. e[n] - wykonaj obliczenia dla jednego z przykładów
    c - wprowadź własną funkcję
    h - wyświetl pomoc
    q - wyjdź z programu""")


def plot(fun: function, range_: (float, float), X: list):
    plot_precision = 100.0
    fig = plt.figure()

    # Draw fun graph
    x_points_f = []
    y_points_f = []
    x_points_g = []
    y_points_g = []
    step = (range_[1] - range_[0]) / plot_precision
    for x in np.arange(range_[0], range_[1], step):
        x_points_f.append(x)
        y_points_f.append(fun.value(x))

    # Draw interpolated function graph
    step = (range_[1] - range_[0]) / plot_precision
    for x in np.arange(range_[0], range_[1], step):
        x_points_g.append(x)
        y_points_g.append(newton(x, X, fun=fun))

    # move axis
    ax = fig.add_subplot(1, 1, 1)
    if min(x_points_f) <= 0 <= max(x_points_f):
        ax.spines['left'].set_position(('data', 0))
    if min(y_points_f) <= 0 <= max(y_points_f):
        ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.plot(x_points_f, y_points_f, zorder=-1, color="orange")
    plt.plot(x_points_g, y_points_g, zorder=-1, color="blue")

    # Scatter interpolation nodes
    plt.scatter(X, [fun.value(x) for x in X], color='blue', zorder=10)
    plt.show()


if __name__ == "__main__":
    print("Program do interpolacji funkcji za pomocą metody Newtona na węzłach Czebyszewa")

    examples = [
        ("x", (-5, 5)),                                                     # liniowa
        ("abs", (-4, 4)),                                                   # moduł
        ("x^5 - 35 x^4 + 461 x^3 - 2821 x^2 + 7842 x - 5423", (2, 12)),     # wielomian
        ("3x^2 + 5x - 8", (-5, 3)),                                         # wielomian (prosty)
        ("sin + cos", (-4, 4)),                                             # trygonometryczna
        ("4sin^3 + sin^2 + sin - 1", (-4, 6)),                              # wielomian i trygonometryczna
        ("sin + cos", (-20, 20)),                                           # trygonometryczna, długi przedział
    ]
    i = ""
    algo = ""
    while i != "q":
        i = input("Wprowadź parametr, h by uzyskać pomoc: ")
        f = ""
        # inputting parameters
        if i == "h":
            print_help()
        elif i == "e":
            for idx, s in enumerate(examples):
                print(f"{idx}. {s}")
        elif "e" in i:
            n = int(i[1:])
            f = examples[n][0]
            r = examples[n][1]
            p, q = r
        elif i == "c":
            f = input("Podaj funkcję: ")
            p, q = input("Podaj przedział: ").split()
            r = (float(p), float(q))
        elif i == "q":
            pass
        else:
            print("Zly parametr!")

        if f != "":
            o = int(input("Podaj ilość węzłów: "))
            nodes = czebyszew(o, p, q)
            fn = function(f)
            plot(fn, r, nodes)
            print("błąd: %.4f" % errors(p, q, nodes, fun=fn))
            del fn
