from typing import List
from collections import defaultdict



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        f = defaultdict(-1)
        for num in nums2:
            if not st or num < st[-1]:
                st.append(num)
            else:
                while st and num > st[-1]:
                    f[st[-1]] = num
                    st.pop()
                st.append(num)
        result = []
        for num in nums1:
            result.append(f[num])
        return result
        
