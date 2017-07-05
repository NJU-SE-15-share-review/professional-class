# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from scipy.stats import t
import math


class Solution():
    def solve(self):
        n = 25
        mean = 7.73
        std = 0.77
        u0 = 8
        stat_value = (mean - u0) / (std / math.sqrt(n))
        t_value = t.isf(0.05, n - 1)
        return [round(n-1, 2), round(stat_value, 2), not math.fabs(stat_value) >= t_value]

print Solution().solve()
