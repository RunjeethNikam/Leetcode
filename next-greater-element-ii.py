from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        count = 0
        result = [-1] * len(nums)
        st = []
        i = 0
        for i in range(2* len(nums)):
            i = i % len(nums)
            value = nums[i]
            while st and nums[st[-1]] < value:
                if result[st[-1]] == -1:
                    count += 1
                    result[st[-1]] = value
                st.pop()
            st.append(i)

        return result
print(Solution().nextGreaterElements([1,1,1]))
