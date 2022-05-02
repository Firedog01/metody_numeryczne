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

    print("Solution:", newton_cotes(-10, 10, fn, 0.000001, functions.e_to_min_x2))
    #print("Solution:", gauss_hermite(fn, 3))
    #print("Solution:", newton_cotes_inf(0.001, 0.000001, fn, 0.000000001, lambda x: 1))
    #print("Solution:", newton_cotes_single(-10, 10, fn, 1000000, functions.e_to_min_x2))
