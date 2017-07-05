# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
from scipy.stats import t
import math

class Solution():
    def solve(self):
        n = 20
        std = 2.2
        mean = 4.6
        standard = 5
        stat_value =(mean - standard) / (std / math.sqrt(n))
        t_value = t.isf(0.025, n - 1)
        return [round(n - 1, 2), round(stat_value, 2), not stat_value <= -t_value]
