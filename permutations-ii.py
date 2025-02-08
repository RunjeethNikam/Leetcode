from typing import List
from typing import Counter
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(selected: List[int], counter: Counter):
            if len(selected) == len(nums):
                result.append(selected[:])
                return
            for item in counter.keys():
                if counter[item] > 0:
                    counter[item] -= 1
                    selected.append(item)
                    solve(selected, counter)
                    selected.pop()
                    counter[item] += 1

        solve([], Counter(nums))
        return result


print(Solution().permuteUnique(nums=[1, 2, 3]))
