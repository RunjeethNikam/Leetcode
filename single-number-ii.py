from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = [0] * 64
        for num in nums:
            if num < 0:
                f[-1] += 1
                num = -num
            i = 0
            while num:
                f[i] += num % 2
                num //= 2
                i += 1
        i = 0
        f[-1] %= 3
        while i < 63:
            f[i] = f[i] % 3
            i += 1
        result = 0
        for index, value in enumerate(f):
            if index < 63:
                result += value * (2 ** index)
        if f[-1] > 0:
            result = -result
        return result

print(Solution().singleNumber([1,1,1,-3]))

