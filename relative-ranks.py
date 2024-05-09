from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [None] * len(score)
        score = list(map(lambda item: (item[1], item[0]), enumerate(score)))
        score.sort(reverse=True)
        ranks = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        count = 1
        for _, index in score:
            result[index] = ranks.get(count, str(count))
            count += 1
        return result


print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))
