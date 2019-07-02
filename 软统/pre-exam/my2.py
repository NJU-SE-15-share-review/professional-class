from __future__ import print_function
import csv
import urllib
import pandas as pd
from scipy.stats import t
from scipy.stats import chi2
import math

class Solution():
    def solve(self):
        filename_old = "http://py.mooctest.net:8081/dataset/population/population_old.csv"
        filename_total = "http://py.mooctest.net:8081/dataset/population/population_total.csv"
        reader_old = csv.reader(urllib.urlopen(filename_old))
        reader_total = csv.reader(urllib.urlopen(filename_total))
        count_line_old = 3
        old_num = []
        for row in reader_old:
            if count_line_old > 0:
                count_line_old -= 1;
                continue;
            old_num.append(int(row[1]))
        count_line_total = 5
        total_num = []
        for row in reader_total:
            if count_line_total > 0:
                count_line_total -= 1
                continue
            total_num.append(int(row[4]))
        old_rate = []
        for i in range(len(old_num)):
            old_rate.append(100.0 * old_num[i-1] / total_num[i-1])

        a = pd.Series(old_rate)
        x = a.mean()
        std = a.std()
        var = a.var() # var = s^2
        z = t.isf(0.05, 31)
        mean_lower = x - std / math.sqrt(31) * z
        mean_upper = x + std / math.sqrt(31) * z
        std_lower = 31 * var / chi2.isf(0.05, 31)
        std_upper = 31 * var / chi2.isf(0.95, 31)
        result = [[mean_lower, mean_upper], [std_lower, std_upper]]
        print(result)
        return result

Solution().solve()