# -*- coding:utf-8 -*-

# 下面为独立同分布的中心极限定理的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）试利用其他分布函数验证此中心极限定理。
#
# （1）此题为普通编程练习题
# （2）scipy.stats.expon.rvs(scale=1,size=1)函数返回size个符合指数分布的参数为scale的随机变量

import sys
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt


def central_limit_theorem():
    y = []
    n = 100
    for i in range(1000):
        r = expon.rvs(scale=1, size=n)
        rsum = np.sum(r)
        z = (rsum - n) / np.sqrt(n)
        y.append(z)

    plt.hist(y, color='grey')
    plt.savefig('central_limit_theorem.png')


# the code should not be changed
if __name__ == '__main__':
    central_limit_theorem()