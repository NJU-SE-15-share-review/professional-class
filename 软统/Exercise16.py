# -*- coding:utf-8 -*-

# 下面利用exp(lam)函数指数分布的计算公式返回服从参数lam的指数分布的随机变量概率值，并分别在[0,1]和[0,5]之间的均匀间隔地取100个值分别作为x轴，利用自定义exp(lam)函数和内置expon()函数求出的相应概率值作为y轴，画出其直方图，对比分析。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）怎么求取期望值为1.0，标准差为2.0满足正态分布的随机值呢？tips：自定义norm函数
# （3）试着自定义binom、geom、poisson函数吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.expon(scale)函数返回符合指数分布的参数为scale的随机变量rv，经常配合使用rv.cdf(x)计算其累计概率密度值，参数x为序列
# （3）numpy.linspace(start,stop,num)返回[start,stop)之间的均匀间隔的num个数字组成的序列
# （4）random.random()函数返回[0,1)之间的浮点数

import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E


def exp(lam):
    p = random.random()  # return float in [0,1)
    return -math.log(1 - p) / lam  # calculate expon value




# the code should not be changed
if __name__ == '__main__':
    # generate 100 random variables calculated by self-defined exp function
    x1 = []
    for i in range(100):
        x1.append(exp(1))
    x1 = sorted(x1)
    y1 = np.linspace(0, 1, 100)
    plt.plot(x1, y1, color='blue')

    # generate 100 random varaibles calculated by inner-defined expon function
    rv = E(scale=1)
    x2 = np.linspace(0, 5, 100)
    plt.plot(x2, rv.cdf(x2), color='red')
    plt.savefig('fig.png')  # make chart
