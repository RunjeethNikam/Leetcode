class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        start = 0
        end = 0
        while start < len(nums) and end < len(nums):
            if end + 1 < len(nums) and nums[end+1] == nums[end] + 1:
                end += 1
            else:
                if nums[start] == nums[end]:
                    result.append(str(nums[start]))
                else:
                    result.append(f'{nums[start]}->{nums[end]}')
                start = end + 1
                end = end + 1
        print(result)
print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
# print(Solution().summaryRanges([0,1,2,4,5,7]))
# print(Solution().summaryRanges([0,1,2,4,5,7]))