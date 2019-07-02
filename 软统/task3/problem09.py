# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from __future__ import print_function
from scipy.stats import chi2
import numpy as np

class Solution():
    def solve(self):
        n = 3
        n_i = [43, 21, 35]
        stat_value = 0
        avg = np.array(n_i).mean()
        for i in n_i:
            stat_value += (i - avg) ** 2 / avg
        chi2_value = chi2.isf(0.05, n - 1)
        return [round(n - 1, 2), round(stat_value, 2), not stat_value >= chi2_value]

print(Solution().solve())
