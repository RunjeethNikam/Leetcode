class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        fq = set(nums)
        result = -1
        for num in nums:
            if (num-1) not in fq:
                count = 0
                while num in fq:
                    count += 1
                    num += 1
                result = max(result, count)
        return result

print(Solution().longestConsecutive([-1, 0, 1, 2, 3, 4]))        