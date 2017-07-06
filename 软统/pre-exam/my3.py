import csv
import urllib
import numpy as np
from scipy.stats import t

class Solution():
    def solve(self):
        file_2010 = "http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv"
        file_2014 = "http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv"
        reader_2010 = csv.reader(urllib.urlopen(file_2010))
        reader_2014 = csv.reader(urllib.urlopen(file_2014))
        temperature_2010 = []
        i = 0
        for row in reader_2010:
            i += 1
            if i <= 6 or i >= 38:
                continue
            temperature_2010.append(float(row[8]))
        temperature_2014 = []
        i = 0
        for row in reader_2014:
            i += 1
            if i <= 5 or i >= 37:
                continue
            temperature_2014.append(float(row[8]))
        diff = []
        for i in range(len(temperature_2010)):
            diff.append(temperature_2014[i] - temperature_2010[i])
        d = np.mean(diff)
        sd = np.std(diff)
        result = d / (sd / np.sqrt(31))
        t_alpha = t.isf(0.05, 30)
        if result >= t_alpha:
            return "YES"
        else:
            return "NO"

print Solution().solve()