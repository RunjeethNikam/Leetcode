from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right):
            if left == right:
                return nums[left], 0
            else:
                # case
                v1 = nums[left]
                mx, mn = solve(left + 1, right)

                v2 = nums[right]
                mx_, mn_ = solve(left, right - 1)
                if (v1 + mn) > (v2 + mn_):
                    return v1 + mn, mx
                else:
                    return v2 + mn_, mx_

        mx, mn = solve(0, len(nums) - 1)
        if mx >= (sum(nums) - mx):
            return True
        else:
            return False

print(Solution().predictTheWinner([1,5,233,7]))
