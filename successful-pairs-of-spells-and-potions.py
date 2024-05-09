from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def search(spell):
            low = 0
            high = len(potions)-1
            while low <= high:
                mid = (high + low) // 2
                if (potions[mid] * spell) < success:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        potions.sort()
        result = []
        for spell in spells:
            left = search(spell)
            if left < len(potions):
                result.append(len(potions) - left)
            else:
                result.append(0)
        return result
    

print(Solution().successfulPairs([3,1,2], [8,5,8], 16))