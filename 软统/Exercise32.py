# -*- coding:utf-8 -*-

# 下面为卡方分布的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）替换df为不同的自由度，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）matplotlib.pyplot.subplot(nrows,ncols,plot_number)生成nrows * ncols 个subplot并返回plot_number所指定plot
# （3）numpy.linspace(start,end,num=50)返回start到end之间num个等间距数字
# （4）scipy.stats.chi2.ppf(q,df)是ccf函数的反函数，计算自由度为df的卡方分布累积概率值为q时的随机变量值
# （5）scipy.stats.chi2.pdf(x,df)概率密度函数
# （6）scipy.stats.norm.rvs(size=1)返回size个符合标准正态分布的随机变量

import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
import matplotlib.pyplot as plt


def chi2_distribution():
    fig, ax = plt.subplots(1, 1)
    # display the probability density function
    df = 10
    x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 100)
    ax.plot(x, chi2.pdf(x, df))

    # simulate the chi2 distribution
    y = []
    n = 10
    for i in range(1000):
        chi2r = 0.0
        r = norm.rvs(size=n)
        for j in range(n):
            chi2r = chi2r + r[j] ** 2
        y.append(chi2r)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('chi2_distribution.png')


# the code should not be changed
if __name__ == '__main__':
    chi2_distribution()