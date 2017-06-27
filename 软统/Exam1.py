#-*- coding:utf-8 -*-


class Solution():
    def describe(self, a):
        n = len(a)
        if n == 0:
            return [None, None, None, None]

        mean = 0.000000
        var = 0.000000
        skew = 0.000000
        kurt = 0.000000

        svar = 0.000000

        for i in a:
            mean += i
        mean = mean / n

        if n == 1:
            return [round(mean, 6), None, 0, -3]

        for i in a:
            var += (i - mean) ** 2
        var = var / (n - 1)
        for i in a:
            svar += (i - mean) ** 2
        svar = svar / n

        if var == 0:
            return [round(mean, 6), round(var, 6), None, None]

        for i in a:
            skew += (i - mean) ** 3
            kurt += (i - mean) ** 4
        skew = skew / n
        kurt = kurt / n
        skew = skew / (svar ** 1.5)
        kurt = kurt / (svar ** 2)

        result = [round(mean, 6), round(var, 6), round(skew, 6), round(kurt - 3, 6)]
        return result
