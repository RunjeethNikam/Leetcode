from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        r1, r2 = -1, -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    r1 = mid
                    break
                else:
                    end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid + 1] != target:
                    r2 = mid
                    break
                else:
                    start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return r1, r2

print(Solution().searchRange([1,1], 1))