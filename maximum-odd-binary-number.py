class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse=True)
        s.pop(0)
        s += ['1']
        return ''.join(s)
        

print(Solution().maximumOddBinaryNumber('0101'))
        