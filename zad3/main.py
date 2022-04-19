import matplotlib.pyplot as plt
import numpy as np
from function import Function



def print_help():
    print("""Parametry:
    e - wyświetl dostępne przykłady
    e0 .. e[n] - wykonaj obliczenia dla jednego z przykładów
    c - wprowadź własną funkcję
    h - wyświetl pomoc
    q - wyjdź z programu""")


def plot(fun: Function, range_: (float, float), x0: float, y0: float):
    plot_precision = 100.0
    fig = plt.figure()

    x_points = []
    y_points = []

    step = (range_[1] - range_[0]) / plot_precision
    for x in np.arange(range_[0], range_[1], step):
        x_points.append(x)
        y_points.append(fun.value(x))

    # move axis
    ax = fig.add_subplot(1, 1, 1)
    if min(x_points) < 0 < max(x_points):
        ax.spines['left'].set_position(('data', 0))
    if min(y_points) < 0 < max(y_points):
        ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.plot(x_points, y_points, zorder=-1)
    plt.scatter(x0, y0, color='red', zorder=10)
    plt.show()


if __name__ == "__main__":
    print("Program do interpolacji funkcji za pomocą metody Newtona na węzłach Cauchiego")

    examples = [
        ("x", (-50, 50)),
        ("x^3-x^2-2x+1", (-10, 10)),
        ("2^x-3x", (2, 10)),
        ("3x+sin-e^x", (-1, 1)),
        ("x^3-x+1", (-10, 10)),
        ("tan-1", (-1, 1.5)),
        ("cos-2x", (-10, 10)),
        ("cos-sin^2", (0, 4)),
        ("5x^3 - 5.8sin*x^3 + cos^3*x^2", (1, 2)),
        ("3sin*x^3 + cos^3*x^2", (1, 3.1)),
        ("2x", (-1, 1))
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
        elif i == "c":
            f = input("Podaj funkcję: ")
            p, q = input("Podaj przedział w postaci x y: ").split()
            r = (float(p), float(q))
        elif i == "q":
            pass
        else:
            print("Zly parametr!")

        if f != "" and algo != "":
            fn = Function(f)

            del fn

