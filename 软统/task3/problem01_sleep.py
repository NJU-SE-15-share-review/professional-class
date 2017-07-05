# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from scipy.stats import norm
import math


class Solution:
    def solve(self):
        avg = 8.5
        # 标准差
        std = math.sqrt(25)
        n = 3600
        z = norm.isf(0.025)
        delta = std / math.sqrt(n) * z
        return [avg - delta, avg + delta]


print Solution().solve()
