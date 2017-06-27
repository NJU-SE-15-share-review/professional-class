# -*- coding:utf-8 -*-

# 铁路公司将它所有的火车头都进行了编号，从1到N。有一天你看见一个编号为60的火车头，那该铁路公司共有多少火车头呢？
# 试用极大似然估计、最小偏方差估计、无偏估计分别估算火车头数目x，并重复10000次试验，计算命中率、均偏方差(x-N)^2、均偏差(x-N)并进行比较，体会各种估计方法的优缺点。
# 下面为火车头问题的python实现，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？
# （2）假如你看到了两辆火车，编号分别为46、24，那么如何进行参数估计呢？（提示：多次估算计算平均值or修改估算公式？）
# （3）假如你看到了多辆（多于两辆）火车呢？

import random

def number_trans(upper_bound):
    return random.randint(1, upper_bound)


def train_seen(N):
    return random.randint(1, N)


def MLE_estimation(evidence):
    return evidence


def MSE_estimation(evidence):
    return round(1.5 * evidence)


def ME_estimation(evidence):
    return 2 * evidence


def estimate():
    number_experiments = 10000
    upper_bound = 100
    H1 = H2 = H3 = MSE1 = MSE2 = MSE3 = ME1 = ME2 = ME3 = 0.0

    for j in range(number_experiments):
        # 返回一个1-100的数作为实际火车头数
        N = number_trans(upper_bound)
        # 看到的火车头数（题目中为60）
        evidence = train_seen(N)

        hypo1 = MLE_estimation(evidence)
        hypo2 = MSE_estimation(evidence)
        hypo3 = ME_estimation(evidence)

        # calculating hits
        H1 = H1 + 1 if hypo1 == N else H1
        H2 = H2 + 1 if hypo2 == N else H2
        H3 = H3 + 1 if hypo3 == N else H3

        # calculating mean squared error
        MSE1 = MSE1 + (hypo1 - N) ** 2
        MSE2 = MSE2 + (hypo2 - N) ** 2
        MSE3 = MSE3 + (hypo3 - N) ** 2

        # calculating mean error
        ME1 = ME1 + (hypo1 - N)
        ME2 = ME2 + (hypo2 - N)
        ME3 = ME3 + (hypo3 - N)

    print (H1 / number_experiments)
    print (H2 / number_experiments)
    print (H3 / number_experiments)
    print (MSE1 / number_experiments)
    print (MSE2 / number_experiments)
    print (MSE3 / number_experiments)
    print (ME1 / number_experiments)
    print (ME2 / number_experiments)
    print (ME3 / number_experiments)


# the code should not be changed
if __name__ == '__main__':
    estimate()