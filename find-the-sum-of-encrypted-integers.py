from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sm = 0

        def solve(num):
            mx = float('-inf')
            count = 0
            while num:
                mx = max(mx, num%10)
                count += 1
                num = num//10
            result = 0
            for _ in range(count):
                result = (result * 10) + mx
            return result

        for num in nums:
            sm += solve(num)


        return sm
    

print(Solution().sumOfEncryptedInt([0]))