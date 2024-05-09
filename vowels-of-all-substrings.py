class Solution:
    def countVowels(self, word: str) -> int:
        last = [-1, 0]  # index, count
        vowels = set(["a", "e", "i", "o", "u"])
        sm = 0
        l = 0
        if word[0] in vowels:
            sm = 1
            last = [0, 1]
            l = 1
        for index, value in enumerate(word):
            if index > 0:
                if value not in vowels:
                    sm += l
                else:
                    l = (index - last[0]) + (l + last[1])
                    sm += l
                    last = [index, last[1] + (index - last[0])]
        return sm
    
print(Solution().countVowels('aba'))
