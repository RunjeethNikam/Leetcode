class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        result = 0
        while x:
            result = (result * 10) + (x % 10)
            x //= 10
        return temp == result


print(Solution().isPalindrome(10))