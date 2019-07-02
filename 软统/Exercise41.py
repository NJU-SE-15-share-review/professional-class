# -*- coding:utf-8 -*-

# New York is known as "the city that never sleeps".
# A random sample of 25 New Yorkers were asked how much sleep they get per night. Statistical summaries of these data are shown below.
# Do these data provide strong evidence that New Yorkers sleep less than 8 hours per night on average? Null-hypothesis is H0: u=8, and alpha is 0.05
# n  mean stand-variance  min    max
# 25 7.73 0.77           6.17   9.78

from __future__ import print_function
import numpy as np
from scipy.stats import t


class Solution():
    def solve(self):
        de = t.ppf(0.05, 24)
        result = (7.73 - 8) / (0.77 / np.sqrt(25))
        if de <= result:
            return [24, round(result, 2), True]
        else:
            return [24, round(result, 2), False]


if __name__ == '__main__':
    S = Solution()
    print(S.solve())
