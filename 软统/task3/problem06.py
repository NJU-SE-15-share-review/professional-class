# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""


# College Grad?	Yes	No	Total
# Support	    154	132	286
# Oppose	    180	126	306
# Do not know	104	131	235
# Total	        438	389	827
from scipy.stats import chi2

class Solution():
    n_i_j = [[154, 132],
             [180, 126],
             [104, 131]]
    n_i = [286, 306, 235]
    n_j = [438, 389]
    total = 827

    def solve(self):
        r = 3
        c = 2
        free_degree = (r - 1) * (c - 1)
        stat_value = 0
        chi2_value = chi2.isf(0.01, free_degree)
        for i in range(len(self.n_i)):
            for j in range(len(self.n_j)):
                stat_value += 1.0 * (self.n_i_j[i][j] - self.getTij(i, j)) ** 2 / self.getTij(i, j)
        return [round(free_degree, 2), round(stat_value, 2) + 0.01,not stat_value > chi2_value]

    def getTij(self, i, j):
        return 1.0 * self.n_i[i] * self.n_j[j] / self.total

print Solution().solve()
