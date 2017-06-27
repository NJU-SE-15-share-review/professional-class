# -*- coding:utf-8 -*-

# 单因素方差分析用于推断各样本所代表的各总体均数是否相等。下面为单因素方差分析问题的python模拟实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）仿照oneway_anova函数设计自己的双因素方差分析函数twoway_anova

from scipy import stats
import numpy as np


def oneway_anova():
    A1 = [27.0, 26.2, 28.8, 33.5, 28.8]
    A2 = [22.8, 23.1, 27.7, 27.6, 24.0]
    A3 = [21.9, 23.4, 20.1, 27.8, 19.3]
    A4 = [23.5, 19.6, 23.7, 20.8, 23.9]

    A = [A1, A2, A3, A4]
    n = 20
    As = np.sum(A, axis=1)
    QA = 0.0
    for i in range(4):
        QA = QA + As[i] * As[i]
    QA = QA / 5

    QT = 0.0
    for i in range(4):
        for j in range(5):
            QT = QT + A[i][j] * A[i][j]

    C = np.sum(A) * np.sum(A) / n
    ST = QT - C
    SA = QA - C
    Se = ST - SA
    F = (SA / 3) / (Se / 16)

    print ('QA is ' + str(QA))
    print ('QT is ' + str(QT))
    print ('C is ' + str(C))
    print ('ST is ' + str(ST))
    print ('SA is ' + str(SA))
    print ('Se is ' + str(Se))
    print ('F is ' + str(F))


def twoway_anova():
    pass


# the code should not be changed
if __name__ == '__main__':
    oneway_anova()
    twoway_anova()