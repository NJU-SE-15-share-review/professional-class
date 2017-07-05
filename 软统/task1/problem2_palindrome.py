# -*- coding:utf-8 -*-
"""
log api example: log('output is: ' + str(output))
"""
# 对于一个包含一系列数字字符串的列表，寻找其中的回文串存入一个列表中并返回


class Solution():
    def solve(self, A):
        # use isPalindrom function to check if the string is palindrome or not
        result = []
        for string in A:
            if self.isPalindrome(string):
                result.append(string)
        return result

    @staticmethod
    def isPalindrome(x):
        length = len(x)
        for i in range(length / 2):
            if x[i] != x[length-i-1]:
                return False
        return True

A = ['123', '232', '4556554', '12123', '3443','1314131']
print Solution().solve(A)
