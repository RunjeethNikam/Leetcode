from typing import List


class Solution:
    # def check(self, temp, pattern, start):
    #     i = 0
    #     while i < len(pattern) and start < len(temp):
    #         if temp[start] == pattern[i]:
    #             start += 1
    #             i += 1
    #         else:
    #             return False
    #     if i == len(pattern):
    #         return True
    #     else:
    #         return False

    def pre_process(pattern, lps):
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i-1]
        return lps



    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        temp = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                temp.append(0)
            elif nums[i] > nums[i-1]:
                temp.append(1)
            else:
                temp.append(-1)
        count = 0
        lps = self.pre_process(pattern, [0] * len(pattern))
        j = 0
        i = 0
        while i < len(temp) and j < len(pattern):
            if temp[i] == pattern[j]:
                i += 1
                j += 1

            if j == len(pattern):
                count += 1
                j = lps[j-1]
            
            if temp[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            
        return count