import os
import numpy as np


def get_files():
    root_dir = os.path.dirname(__file__)
    files_dir = root_dir + "\\files"
    return os.listdir(files_dir)


def get_matrices(file: str):
    concated = np.genfromtxt("files\\" + file, delimiter=",")
    height = len(concated)
    splited = np.array_split(concated, [height], axis=1)
    return tuple(splited)


def swap_pos(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst


def almost_range(i, k, n):
    ret = [*range(i, n)]
    ret.remove(k)
    return ret
