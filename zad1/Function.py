import re


class Function:
    factors = list()
    funcs = list()

    def __init__(self, s: str):
        s = re.sub(' ', '', s)
        print(s)
        s = re.sub('\+', ' ', s)
        print(s)
        s = re.sub('-', ' -', s)
        print(s)
        s = re.sub('\( -', '(-', s)
        # s = re.sub('\^-?[0-9]', '', s)
        # print(s)
        s = re.sub('-x', '-1x', s)
        print(s)
        # s = re.sub('^x', '1x', s)
        # print(s)
        s = re.sub('[^\d|^(]x', ' 1x', s)
        print(s)
        # s = re.sub('x', '', s)
        # print(s)
        #
        char_list = list(str.split(s))
        print(char_list)

        for fn in char_list:
            if re.search('sin', fn):
                print("sinus: ", fn)
            elif re.search('cos', fn):
                print("cosinus: ", fn)
            elif re.search('tan', fn):
                print("tangens: ", fn)
            elif re.search('e\^x', fn):
                print("e do x:", fn)
            # elif re.search('x\^?$', fn):
            #     print("mam: ", fn)
            elif re.search('x\^?\d+?|(\(-\d+\))?$', fn):
                fn = re.sub('x', '', fn)
                fn = re.sub('\^?\d+$', '', fn)
                if re.search('\d', fn):
                    print("jednomian: ", fn)
                else:
                    fn += '1'
                    print("jednomian: ", fn)
                # self.factors.append()
            elif re.search('\d+', fn):
                print("stala: ", fn)

        # self.factors = list(map(float, char_list))

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
