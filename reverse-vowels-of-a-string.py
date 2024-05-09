class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        i = 0
        while i < len(s) and s[i] not in vowels:
            i += 1

        j = len(s) - 1
        while j >= 0 and s[j] not in vowels:
            j -= 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            while i < len(s) and s[i] not in vowels:
                i += 1
            while j >= 0 and s[j] not in vowels:
                j -= 1

            
        return ''.join(s)
    

# print(Solution().reverseVowels("aA"))