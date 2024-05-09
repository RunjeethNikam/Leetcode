class Solution:
    def minimumCost(self, s: str) -> int:
        dp1 = [0] * len(s)
        dp2 = [0] * len(s)
        for index, value in enumerate(s):
            if index > 0:
                if value == s[index - 1]:
                    dp1[index] = dp1[index - 1]
                else:
                    dp1[index] = dp1[index - 1] + index

        # s = list(reversed(s))

        for index in range(len(s) - 2, -1, -1):
            value = s[index]
            if value == s[index + 1]:
                dp2[index] = dp2[index + 1]
            else:
                dp2[index] = dp2[index + 1] + len(s) - index - 1

        # dp2.reverse()
        mx = float("inf")

        for d1, d2 in zip(dp1, dp2):
            mx = min(mx, d1 + d2)

        return mx


print(Solution().minimumCost("0011"))
