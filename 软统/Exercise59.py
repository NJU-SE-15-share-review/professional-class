# -*- coding:utf-8 -*-

# 对于一个包含一系列数字字符串的列表，寻找其中的回文串存入一个列表中并返回

class Solution():
    def solve(self, A):
        # use isPalindrom function to check if the string is palindrome or not
        result = []
        for i in A:
            if (self.isPalindrome(i) == True):
                result.append(i)
        return result

    def isPalindrome(self, x):
        mark = True
        length = len(x)
        for i in range(length / 2):
            if x[i] != x[length - 1 - i]:
                mark = False
        return mark


if __name__ == '__main__':
    A = ['123', '232', '4556554', '12123', '3443', '1314131']
    S = Solution()
    print S.solve(A)
