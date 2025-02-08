from typing import List
from collections import Counter
from math import sqrt


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def find_factors(n):
            factors = set()
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    factors.add(i)
                    factors.add(n // i)

            # Return the sorted list of factors
            return factors

        ln = len(nums2)
        nums2 = map(lambda item: item * k, nums2)
        nums2 = Counter(nums2)
        result = 0
        for num in nums1:
            # if num == 1:
            #     result += ln
            # else:
            factors = find_factors(num)
                # factors.remove(1)
            result += sum([nums2[f] for f in factors if f in nums2])
        return result


print(Solution().numberOfPairs(nums1=[2,8,17,6], nums2=[3,1,1,8], k=2))
