import re
import numpy as np


class Function:
    funcs = list()

    # Divide string into list and transform into lambdas
    def __init__(self, s: str):
        # sorted list where:
        #   3x^3 -> fn_list[3] == "3x"
        #   2 -> fn_list[0] == "2"
        #   3x + 5x -> fn_list[1] == "3x 5x"
        #   5sin^3*x^2 -> fn_list[2] == "5sin^3"
        fn_list = make_list(s)

        print("Function, fn_list:", fn_list)
        for fn in fn_list:
            self.funcs.append(make_lambda(fn))
        self.funcs.reverse()

    def value(self, x: float):
        ret = 0
        for fn in self.funcs:
            ret = ret * x + fn(x)
        return ret


def prepend_1(s: str, f: str):
    s = re.sub('-' + f, '-1' + f, s)
    s = re.sub(' ' + f, ' 1' + f, s)
    s = re.sub('^' + f, '1' + f, s)
    return s


def make_list(s):
    s = re.sub(r' ', '', s)
    # delete all spaces

    s = re.sub(r'\+', ' ', s)
    s = re.sub(r'-', ' -', s)
    s = re.sub(r'^ -', '-', s)
    s = re.sub(r'\( -', '(-', s)
    # space indicates addition

    s = prepend_1(s, "x")
    s = prepend_1(s, "sin")
    s = prepend_1(s, "cos")
    s = prepend_1(s, "tan")
    s = prepend_1(s, "e")
    s = prepend_1(s, "pi")
    # x -> 1x, -x -> -1x
    # same for functions and constants

    fn_list = list(str.split(s, ' '))
    print("make_list, fn_list:", fn_list)
    fn_dict = dict()
    for fn in fn_list:
        if re.search(r'x\^', fn):
            pow_key = int(fn.split('x^')[1])
        else:
            pow_key = 0

        before = fn.split('x^')[0]
        if before[-1] == "*":
            before = before[:len(before) - 1]

        if pow_key in fn_dict:
            fn_dict[pow_key] += ' ' + before
        else:
            fn_dict[pow_key] = before
    max_idx = max(k for k, v in fn_dict.items())
    fn_list_new = list()
    for idx in range(max_idx + 1):
        if idx in fn_dict:
            fn_list_new.append(fn_dict[idx])
        else:
            fn_list_new.append("")
    return fn_list_new


def make_lambda(fns: str):
    if fns == "":
        return lambda x: 0
    fn_list = fns.split(' ')
    lambdas = list()
    for elem in fn_list:
        a = float(re.findall(r'^-?\d+\.?\d*', elem)[0])
        rest = re.search(r'[^\d\.]+.*$', elem)
        if rest is None:
            print("rest_s: none, a:", a)
            def lbd(x): return a
            lambdas.append(lbd)
        else:
            rest_s = rest.group(0)
            print("rest_s:", rest_s)
            parts = rest_s.split('^')
            part0lbd = lambda x: 0
            if parts[0] == "sin":
                part0lbd = lambda x: np.sin(x)
                # def part0lbd(x): return np.sin(x)
            elif parts[0] == "cos":
                part0lbd = lambda x: np.cos(x)
                # def part0lbd(x): return np.cos(x)
            elif parts[0] == "tan":
                part0lbd = lambda x: np.tan(x)
                # def part0lbd(x): return np.tan(x)
            elif parts[0] == "pi":
                part0lbd = lambda x: np.pi
                # def part0lbd(x): return np.pi
            elif parts[0] == "e":
                part0lbd = lambda x: np.e
                # def part0lbd(x): return np.e

            if len(parts) == 1:
                def lbd(x): return a * part0lbd(x)
                lambdas.append(lbd)
            elif len(parts) == 2:
                if parts[1] == "x":
                    def lbd(x): return a * part0lbd(x) ** x
                    lambdas.append(lbd)
                else:
                    b = int(parts[1])
                    def lbd(x): return a * part0lbd(x) ** b
                    lambdas.append(lbd)
    for l in lambdas:
        print(l(2))
    return lambda x: sum(f(x) for f in lambdas)
