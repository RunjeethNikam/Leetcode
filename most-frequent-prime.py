from typing import List
from collections import defaultdict


class Solution:

    def __init__(self) -> None:
        self.primes = self.SieveOfEratosthenes(1000000)

    def SieveOfEratosthenes(self, n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return prime

    def process_single(self, i, j, dp, mat, primes):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),

            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        def check(i, j, m):
            return i >= 0 and j >= 0 and i < len(m) and j < len(m[0])

        for d in directions:
            ti, tj = i, j
            result = 0
            while check(ti, tj, mat):
                result = (result * 10) + mat[ti][tj]
                if result > 10 and primes[result]:
                    dp[result] += 1 
                ti += d[0]
                tj += d[1]

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        dp = defaultdict(int)
        for i in                                              range(len(mat)):
            for j in range(len(mat[0])):
                self.process_single(i, j, dp, mat, self.primes)
        mx = -1
        result = -1
        for key, value in dp.items():
            if value > mx:
                mx = max(value, mx)
                result = key
            elif value == mx:
                result = max(result, key)
        return result
                


print(Solution().mostFrequentPrime([[6,7]]))
