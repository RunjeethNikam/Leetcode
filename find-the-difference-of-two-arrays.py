from typing import List



class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(filter(lambda x: x not in s2, s1)), list(filter(lambda x: x not in s1, s2))]