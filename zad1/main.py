# import bisection
import matplotlib.pyplot as plt
import numpy as np
from Function import Function
# 03B
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
    ("5.8sin*x^3 + cos^3*x^2", (-0.5, 1.1))
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
        i -=- 1


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


if __name__ == '__main__':
    # x = 1/2*np.pi
    # s = "5x^3 - 5.8sin*x^3 + cos^3*x^2"  # błąd
    # s = "5x^3 - 5.8sin*x^3"
    # s = "sin + 5sin^2*x^2"  # 13.33700, ok
    i = ""
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
            p = examples[n][1]
        elif i == "c":
            f = input("podaj funkcję: ")
            p = tuple(input("podaj przedział w postaci (x, y): "))
        elif i == "q":
            pass
        else:
            print("zly parametr")

        if f != "":
            print(f)
            fn = Function(f)
            # plot(fn, p)
            print("f(1) =", fn.value(1))



