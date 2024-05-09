class Solution:
    def squared(self, given):
        result = 0
        while given > 0:
            result += (given%10) ** 2
            given = given // 10
        return result


    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))
        while slow != fast and fast != 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        if fast == 1:
            return True
        else:
            return False
        
print(Solution().isHappy(1))
print(Solution().isHappy(2))
print(Solution().isHappy(3))
print(Solution().isHappy(4))
print(Solution().isHappy(5))
print(Solution().isHappy(6))
