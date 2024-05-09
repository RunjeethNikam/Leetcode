from typing import List


class Solution:
    def bits(self, num):
        count = 0
        while num > 0:
            count += num%2
            num //= 2
        return count


    def canSortArray(self, nums: List[int]) -> bool:
        mx1 = None
        mn1 = None
        mn2 = nums[0]
        mx2 = nums[0]
        lt = self.bits(nums[0])
        for i in range(1, len(nums)):
            bt = self.bits(nums[i])
            if lt == bt:
                mn2 = min(mn2, nums[i])
                mx2 = max(mx2, nums[i])
            else:
                if mx1 is None and mn1 is None:
                    mx1, mn1 = mx2, mn2
                    mx2 = nums[i]
                    mn2 = nums[i]
                else:
                    if mx1 <= mn2:
                        mx1, mn1 = mx2, mn2
                        mx2 = nums[i]
                        mn2 = nums[i]
                    else:
                        return False
            lt = bt
        if mx1 is None and mn1 is None:
            pass
        else:
            if mx1 <= mn2:
                pass
            else:
                return False
        return True

print(Solution().canSortArray([8,4,2,30,15]))