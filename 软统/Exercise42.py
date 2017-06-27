# -*- coding:utf-8 -*-

# Georgianna claims that in a small city renowned for its music school, the average child takes at least 5 years of piano lessons.
# We have a random sample of 20 children from the city with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years.
# Evaluate Georgianna's claims using a hypothesis test. alpha is 0.05.

import numpy as np
from scipy.stats import t

class Solution():
    def solve(self):
        de=t.ppf(0.05,19)
        result=(4.6-5)/(2.2/np.sqrt(20))
        if de<=result :
            return [round(19,2),round(result,2),True]
        else:
            return [round(19,2),round(result,2),False]
