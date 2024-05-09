from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        low = 0
        high = len(people) - 1
        while low <= high:
            if people[low] + people[high] > limit:
                high -= 1
                count += 1
            else:
                low += 1
                high -= 1
                count += 1

        return count
    
print(Solution().numRescueBoats([1,2,2,1], 3))