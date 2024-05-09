from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        dp = {}
        def solve(l, r, nums, score):
            if (l, r, score) in dp:
                return dp[(l,r,score)]
            if l < r:
                c1 = 0
                c2 = 0
                c3 = 0
                flag = 0
                if (nums[l] + nums[l+1]) == score:
                    flag = 1
                    c1 = solve(l+2, r, nums, score)
                
                if (nums[r] + nums[r-1]) == score:
                    flag = 1
                    c2 = solve(l, r-2, nums, score)

                if (nums[l] + nums[r]) == score:
                    flag = 1
                    c3 = solve(l+1, r-1, nums, score)
                
                dp[(l,r,score)] = flag + max(c1, c2, c3)
                return dp[(l,r,score)]
            else:
                return 0

            
        return 1 + max(
            solve(1, len(nums) - 2, nums, nums[0] + nums[-1]),
            solve(2, len(nums) - 1, nums, nums[0] + nums[1]),
            solve(0, len(nums) - 3, nums, nums[-1] + nums[-2]),
        )

print(Solution().maxOperations([3,2,1,2,3,4]))