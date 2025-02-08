from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = defaultdict(int)
        # f[s[0]] += 1
        low = 0
        result = 0
        for high in range(0, len(s)):
            f[s[high]] += 1
            count = high - low + 1
            while low <= high and count - max(f.values()) > k:
                if f[s[low]] == 1:
                    del f[s[low]]
                else:
                    f[s[low]] -= 1
                low += 1
                count = high - low + 1
            result = max(result, count)
        return result


print(Solution().characterReplacement(s="AABABBA", k=1))
