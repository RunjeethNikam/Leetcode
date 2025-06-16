from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        low = 0
        count = 0
        result = 0
        for index, ch in enumerate(s):
            freq[ch] += 1
            if freq[ch] > 1:
                count += 1
            while count > 0 and low <= index:
                freq[s[low]] -= 1
                if freq[s[low]] == 1:
                    count -= 1
                low += 1
            result = max(result, index - low + 1)
        return result


print(Solution().lengthOfLongestSubstring("abcabcbb"))
