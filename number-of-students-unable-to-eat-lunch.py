from typing import List
from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sd = Counter(students)
        i = 0
        while i < len(sandwiches):
            if sd[sandwiches[i]] > 0:
                sd[sandwiches[i]] -= 1
            else:
                break
            i += 1
        return sd[0] + sd[1]
    
print(Solution().countStudents([1,1,0,0], [0,1,0,1]))
