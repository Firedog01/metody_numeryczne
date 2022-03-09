import re


class Function:
    factors = list()

    def __init__(self, s: str):
        s = re.sub(' ', '', s)
        s = re.sub('\+', ' ', s)
        s = re.sub('-', ' -', s)
        s = re.sub('\^-?[0-9]', '', s)
        s = re.sub('-x', '-1', s)
        s = re.sub('^x', '1', s)
        s = re.sub('[^\d]x', ' 1', s)
        s = re.sub('x', '', s)

        char_list = list(str.split(s))
        self.factors = list(map(float, char_list))

    def value(self, x: float):
        ret = 0
        for a in self.factors[:-1]:
            ret += a
            ret *= x
            print(ret)
        ret += self.factors[-1]
        return ret

    # def value(self, x: float):
    #     ret = self.factors[0]
    #     for i in range(1, len(self.factors)):
    #         ret = ret * x + self.factors[i]
    #     return ret
