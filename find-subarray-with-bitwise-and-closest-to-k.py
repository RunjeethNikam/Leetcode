from typing import List
from collections import defaultdict


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        def add(index):
            for i in range(32):
                msk = 1 << i
                if msk & nums[index]:
                    c[i] += 1

        def get():
            xor = 0
            for i in range(32):
                if c[i] > 0:
                    xor += 1 << i
            return xor

        def next_():
            xor = get()
            for i in range(32):
                msk = 1 << i
                if msk & nums[start] and c[i] == 1:
                    xor -= msk
            return abs(k - xor), xor

        def remove(index):
            for i in range(32):
                msk = 1 << i
                if msk & nums[index]:
                    c[i] -= 1

        c = defaultdict(int)
        add(nums[0])
        start = 0
        mn = abs(k - nums[0])
        for i in range(1, len(nums)):
            add(nums[i])
            xor = get()
            mn = min(mn, abs(k - xor))
            dist = abs(k - xor)
            next_dist, next_xor = next_()
            while start <= i and dist > next_dist:
                dist = next_dist
                mn = min(abs(k - next_xor))
                remove(start)
                start += 1
