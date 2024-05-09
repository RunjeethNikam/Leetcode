from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens)-1
        score = 0
        result = 0
        while i <= j:
            if power >= tokens[i]:
                score += 1
                result = max(score, result)
                power -= tokens[i]
                i += 1
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return result
        



print(Solution().bagOfTokensScore([26], 51))
