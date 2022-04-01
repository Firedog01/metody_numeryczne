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
