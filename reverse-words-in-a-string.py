class Solution:

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        result = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] != ' ':
                j += 1
            else:
                if i != j:
                    self.reverse(s, i , j-1)
                    while i < j:
                        result.append(s[i])
                        i += 1
                    result.append(' ')
                j += 1
                i = j
        self.reverse(s, i , j-1)
        while i < j:
            result.append(s[i])
            i += 1
        result.reverse()
        return "".join(result)

print(Solution().reverseWords("a good   example"))