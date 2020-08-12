# -*- coding:utf-8 -*-
# The table below summaries a data set that examines the response of a random sample
# of college graduates and non-graduate on the topic of oil drilling.
# Complete a chi-square test for test data to check
# whether there is a statistically significant difference in responses
# from college graduates and non-graduates.
# College Grad? 	Yes 	No 	    Total
# Support 	        154 	132 	286
# Oppose 	        180 	126 	306
# Do not know 	    104 	131 	235
# Total 	        438 	389 	827
from __future__ import print_function
import numpy as np
from scipy.stats import chi2

class Solution():
    def solve(self):
        count_exp = [[154, 132], [180, 126], [104, 131]]
        count_the = np.ndarray((3, 2))
        total_r = [286, 306, 235]
        total_c = [438, 389]
        for i in range(3):
            for j in range(2):
                count_the[i][j] = total_r[i] * total_c[j] / 827.0

        x2 = 0.0
        for i in range(3):
            for j in range(2):
                x2 += (count_exp[i][j] - count_the[i][j]) ** 2 / count_the[i][j]

        de = chi2.ppf(0.95, 2)   # (r-1)*(c-1)
        if x2 >= de:
            return [2, round(x2, 2), False]
        else:
            return [2, round(x2, 2), True]


print(Solution().solve())
