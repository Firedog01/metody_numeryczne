import numpy as np


def e_to_min_x_2(x: float):
    # +-inf: 1.77245385090551602729816748
    # +-10:  1.77245385090551602729816748
    return np.exp(-(x * x))


def p_3x2_2x_min_13(x: float):
    # +-inf: -20.383219285413434313928926
    # +-10:  -20.383219285413434313928926
    return 3 * x * x + 2 * x - 13


def sin(x: float):
    # +-inf: 0
    # +-10: 0
    # 0, 10: 0.424436
    return np.sin(x)


def sin2_min_cos2(x: float):
    # +-inf: -0.6520493321732921830591586
    # +-10:  -0.6520493321732921830591586
    return np.sin(x) ** 2 - np.cos(x) ** 2



def sin_to_2_cos(x: float):
    return np.sin(x) * np.sin(x) + np.cos(x)


def x(x: float):
    # +-inf: 0
    # +-10: 0
    return x


def two_x_5(x: float):
    return 2 * x + 5
