# -*- coding:utf-8 -*-

# 皮尔森相关系数用于度量两个变量之间相关程度，介于-1到1之间，其中-1表示完全负相关，0表示无关，1表示完全正相关。下面为皮尔森相关系数的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）试试自己构造其他变量组X、Y，并计算它们之间的皮尔森相关系数？

# （1）此题为普通编程练习题
# （2）scipy.stats.pearsonr(x,y)计算x,y之间的相关系数，此外，并返回p-value值

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def pearsonr():
    x = np.linspace(-5, 5, num=150)
    y = x + np.random.normal(size=x.size)
    y[12:14] += 10

    print (stats.pearsonr(x, y))
    plt.scatter(x, y)
    plt.savefig('pearsonr.png')


# the code should not be changed
if __name__ == '__main__':
    pearsonr()