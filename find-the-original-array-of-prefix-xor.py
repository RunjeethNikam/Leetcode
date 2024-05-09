from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        xor_till_now = 0
        for num in pref:
            current_element = xor_till_now ^ num
            result.append(current_element)
            xor_till_now ^= current_element
        return result
    
print(Solution().findArray([5,2,0,3,1]))
