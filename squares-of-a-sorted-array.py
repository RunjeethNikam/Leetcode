from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[-1] <= 0:
            nums.reverse()
            nums = list(map(lambda _: abs(_) * abs(_), nums))
            return nums
        elif nums[0] >= 0:
            nums = list(map(lambda _: abs(_) * abs(_), nums))
            return nums
        else:
            i = 0
            while nums[i] < 0:
                i += 1
            j = i-1
            result = []
            while i < len(nums) or j >= 0:
                left = (nums[i] * nums[i]) if i < len(nums) else float('inf')
                right = (nums[j] * nums[j]) if j >= 0 else float('inf')
                if left < right:
                    result.append(left)
                    i += 1
                else:
                    result.append(right)
                    j -= 1
            return result
    

print(Solution().sortedSquares([-7,-3,2,3,11]))

