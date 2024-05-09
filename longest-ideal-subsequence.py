from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = defaultdict(int)  # count
        index_of_alpha = dict(zip(ascii_lowercase, range(26)))
        for ch in s:
            mn = 1
            for last in dp.keys():
                if abs(index_of_alpha[ch] - index_of_alpha[last]) <= k:
                    if mn < dp[last] + 1:
                        mn = dp[last] + 1
            dp[ch] = mn
        return max(dp.values(), key=lambda item: item[-1])[-1]


# class Solution:
#     def longestIdealString(self, s: str, k: int) -> int:
#         lenghts = [0] * 26
#         a = ord("a")
#         for c in s:
#             o = ord(c) - a
#             lenghts[o] = max(
#                 lenghts[max(0, o - k) : min(26, o + k + 1)]
#             ) + 1
#         return max(lenghts)


print(Solution().longestIdealString("abcd", 3))
