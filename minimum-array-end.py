import math


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        zeros = n - 1
        result = 0
        for i in range(64):
            if x & 1 << i:
                result = result ^ 1 << i
            else:
                result = result ^ ((zeros & 1) << i)
                zeros >>= 1
        return result


print(Solution().minEnd(n=6715154, x=7193485))
