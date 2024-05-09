from typing import List



class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        count = 0
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
                count += 1
            else:
                if count > 1:
                    i += 1
                    for ch in str(count):
                        chars[i] = ch
                        i += 1
                else:
                    i += 1
                chars[i] = chars[j]
                j += 1
                count = 1
        if count > 1:
            i += 1
            for ch in str(count):
                chars[i] = ch
                i += 1
        else:
            i += 1
        return i


ch = ["a","a","a","b","b","a","a"]
ln = Solution().compress(ch)
print(ln, ch[:ln])
        