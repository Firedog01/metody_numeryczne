import re
import numpy as np


def make_list(s):
    s = re.sub(' ', '', s)
    s = re.sub(r'\+', ' ', s)
    s = re.sub('-', ' -', s)
    s = re.sub(r'\( -', '(-', s)
    s = re.sub('-x', '-1x', s)
    s = re.sub(r'[^\d|^(]x', ' 1x', s)
    fn_list = list(str.split(s))

    #TODO: Make it work
    # Function could have no '1' or '-1' at the beginning (and it's a problem)
    for fn in fn_list:
        if re.search(r'^x', fn) or re.search(r'^-[a-z]', fn):
            print(fn)
        if re.search(r'^-[^\d]', fn):
            fn = re.sub('^-', '-1', fn)
        elif re.search('^[a-z]', fn):
            fn = '1' + fn

    return fn_list


def make_lambda(fn):

    # Trigonometry
    if re.search('sin', fn):
        # print("sinus: ", fn)
        a = re.sub(r'sin\(x\)', '', fn)
        return lambda x: float(a) * np.sin(x)
    elif re.search('cos', fn):
        # print("cosinus: ", fn)
        a = re.sub(r'cos\(x\)', '', fn)
        return lambda x: float(a) * np.cos(x)
    elif re.search('tan', fn):
        # print("tangens: ", fn)
        a = re.sub(r'tan\(x\)', '', fn)
        return lambda x: float(a) * np.tan(x)

    # e^x
    elif re.search(r'e\^x', fn):
        # print("e do x:", fn)
        a = re.sub(r'e\^x', '', fn)
        return lambda x: float(a) * np.exp(x)

    # Constant
    elif not re.search(r'x', fn):
        # print("stala: ", fn)
        return lambda x: float(fn)

    # ax^p
    elif re.search(r"x\^?\d+?|(\(-\d+\))?$", fn):
        print("jedn: ", fn)
        a = re.sub('x', '', fn)
        p = a
        a = re.sub(r'\^-?(\d+|\(-?\d+\))$', '', a)
        print("mian: ", a)
        p = re.sub(a, '', p)
        p = re.sub(r'\^\(?', '', p)
        p = re.sub(r'\)?', '', p)
        if p == '':
            p = '1'
        print("pow:", p)
        print(a, "x", p)
        return lambda x: float(a) * (float(x) ** float(p))


# TODO: Make it work
def is_polymonial(fn_list: list):
    for fn in fn_list:
        if not re.match(r"\^\d+", fn) and not re.match(r"x", fn):
            return False
    return True


class Function:
    funcs = list()

    # Divide string into list and transform into lambdas
    def __init__(self, s: str):
        # Rn it doesn't care if it's polymonial (but it should)
        fn_list = make_list(s)
        for fn in fn_list:
            self.funcs.append(make_lambda(fn))

    def value(self, x: float):
        ret = 0
        for fn in self.funcs:
            ret += fn(x)
        return ret

    # def value(self, x: float):
    #     ret = self.factors[0]
    #     for i in range(1, len(self.factors)):
    #         ret = ret * x + self.factors[i]
    #     return ret
