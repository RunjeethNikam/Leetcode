from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_freq = defaultdict(int)
        t_counter = Counter(t)
        low = 0
        c = 0
        result = float("inf")
        result_str = ""
        for index, char in enumerate(s):
            if char in t_counter:
                window_freq[char] += 1
                c += 1
                while low <= index and s[low] not in t_counter:
                    low += 1
                while window_freq[char] > t_counter[char]:
                    window_freq[s[low]] -= 1
                    c -= 1
                    low += 1
                    while low <= index and s[low] not in t_counter:
                        low += 1
                if c == len(t) and (index - low + 1) < result:
                    result = index - low + 1
                    result_str = s[low : index + 1]
        return result_str


print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_freq = defaultdict(int)
        t_freq = defaultdict(int)
        result = 999999999
        result_str = ""
        left = None
        count = 0

        for _ in t:
            t_freq[_] += 1

        for index, value in enumerate(s):
            if value in t_freq:
                if left is None:
                    left = index
                window_freq[value] += 1
                if window_freq[value] <= t_freq[value]:
                    count += 1
                while window_freq[s[left]] > t_freq[s[left]]:
                    window_freq[s[left]] -= 1
                    left += 1
                    while left < len(s) and s[left] not in t_freq:
                        left += 1
                if count == len(t) and index-left + 1 < result:
                    result = index-left+1
                    result_str = s[left: index+1]

        return result_str
