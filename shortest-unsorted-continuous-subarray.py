from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def right_traverse(nums):
            st = []
            right = -1
            for index, value in enumerate(nums):
                if not st:
                    st.append(value)
                    continue
                else:
                    while st and st[-1] <= value:
                        st.pop()
                    if st:
                        right = max(index, right)
                    else:
                        st.append(value)

            return right

        def left_traverse(nums):
            st = []
            left = len(nums)
            for index in range(len(nums) - 1, -1, -1):
                value = nums[index]
                if not st:
                    st.append(value)
                    continue
                else:
                    while st and st[-1] >= value:
                        st.pop()
                    if st:
                        left = min(index, left)
                    else:
                        st.append(value)

            return left

        right = right_traverse(nums)
        left = left_traverse(nums)
        if right == -1 and left == len(nums):
            return 0
        return right - left + 1


print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))
