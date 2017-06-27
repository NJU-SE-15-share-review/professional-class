# -*- coding:utf-8 -*-

# 几何分布的一种定义为：每次伯努利试验成功的概率为p，试验k次才得到第一次成功的概率。下面模拟了每次伯努利试验成功的概率为0.2，分别求经过1、2...、10次才得到第一次成功的概率。在上述基础上，利用成功次数作为x轴，相应概率值作为y轴，画出其直方图，可大概体现几何分布的概率质量图的特征。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如每次成功概率为3/4，最多经过100次伯努利试验才得到第一次成功，怎么修改代码中genom函数、arange函数的参数呢？
# （3）设想一种可使用几何分布计算概率的情景，并用代码实现吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.geom(p)函数返回符合几何分布的离散随机变量rv,每次成功的概率为p，经常配合使用rv.pmf(x)计算其概率质量值，参数x为序列
# （3）numpy.arange(start,stop,step)返回给定step间隔的[start,stop)之间的均匀分布值序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom as G


def geom_pmf():
    rv = G(0.2)  # probability of success is 0.2
    x = np.arange(1, 11, 1)  # return evenly spaced values within 1 interval between [1,11)
    y = rv.pmf(x)  # probability mass function

    plt.bar(x, y, width=0.6, color='grey')  # make bar chart
    plt.savefig('fig.png')


# the code should not be changed
if __name__ == '__main__':
    geom_pmf()