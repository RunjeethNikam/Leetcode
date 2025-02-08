class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        last = word[0]
        result = []
        for ch in word[1:]:
            if ch != last:
                result.append(str(count))
                result.append(last)
                count = 1
                last = ch
            elif count == 9:
                result.append(str(count))
                result.append(last)
                count = 1
                last = ch
            else:
                count += 1
        result.append(str(count))
        result.append(last)
        return ''.join(result)

print(Solution().compressedString("abcde"))