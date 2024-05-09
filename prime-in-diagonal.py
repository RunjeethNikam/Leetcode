from typing import List
import math


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        # lt = []
        # x = set()
        # for i in range(len(nums)):
        #     if (i, i) not in x:
        #         lt.append(nums[i][i])
        #         x.add((i, i))

        # for i in range(len(nums)):
        #     if (i, len(nums) - i - 1) not in x:
        #         lt.append(nums[i][len(nums) - i - 1])
        #         x.add((i, len(nums) - i - 1))

        lt=[]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i==j:
                    lt.append(nums[i][j])
                    lt.append(nums[i][len(nums)-1-i])

        result = 0
        for item in lt:
            for j in range(2, math.ceil(math.sqrt(item))):
                if item % j == 0:
                    break
            else:
                result = max(result, item)
        return result
