class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def solve(s):
            j = 0
            i = 1
            while i < len(s):
                if s[i] == s[j]:
                    j += 1
                else:
                    j = 0
                i += 1
            if j >= len(s)//2:
                return s[j:i]
            else:
                return ""
            
        
            
        s1 = solve(str1)
        s2 = solve(str2)
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
    
print(Solution().gcdOfStrings("BBBBBB", "BBB"))