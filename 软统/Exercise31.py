# -*- coding:utf-8 -*-

# 下面为独立同分布的中心极限定理，拉普拉斯定理的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）试调整二项分布的参数，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）scipy.stats.binom.rvs(n,p,size=1)函数返回size个符合二项分布的随机变量,其独立试验次数为n，每次成功的概率为p

import sys
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


def central_limit_theorem():
    y = []
    n = 100
    for i in range(1000):
        r = binom.rvs(n, 0.3)
        rsum = np.sum(r)
        z = (rsum - n * 0.3) / np.sqrt(n * 0.3 * 0.7)
        y.append(z)

    plt.hist(y, color='grey')
    plt.savefig('central_limit_theorem.png')


# the code should not be changed
if __name__ == '__main__':
    central_limit_theorem()