class Solution:
    def solve(self, s):
        flag = False
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                if flag:
                    return False
                else:
                    if s[i + 1] == s[j]:
                        i += 1
                    elif s[i] == s[j - 1]:
                        j -= 1
                    else:
                        return False
                flag = True
            else:
                i += 1
                j -= 1
        return True

    def solve_1(self, s):
        flag = False
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                if flag:
                    return False
                else:
                    if s[i] == s[j - 1]:
                        j -= 1
                    elif s[i + 1] == s[j]:
                        i += 1
                    else:
                        return False
                flag = True
            else:
                i += 1
                j -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        return self.solve(s) or self.solve_1(s)
