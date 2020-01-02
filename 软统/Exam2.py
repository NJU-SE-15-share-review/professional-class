#-*- coding:utf-8 -*-

#中国人平均睡眠时长为8.5小时，这是从3600份问卷统计得到的结果。另外报告指出，中国人睡眠时长符合方差为25的正态分布
#试写solve函数估计中国人睡眠时长的置信区间（置信水平95%）
from __future__ import print_function
import numpy as np
from scipy.stats import norm

class Solution:
    def solve(self):
        de = norm.ppf(0.025)
        lower = 8.5+5/np.sqrt(3600)*de
        upper = 8.5-5/np.sqrt(3600)*de
        return [lower,upper]

if __name__ == '__main__':
    S = Solution()
    print(S.solve())