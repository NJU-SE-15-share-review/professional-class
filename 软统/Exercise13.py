# -*- coding:utf-8 -*-

# 下面模拟了期望值分别为0、-5、0，标准差分别为1、1、3的正态分布随机变量rv1、rv2、rv3。并在[-10,10]平均间隔地取100个值作为随机值。在上述基础上，利用随机值作为x轴，相应概率值作为y轴，画出其直方图，可大概体现正态分布的概率密度图的特征。请完成如下练习：
# （1）请仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如描述期望值为3，标准差为5的正态分布，怎么修改代码中norm函数的参数呢？
# （3）设想一种可使用正态分布计算概率的情景，并用代码实现吧！

# （1）此题为普通编程练习题
# （2）scipy.stats.norm(loc,scale)函数返回符合正态分布的期望值为loc、标准差为scale的随机变量rv，经常配合使用rv.pdf(x)计算其概率密度值，参数x为序列
# （3）numpy.linspace(start,stop,num)返回[start,stop)之间的均匀间隔的num个数字组成的序列

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as N


def norm_pdf():
    x = np.linspace(-10, 10, 100)  # return evenly spaced samples, calculated over the interval [-10,10]
    rv1 = N(loc=0, scale=1)  # the mean is 0, the standard deviation is 1
    rv2 = N(loc=-5, scale=1)  # the mean is -5, the standard deviation is 1
    rv3 = N(loc=0, scale=3)  # the mean is 0, the standard deviation is 3



    plt.plot(x, rv1.pdf(x), color='green')  # make chart
    plt.plot(x, rv2.pdf(x), color='blue')  # make chart
    plt.plot(x, rv3.pdf(x), color='red')  # make chart
    plt.savefig('fig.png')


# the code should not be changed
if __name__ == '__main__':
    norm_pdf()
