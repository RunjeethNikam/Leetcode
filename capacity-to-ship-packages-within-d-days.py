from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(capacity):
            current_weight = 0
            count = 0
            for w in weights:
                if w > capacity:
                    return False
                if (current_weight + w) > capacity:
                    count += 1
                    current_weight = w
                else:
                    current_weight += w
            count += 1
            return count <= days
        
        low =1
        high = sum(weights)
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

print(Solution().shipWithinDays([1,2,3,1,1], 4))