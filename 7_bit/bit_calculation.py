#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: bit_calculation.py
@Time: 2020/9/2 20:41
'''


class Solution:
    def add(self, a, b):
        sum = a
        while b != 0:
            sum = a ^ b
            b = (a & b) << 1
            a = sum
        return sum

    def substract(self, a, b):
        b = self.add(~b, 1)
        return self.add(a, b)

    def multiply(self, a, b):
        """
        res初始化为0
        当b的最低位为1时：b右移1位，a左移一位，res加上a；
        当b的最低位为0时：b右移1位，a左移一位，res不变
        直到b等于0时返回，输出res
        """
        res = 0
        while b != 0:
            if (b & 0b1) != 0:
                res += a
            a <<= 1
            b >>= 1
        return res

    def div(self, a, b):
        x = self.add(~a, 1) if a < 0 else a
        y = self.add(~b, 1) if b < 0 else b
        res = 0
        for i in range(31, -1, -1):
            if (x >> i) >= y:
                res |= 1 << i
                x = self.substract(x, y << i)
        return self.add(~res, 1) if a < 0 ^ b < 0 else res

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        if a == float("-inf") and b == float("-inf"):
            return 1
        elif b == float("-inf"):
            return 0
        elif a == float("-inf"):
            res = self.div(self.add(a, 1), b)
            return self.add(res, self.div(self.substract(a, self.multiply(res, b)), b))
        else:
            return self.div(a, b)




s = Solution()
# print(s.multiply(129, 17))
print(s.divide(129, 17))
