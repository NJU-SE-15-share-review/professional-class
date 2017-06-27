# -*- coding:utf-8 -*-
# 二项分布是最重要的离散概率分布之一。假设有一种只有两个结果的试验，其成功概率为p,那么二项分布描述了进行n次伯努利试验，成功k次的概率。下面模拟了进行10次伯努利试验，每次成功概率为0.5，分别求最后成功次数为0、1、2...、10次的概率。在上述基础上，利用成功次数作为x轴，相应概率值作为y轴，画出其直方图，可大概体现二项分布的概率质量图的特征。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如进行100次伯努利试验，每次成功概率为1/6，怎么修改代码中binom函数、arange函数的参数呢？
# （3）设想一种可使用二项分布计算概率的情景，并用代码实现吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.binom(n,p)函数返回符合二项分布的离散随机变量rv,其独立试验次数为n，每次成功的概率为p，经常配合使用rv.pmf(x)计算其概率质量值，参数x为序列
# （3）numpy.arange(start,stop,step)返回给定step间隔的[start,stop)之间的均匀分布值序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as B


def binom_pmf():
    rv = B(100, 1.0/6)  # 10 independent trials, probability of success is 0.5
    x = np.arange(0, 101, 1)  # return evenly spaced values within 1 interval between [0,11)
    y = rv.pmf(x)  # probability mass function

    plt.bar(x, y, width=0.6, color='grey')  # make bar chart
    plt.savefig('fig.png')


# the code should not be changed
if __name__ == '__main__':
    binom_pmf()
