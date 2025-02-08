class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        flag = 1
        if x < 0:
            x = abs(x)
            flag = -1
        while x:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10
        return result * flag


print(Solution().reverse(x=-123))
