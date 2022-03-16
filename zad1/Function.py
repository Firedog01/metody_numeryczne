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
            fn_addlist = list()
            split = fn.split(' ')
            for s in split:
                print("split, s:", s)
                fn_addlist.append(make_lambda(s))
            for f in fn_addlist:
                print("fn_addlist, f(1) =", f(1))
            self.funcs.append(fn_addlist)
        # print("funcs len", len(self.funcs))
        self.funcs.reverse()

    def __del__(self):
        self.funcs.clear()

    def value(self, x: float):
        ret = 0
        for f in self.funcs[0]:
            print("a(x) =", f(x))
            ret += f(x)
        for fn in self.funcs[1:]:
            print("-- ret:", ret)
            ret *= x
            for f in fn:
                print("a(x) =", f(x))
                ret += f(x)
            print("ret*x + a", ret)
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
        if re.search("\*x$", before):
            before = before[:len(before) - 2]

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


def make_lambda(fn: str):
    if fn == "":
        return lambda x: 0
    a = float(re.findall(r'^-?\d+\.?\d*', fn)[0])
    rest = re.search(r'[^\d\.-]+.*$', fn)
    # print("a:", a, "rest:", rest)
    if rest is None:
        return lambda x: a
    else:
        rest_s = rest.group(0)
        parts = rest_s.split('^')
        b = 1
        print("parts:", parts)
        if len(parts) == 2:
            if parts[1] == "x":
                if parts[0] == "sin":
                    return lambda x: a * np.sin(x) ** x
                elif parts[0] == "cos":
                    return lambda x: a * np.cos(x) ** x
                elif parts[0] == "tan":
                    return lambda x: a * np.tan(x) ** x
                elif parts[0] == "pi":
                    return lambda x: a * np.pi ** x
                elif parts[0] == "e":
                    return lambda x: a * np.e ** x
                elif parts[0] == "x":  # ???
                    return lambda x: a * x ** x
                elif parts[0] == "":
                    return lambda x: a ** x
            else:
                b = int(parts[1])
                if parts[0] == "sin":
                    return lambda x: a * np.sin(x) ** b
                elif parts[0] == "cos":
                    return lambda x: a * np.cos(x) ** b
                elif parts[0] == "tan":
                    return lambda x: a * np.tan(x) ** b
                elif parts[0] == "pi":
                    return lambda x: a * np.pi ** b
                elif parts[0] == "e":
                    return lambda x: a * np.e ** b
                elif parts[0] == "x":  # ???
                    return lambda x: a * x ** b
        else:
            print("part 0:", parts[0])
            if parts[0] == "sin":
                return lambda x: a * np.sin(x)
            elif parts[0] == "cos":
                return lambda x: a * np.cos(x)
            elif parts[0] == "tan":
                return lambda x: a * np.tan(x)
            elif parts[0] == "pi":
                return lambda x: a * np.pi
            elif parts[0] == "e":
                return lambda x: a * np.e
            elif parts[0] == "x":  # ???
                return lambda x: a * x
