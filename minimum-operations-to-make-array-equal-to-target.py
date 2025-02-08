from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        def same_sign(a, b):
            return a * b >= 0

        def check(a, b, given):
            remaining = 0
            last = 0
            count = 0
            for num in given:
                if last >= 0 and num >= 0:
                    if num >= last:
                        remaining = num
                    else:
                        count += remaining
                        remaining = last - num
                # else:
                #     count += remaining
            return count

        a = []
        low = 0
        high = 0
        for n, t in zip(nums, target):
            diff = t - n
            a.append(diff)
            high = max(high, abs(diff))

        while low < high:
            mid = (low + high) // 2
            if check(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        rararararararar
