class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        mx = count
        i += 1
        while i < len(s):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            mx = max(mx, count)
            i += 1
        return mx

print(Solution().maxVowels('ramadan', 2))