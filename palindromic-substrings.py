from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome = defaultdict(lambda: True)
        count = 0
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j] and palindrome[(i+1, j-1)]:
                    count += 1
                if s[i] == s[j]:
                    palindrome[(i,j)] = palindrome[(i+1, j-1)]
                else:
                    palindrome[(i,j)] = False
        return count


print(Solution().countSubstrings("fdsklf"))
