# -*- coding:utf-8 -*-

# 下面为t分布的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）替换df为不同的自由度，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）matplotlib.pyplot.subplot(nrows,ncols,plot_number)生成nrows * ncols 个subplot并返回plot_number所指定plot
# （3）numpy.linspace(start,end,num=50)返回start到end之间num个等间距数字
# （4）scipy.stats.t.pdf(x,df)概率密度函数
# （5）scipy.stats.norm.rvs()返回符合标准正态分布的随机变量
# （6）scipy.stats.chi2.rvs(df)返回自由度为df的卡方分布的随机变量

import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t
import matplotlib.pyplot as plt


def t_distribution():
    fig, ax = plt.subplots(1, 1)
    # display the probability density function
    df = 10
    x = np.linspace(-4, 4, 100)
    ax.plot(x, t.pdf(x, df))

    # simulate the t-distribution
    y = []
    for i in range(1000):
        rx = norm.rvs()
        ry = chi2.rvs(df)
        rt = rx / np.sqrt(ry / df)
        y.append(rt)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('t_distribution.png')


# the code should not be changed
if __name__ == '__main__':
    t_distribution()