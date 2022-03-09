import re

class Function:
    factors = list()

    def __init__(self, s: str):
        print(s)
        # s = re.sub('\^\-?[0-9]', '', s)
        # s = re.sub('[^\d]x', '1', s)
        # s = re.sub()
        #s = re.sub('\*x\^\d+', '', s)
        #s = re.sub('x(\^\d+|)', '1', s)

        # s = s.replace(x^[])

        # s = s.replace(" ", "")
        # s = s.replace("x", "")
        # s = s.replace("^", "")
        # s = s.replace("+", " ")
        # s = s.replace("-", " -")
        # print(s)
        char_list = list(str.split(s))
        self.factors = list(map(float, char_list))
        print(self.factors)
        pass

    def value(self, x: float):
        ret = 0
        for i in range(len(self.factors)):
            ret = ret * x + n
        return ret
