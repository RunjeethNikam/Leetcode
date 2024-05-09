class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = c
        while low <= high:
            value = (low ** 2) + (high ** 2)
            if value == c:
                return True
            elif value > c:
                high = high - 1
            else:
                low = low + 1
        return False

print(Solution().judgeSquareSum(4))