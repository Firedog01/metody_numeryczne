import bisection
import matplotlib.pyplot as plt
import numpy as np
from Function import *

# 03B


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
    pn1 = Function("2 1 -5.4 -18")
    plot(pn1, (2, 5))



