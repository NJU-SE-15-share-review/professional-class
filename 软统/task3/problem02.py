# -*- coding:utf-8 -*-
# A 95% confidence interval for a population mean, u, is given as (18.985, 21.015). This confidence interval is based on a simple random
# samples of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are
# satisfied. Use the t-distribution in any calculations.
from scipy.stats import t
import math


class Solution():
    def solve(self):
        lower = 18.985
        upper = 21.015
        mean = (lower + upper) / 2
        delta = mean - lower
        n = 36
        t_value = t.isf(0.025, n - 1)
        std = delta * math.sqrt(n) / t_value
        return [round(mean, 2), round(std, 2)]


print Solution().solve()