import math
class Solution:

    def power(self, x, n):
        result = 1
        while True:
            i = 1
            temp = x
            while (i * 2) < n:
                temp *= temp
                i *= 2
            if i == n:
                return result * temp
            n -= i
            result *= temp

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            p = self.power(abs(x), n)
            if x < 0 and n %2 == 1:
                return -1/p
            else:
                return 1/p
        else:
            p = self.power(abs(x), n)
            if x < 0 and n %2 ==1:
                return -p
            else:
                return p


print(Solution().myPow(2.1, 3))
