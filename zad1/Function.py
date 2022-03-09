import re

class Function:
    factors = list()

    def __init__(self, s: str):
        char_list = list(str.split(s))
        self.factors = list(map(float, char_list))
        print(self.factors)
        pass

    def value(self, x: float):
        ret = self.factors[0]
        for i in range(1, len(self.factors)):
            ret = ret * x + self.factors[i]
        return ret
