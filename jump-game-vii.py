class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [0] * len(s)
        count = 0
        for index, step in enumerate(s):
            count += dp[index]
            if (step == "0" and count > 0) or index == 0:
                if index + minJump < len(s):
                    dp[index + minJump] += 1
                if index + maxJump + 1 < len(s):
                    dp[index + maxJump + 1] -= 1
        return s[-1] == "0" if count > 0 else False


print(Solution().canReach("0000000000", 8, 8))
