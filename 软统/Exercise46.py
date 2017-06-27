# -*- coding:utf-8 -*-



from scipy.stats import chi2


class Solution():
    def solve(self):
        count = [43, 21, 35]
        x2 = 0.0
        for i in range(3):
            x2 += ((count[i] - 33) ** 2)*1.0/ 33.0
        de = chi2.ppf(0.05, 2)
        if x2 >= de:
            return [2, round(x2, 2), False]
        else:
            return [2, round(x2, 2), True]


if __name__ == '__main__':
    S = Solution()
    print S.solve()