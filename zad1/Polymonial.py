class Polymonial:
    factors = list()

    def __init__(self, factors):
        self.factors = factors

    def value(self, x: float):
        ret = 0
        for a in self.factors[:-1]:
            ret += a
            ret *= x
            print(ret)
        ret += self.factors[-1]
        return ret