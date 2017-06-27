# -*- coding:utf-8 -*-

# 下面为样本均值抽样分布-norm分布的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）使用其他分布替代norm分布，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）matplotlib.pyplot.subplot(nrows,ncols,plot_number)生成nrows * ncols 个subplot并返回plot_number所指定plot
# （3）numpy.linspace(start,end,num=50)返回start到end之间num个等间距数字
# （4）scipy.stats.norm.pdf(x)概率密度函数
# （5）scipy.stats.norm.rvs(loc=0,scale=1,size=1)函数返回size个符合正态分布的随机变量，其数学期望为loc，标准差为scale

import sys
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    # display the probability density function
    x = np.linspace(-4, 4, 100)
    ax.plot(x, norm.pdf(x))

    # simulate the sampling distribution
    y = []
    n = 100
    for i in range(1000):
        r = norm.rvs(loc=5, scale=2, size=n)
        rsum = np.sum(r)
        z = (rsum - n * 5) / np.sqrt(n * 4)
        y.append(z)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('sampling_distribution.png')


# the code should not be changed
if __name__ == '__main__':
    sampling_distribution()
