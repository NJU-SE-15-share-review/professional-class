# -*- coding:utf-8 -*-

# A 95% confidence interval for a population mean, u, is given as (18.985, 21.015).
# This confidence interval is based on a simple random samples of 36 observations. Calculate the sample mean and standard deviation.
# Assume that all conditions necessary for inference are satisfied. Use the t-distribution in any calculations.
from __future__ import print_function
import numpy as np
from scipy.stats import t


class Solution():
    def solve(self):
        upper = 21.015
        lower = 18.985
        de = t.ppf(0.025, 35)
        mean = (upper + lower) / 2
        s = np.sqrt(36) * (upper - lower) / (2 * (-de))
        return [round(mean, 2), round(s, 2)]


if __name__ == '__main__':
    S = Solution()
    print(S.solve())

