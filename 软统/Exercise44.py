# -*- coding:utf-8 -*-

# A group of researchers are interested in the possible effects of distracting stimuli during eating, such as an increase or decrease in the amount of food consumption.
# To test this hypothesis, they monitored food intake for a group of 44 patients who were randomised into two equal groups.
# The treatment group ate lunch while playing solitaire, and the control group ate lunch without any added distractions.
# Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of 45.1 grams, and patients in the control group ate 27.1 grams of biscuits with a standard deviation of 26.4 grams.
# Do these data provide convincing evidence that the average food intake is different for the patients in the treatment group? Assume the conditions for inference are satisfied.
#  Null hypothesis is H0: u_t - u_c = 0, alpha is 0.05

import numpy as np
from scipy.stats import t

#p186,基于成对数据的检验
class Solution():
    def solve(self):
        # de=t.ppf(0.025,42)
        de=t.ppf(0.025,21)
        mean=52.1-27.1
        s=np.sqrt(45.1**2+26.4**2)  #D(X-Y) = D(X) + D(Y)
        # result=(mean-0)/(s/np.sqrt(1/11))
        result = (mean-0)  / (s / np.sqrt(22))
        if (de<=result) & (result<=-de):
            return [round(21,2),round(result,2),True]
        else:
            return [round(21, 2), round(result, 2), False]


if __name__ == '__main__':
    S = Solution()
    print S.solve()
