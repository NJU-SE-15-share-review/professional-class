# -*- coding:utf-8 -*-

# 下面为样本方差抽样分布的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）修改正态分布函数norm的参数，看看结果如何变化？

# （1）此题为普通编程练习题
# （2）matplotlib.pyplot.subplot(nrows,ncols,plot_number)生成nrows * ncols 个subplot并返回plot_number所指定plot
# （3）numpy.linspace(start,end,num=50)返回start到end之间num个等间距数字
# （4）scipy.stats.chi2.ppf(q,df)是ccf函数的反函数，计算自由度为df的卡方分布累积概率值为q时的随机变量值
# （5）scipy.stats.chi2.pdf(x,df)概率密度函数
# （6）scipy.stats.norm.rvs(loc=0,scale=1,size=1)函数返回size个符合正态分布的随机变量，其数学期望为loc，标准差为scale

import sys
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm
import matplotlib.pyplot as plt


def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    # display the probability density function
    df = 10
    x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 100)
    ax.plot(x, chi2.pdf(x, df))

    # simulate the sampling distribution
    y = []
    for i in range(1000):
        r = norm.rvs(loc=5, scale=2, size=df + 1)
        rchi2 = (df) * np.var(r) / 4
        y.append(rchi2)

    ax.hist(y, normed=True, alpha=0.2)
    plt.savefig('sampling_distribution.png')


# the code should not be changed
if __name__ == '__main__':
    sampling_distribution()
