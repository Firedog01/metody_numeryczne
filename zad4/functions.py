import numpy as np


def e_to_x2(x: float):
    # +-inf: 1.77245385090551602729816748
    # +-10:  1.77245385090551602729816748
    return np.exp(-(x * x))


def e_to_x2_x(x: float):
    # +-inf: 0
    # +-10: 0
    return np.exp(-(x * x)) * x


def e_to_x2_sin(x: float):
    # +-inf: 0
    # +-10: 0
    # 0, 10: 0.424436
    return np.exp(-(x * x)) * np.sin(x)


def e_to_x2_sin2_min_cos2(x: float):
    # +-inf: -0.6520493321732921830591586
    # +-10:  -0.6520493321732921830591586
    return np.exp(-(x * x)) * (np.sin(x) ** 2 - np.cos(x) ** 2)


def e_to_x2_3x2_2x_min13(x: float):
    # +-inf: -20.383219285413434313928926
    # +-10:  -20.383219285413434313928926
    return np.exp(-(x * x)) * p_3x2_2x_min13(x)


def linear(x: float):
    # 0, 10: 50
    # +-10: 0
    return x


def p_3x2_2x_min13(x):
    # +-10: 1740
    return 3 * x * x + 2 * x - 13


def gaussian(x):
    # +-inf: 2.5066282746
    # 0, 10: 1.25331
    # -10, 10: 2.5066282746
    return np.exp(-(x * x)/2)
