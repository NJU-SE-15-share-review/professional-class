# -*- coding:utf-8 -*-

# 在二项分布中，如果试验次数n很大，每次试验成功概率p很小，其乘积np比较适中时，那么试验成功的次数的概率可以用泊松分布近似描述。在泊松分布中使用λ描述单位时间中随机事件的平均发生率，其中λ=np。下面模拟了事件发生率（每秒内事件平均发生次数）λ为4.5,观察时间为0-10秒的情况。在上述基础上，利用观察时间作为x轴，相应概率值作为y轴，画出其直方图，可大概体现泊松分布的概率质量图的特征。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如单位时间内随机事件的平均发生率为1/3，怎么修改代码中poisson函数的参数呢？
# （3）设想一种可使用泊松分布计算概率的情景，并用代码实现吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.poisson(λ)函数返回符合泊松分布的离散随机变量rv,单位时间内随机事件的平均发生率为λ，经常配合使用rv.pmf(x)计算其概率质量值，参数x为序列
# （3）numpy.arange(start,stop,step)返回给定step间隔的[start,stop)之间的均匀分布值序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson as Pie


def poisson_pmf():
    rv = Pie(4.5)  # the average incident is 4.5
    x = np.arange(0, 11, 1)  # return evenly spaced values within 1 interval between [1,11)
    y = rv.pmf(x)  # probability mass function

    plt.bar(x, y, width=0.6, color='grey')  # make bar chart
    plt.savefig('fig.png')


# the code should not be changed
if __name__ == '__main__':
    poisson_pmf()