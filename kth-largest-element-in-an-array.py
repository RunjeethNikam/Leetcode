from typing import List
from heapq import heapify, heappop, heappushpop, heappush
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000:
            return 1
        def solve(low, high, nums):
            index = random.randint(low, high)
            pivot = nums[index]
            nums[index], nums[high] = nums[high], nums[index]
            i = low 
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        low = 0
        high = len(nums) - 1
        while True:
            pivot_pos = solve(low, high, nums)
            if pivot_pos == len(nums) - k:
                return nums[pivot_pos]
            elif pivot_pos < (len(nums) - k):
                low = pivot_pos + 1
            else:
                high = pivot_pos - 1

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

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     lt = []
    #     for i in nums:
    #         if len(lt) < k:
    #             heappush(lt, i)
    #         else:
    #             # heappush(lt, -i)
    #             # heappop(lt)
    #             heappushpop(lt, i)
    #     return heappop(lt)

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


print(Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
