
import matplotlib.pyplot as plt
import numpy as np
from Function import Function
from bisection import bisection
from falsi import falsi
# 03B
from test import test_block

examples = [
    ("x", (-5, 5)),
    ("x^3-x^2-2x+1", (-10, 10)),
    ("2^x-3x", (-10, 10)),
    ("3x+sin-e^x", (-10, 10)),
    ("x^3-x+1", (-10, 10)),
    ("tan-1", (-10, 10)),
    ("2+cos", (-10, 10)),
    ("sin-cos", (-10, 10)),
    ("5x^3 - 5.8sin*x^3 + cos^3*x^2", (-0.5, 1.1)),
    ("5.8sin*x^3 + cos^3*x^2", (-0.5, 1.1)),
    ("2x", (-1, 1))
]


def print_help():
    print("""
Parametry:
    e0 .. e[n] - wykonaj obliczenia dla jednego z przykładów
    e - wyświetl dostępne przykłady
    h - wyświetl pomoc
    c - wprowadź własną funkcję
    q - wyjdź z programu
Zasady wpisywania: 
    - obsługiwana jest postać wielomianowa równania
    - wpisany element musi spełniać schemat: 
    - dostępne są funkcje trygonometryczne sin, cos i tan oraz stałe e, pi
    - argumentem funkcji trygonometrycznej może być tylko x
    - by skorzystać z funkcji należy wpisać jej nazwę, np. 3sin [co oznacza 3 * sin(x)]
    - funkcje trygonometryczne działają na x podanym w radianach
    - brak obsługi nawiasów ani znaku modułu |
    - obsługiwane są tylko potęgi naturalne
    - brak obsługi dzielenia
    - nie wstawiać znaku '*' pomiędzy współczynnikiem a funkcją/stałą
    - spacje są ignorowane

Schemat postaci wpisywanego czynnika:
    (współczynnik) (funkcja/stała (^ potęga/x) *) x (^ potęga) 
lub (współczynnik) [funkcja/stała] (^ potęga/x)
    [] - część wymagana
    () - część opcjonalna
Przykłady poprawnych czynników
    -1 sin^2 * x^3
    0.4x^2
    15 sin""")


def print_examples():
    i = 0
    for e in examples:
        print("[", i, "]", "f(x) =", e[0], "przedział:", e[1])
        i += 1


def plot(fun: Function, range_: (float, float)):
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

    plt.plot(x_points, y_points)
    plt.show()

def set_parameters():
    algo = input("wybierz algorytm (b - bisekcja, f - falsi, t - testuj algorytmy): ")
    if algo == "t":
        return "t", "t", "t"
    elif algo != "b" and algo != "f":
        print("bledny parametr")
        return "", "", ""

    mode = input("wybierz warunek stopu (d - dokładność, i - iteracje): ")
    if mode == "d":
        mode = 0
    elif mode == "i":
        mode = 1
    else:
        print("bledny parametr")
        return "", "", ""

    limit = ""
    if mode == 0:
        limit = float(input("podaj dokładność obliczeń: "))
    elif mode == 1:
        limit = int(input("podaj ilość iteracji: "))
    return algo, mode, limit



if __name__ == '__main__':
    # todo
    #  - przedziały z pi
    #  - aproksymacja
    #  - miejsca znaczące
    i = ""
    algo = ""
    while i != "q":
        i = input("wprowadź parametr, h by uzyskać pomoc: ")
        f = ""
        if i == "h":
            print_help()
        elif i == "e":
            print_examples()
        elif "e" in i:
            n = int(i[1:])
            f = examples[n][0]
            r = examples[n][1]
            p, q = r
            algo, mode, limit = set_parameters()
        elif i == "c":
            f = input("podaj funkcję: ")
            p, q = input("podaj przedział w postaci x y: ").split()
            p = float(p)
            q = float(q)
            r = (p, q)
            algo, mode, limit = set_parameters()
        elif i == "q":
            pass
        else:
            print("zly parametr")

        if f != "" and algo != "":
            if algo != "t":
                fn = Function(f)
                if algo == "b" and not mode:
                    x0, iters = bisection(fn, p, q, mode, epsilon=limit)
                elif algo == "b" and mode:
                    x0, iters = bisection(fn, p, q, mode, iterations=limit)
                elif algo == "f" and not mode:
                    x0, iters = falsi(fn, p, q, mode, epsilon=limit)
                elif algo == "f" and mode:
                    x0, iters = falsi(fn, p, q, mode, iterations=limit)

                plot(fn, r)
                print(f)
                print("x0 =", x0)
                print("iteracje:", iters)
                del fn
            else:
                test_block(f, p, q)
