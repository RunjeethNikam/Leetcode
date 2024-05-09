from collections import defaultdict


class Solution:

    def wonderfulSubstrings(self, word: str) -> int:
        dp = defaultdict(int)
        msk = 0
        count = 0
        for ch in word:
            index = ord('ch') - ord('a')
            msk ^= 1 << index
            count += dp[msk]
            for i in range(10):
                pre_mask = msk ^ (1 << i)
                count += dp[pre_mask]
            dp[msk] += 1
        return count

    # def wonderfulSubstrings(self, word: str) -> int:
    #     dp = defaultdict(int)
    #     dp[0] = 1
    #     mask = 0
    #     count = 0

    #     for ch in word:
    #         index = ord(ch) - ord('a')
    #         mask ^= 1<<index
    #         count += dp[mask]
    #         for i in range(10):
    #             pre_mask = mask ^ (1<<i)
    #             count += dp[pre_mask]
    #         dp[mask] += 1
    #     return count


print(Solution().wonderfulSubstrings("aa"))
