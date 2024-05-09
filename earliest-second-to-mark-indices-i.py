from typing import List



class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:

        def isValid(limit):
            dp = {}
            for index, num in enumerate(nums):
                dp[index+1] = -1
            for index, value in enumerate(changeIndices):
                dp[value] = index+1
            
            lasts = list(dp.items())
            lasts.sort(key= lambda _: _[1])
            i = 0
            for index, value in enumerate(nums[:limit+1]):
                pass


        low = 1
        high = len(changeIndices)
        isValid(high)
        # result = None
        # while low <= high:
        #     mid = (low + high) // 2
        #     if isValid(mid):
        #         result = mid
        #         high = mid - 1
        #     else:
        #         low = mid + 1
            
        # return result
    
print(Solution().earliestSecondToMarkIndices([3,1,2,1], [1,1,4,1,2,3,2,3,3,2,4,2]))