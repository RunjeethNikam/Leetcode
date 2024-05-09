from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        i = 0
        while k > 0 and i < len(happiness):
            if happiness[i] == 0:
                break
            result += max(happiness[i] - i, 0)
            i += 1
            k -= 1
        return result


print(Solution().maximumHappinessSum( happiness = [2,3,4,5], k = 1))
