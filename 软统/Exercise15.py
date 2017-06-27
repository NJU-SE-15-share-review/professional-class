# -*- coding:utf-8 -*-

# 累计分布CDF是指随机变量小于或者等于某个数值的概率P（X<=x），即F(x)=P(X<=x)，为概率密度函数PDF的积分，下面模拟了服从参数1.0的指数分布随机变量rv，并分别求取其PDF、CDF值作为y轴，画出其直方图，比较PDF、CDF的特征。请完成如下练习：
# \n\t（1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）怎么画出期望值为1.0，标准差为2.0满足正态分布的随机值的PDF和CDF呢？

# （1）此题为普通编程练习题
# （2）scipy.stats.expon(scale)函数返回符合指数分布的参数为scale的随机变量rv，经常配合使用rv.pdf(x)计算其概率密度值，使用rv.cdf(x)计算其累计概率密度值，参数x为序列
# （3）numpy.linspace(start,stop,num)返回[start,stop)之间的均匀间隔的num个数字组成的序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E


def expon_cdf_pdf():
    x = np.linspace(0, 5, 100)  ##return evenly spaced samples, calculated over the interval [0,5]
    rv = E(scale=1)  # the scale is 1

    plt.plot(x, rv.pdf(x), color='blue')  # make pdf chart
    plt.plot(x, rv.cdf(x), color='red')  # make cdf chart
    plt.savefig('fig.png')


# the code should not be changed
if __name__ == '__main__':
    expon_cdf_pdf()