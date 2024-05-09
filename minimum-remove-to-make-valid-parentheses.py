class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        pair = 0
        for index in range(len(s)):
            ch = s[index]
            if ch == '(':
                pair += 1
            elif ch == ')':
                pair -= 1
            if pair == -1:
                s[index] = ""
                pair = 0

        pair = 0
        for index in range(len(s)-1, -1, -1):
            ch = s[index]
            if ch == '(':
                pair -= 1
            elif ch == ')':
                pair += 1
            if pair == -1:
                s[index] = ""
                pair = 0
        return ''.join(s)

    

print(Solution().minRemoveToMakeValid("))(("))