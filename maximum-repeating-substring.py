class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        dp = [0] * len(sequence)
        j = 0
        limit = len(word) - 1
        for i, ch in enumerate(sequence):
            if word[j] == ch:
                if j == limit:
                    dp[i] = 1 + dp[i - len(word)]
                j = (j + 1) % len(word)
            else:
                j = 0
        return max(dp)
print(Solution().maxRepeating("ababc", "ac"))
