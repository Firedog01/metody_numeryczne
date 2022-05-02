import numpy as np

import functions
from gauss_hermite import *
from newton_cotes import *
from inspect import getmembers, isfunction


if __name__ == "__main__":
    fns = getmembers(functions, isfunction)
    for idx, f in enumerate(fns):
        print(f"{idx}. {f[0]}")
    idx = int(input("select function: "))
    fn = fns[idx][1]

    print("Solution:", newton_cotes(-10, 10, fn, 0.001, lambda x: 1))
    #print("Solution:", gauss_hermite(fn, 3))
