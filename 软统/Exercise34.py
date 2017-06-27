# -*- coding:utf-8 -*-

# 下面为F分布的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）替换dfn,dfd为不同的自由度，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）matplotlib.pyplot.subplot(nrows,ncols,plot_number)生成nrows * ncols 个subplot并返回plot_number所指定plot
# （3）numpy.linspace(start,end,num=50)返回start到end之间num个等间距数字
# （4）scipy.stats.f.ppf(q,dfn,dfd)是ccf函数的反函数，计算自由度为dfn和dfd的F分布累积概率值为q时的随机变量值
# （5）scipy.stats.f.pdf(x,dfn,dfd)概率密度函数
# （6）scipy.stats.chi2.rvs(df)返回自由度为df的卡方分布的随机变量

import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import f
import matplotlib.pyplot as plt


def F_distribution():
    fig, ax = plt.subplots(1, 1)
    # display the probability density function
    dfn, dfm = 10, 5
    x = np.linspace(f.ppf(0.01, dfn, dfm), f.ppf(0.99, dfn, dfm), 100)
    ax.plot(x, f.pdf(x, dfn, dfm))

    # simulate the F-distribution
    y = []
    for i in range(1000):
        rx = chi2.rvs(dfn)
        ry = chi2.rvs(dfm)
        rf = np.sqrt(rx / dfn) / np.sqrt(ry / dfm)
        y.append(rf)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('F_distribution.png')


# the code should not be changed
if __name__ == '__main__':
    F_distribution()