from typing import List


class Solution:

    def sieve(self, n):
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for num in range(2, int(n**0.5) + 1):
            if sieve[num]:
                primes.append(num)
                for multiple in range(num * num, n + 1, num):
                    sieve[multiple] = False
                    
        return sieve

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = self.sieve(101)
        left = right = -1
        for index, value in enumerate(nums):
            if primes[value]:
                if left == -1:
                    left = index
                else:
                    right = index


        if right != -1:
            abs(right - left)
        else:
            return 0
    


print(Solution().maximumPrimeDifference([4,8,2,8]))
