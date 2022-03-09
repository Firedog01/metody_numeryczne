import re
import numpy as np


class Function:
    factors = list()
    funcs = list()

    def __init__(self, s: str):

        s = re.sub(' ', '', s)
        s = re.sub('\+', ' ', s)
        s = re.sub('-', ' -', s)
        s = re.sub('\( -', '(-', s)
        s = re.sub('-x', '-1x', s)
        s = re.sub('[^\d|^(]x', ' 1x', s)

        for fn in list(str.split(s)):
            # Function could have no '1' or '-1' at the beginning
            if re.search('^-[^\d]', fn):
                fn = re.sub('^-', '-1', fn)
                print("a")
            elif re.search('^[a-z]', fn):
                fn = '1' + fn
                print("b")

            # Trigonometry
            if re.search('sin', fn):
                print("sinus: ", fn)
                a = re.sub('sin\(x\)', '', fn)
                self.funcs.append(lambda x: float(a) * np.sin(x))
            elif re.search('cos', fn):
                print("cosinus: ", fn)
                a = re.sub('cos\(x\)', '', fn)
                self.funcs.append(lambda x: float(a) * np.cos(x))
            elif re.search('tan', fn):
                print("tangens: ", fn)
                a = re.sub('tan\(x\)', '', fn)
                self.funcs.append(lambda x: float(a) * np.tan(x))

            # e^x
            elif re.search('e\^x', fn):
                print("e do x:", fn)
                a = re.sub('tan\(x\)', '', fn)
                self.funcs.append(lambda x: float(a) * np.exp(x))

            # ax^p
            elif re.search('x\^?\d+?|(\(-\d+\))?$', fn):
                print("jedn: ", fn)
                a = re.sub('x', '', fn)
                p = a
                a = re.sub('\^-?(\d+|\(-?\d+\))$', '', a)
                print("mian: ", fn)
                p = re.sub(fn, '', p)
                p = re.sub('\^\(?', '', p)
                p = re.sub('\)?', '', p)
                if p == '':
                    p = '1'
                print("pow:", p)
                self.funcs.append(lambda x: float(a) * (x ** p))

    def value(self, x: float):
        ret = 0
        for a in self.factors[:-1]:
            ret += a
            ret *= x
            print(ret)
        ret += self.factors[-1]
        return ret

    def _str_to_list(s: str):
        s = re.sub(' ', '', s)
        s = re.sub('\+', ' ', s)
        s = re.sub('-', ' -', s)
        s = re.sub('\( -', '(-', s)
        s = re.sub('-x', '-1x', s)
        s = re.sub('[^\d|^(]x', ' 1x', s)
        return list(str.split(s))

    # def value(self, x: float):
    #     ret = self.factors[0]
    #     for i in range(1, len(self.factors)):
    #         ret = ret * x + self.factors[i]
    #     return ret
