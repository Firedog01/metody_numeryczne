import os
import numpy as np


def get_files():
    root_dir = os.path.dirname(__file__)
    files_dir = root_dir + "\\files"
    return os.listdir(files_dir)


def get_matrix(file: str):
    return np.genfromtxt("files\\" + file, delimiter=",")

