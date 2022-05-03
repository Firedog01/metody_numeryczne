import numpy as np
import functions
from gauss_hermite import *
from newton_cotes import *
from inspect import getmembers, isfunction


if __name__ == "__main__":
    fns = getmembers(functions, isfunction)
    while True:
        print("-----------------------------------------------------------------------------------------------------")
        for idx, f in enumerate(fns):
            print(f"{idx}. {f[0]}")
        idx = int(input("select function: "))
        fn = fns[idx][1]
        print("Newton-Cortes:", newton_cotes_inf(1, fn, precision=0.0001))
        print("Gauss-Hermite, 2 nodes:", gauss_hermite(fn, nodes=2))
        print("Gauss-Hermite, 3 nodes:", gauss_hermite(fn, nodes=3))
        print("Gauss-Hermite, 4 nodes:", gauss_hermite(fn, nodes=4))
        print("Gauss-Hermite, 5 nodes:", gauss_hermite(fn, nodes=5))
