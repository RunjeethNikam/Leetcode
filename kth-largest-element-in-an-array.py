from typing import List
from heapq import heapify, heappop, heappushpop, heappush
import random


class Solution:

    # def partition(self, nums, left, right):
    #     i = left
    #     pivot = random.randrange(left, right)
    #     nums[pivot], nums[right] = nums[right], nums[pivot]
    #     x = nums[right]
    #     for j in range(left, right):
    #         if nums[j] <= x:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #     nums[i], nums[right] = nums[right], nums[i]
    #     return nums, i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        lt = []
        for i in nums:
            if len(lt) < k:
                heappush(lt, i)
            else:
                # heappush(lt, -i)
                # heappop(lt)
                heappushpop(lt, i)
        return heappop(lt)

        # k = k-1
        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     # pivot = random.randrange(l, r)
        #     nums, position = self.partition(nums, l, r)
        #     if (position) == k:
        #         return nums[position]
        #     elif position > k:
        #         r = position - 1
        #     else:
        #         l = position + 1
        # return nums[l]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
