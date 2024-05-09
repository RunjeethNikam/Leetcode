from typing import List
import math


class Solution:

    def get_item(self, nums, i):
        if i < 0:
            return 0
        try:
            return nums[i]
        except IndexError:
            return 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n <= 0:
                return True
            if self.get_item(flowerbed[i] == 0 and () self.get_item(flowerbed, i-1) == 0 and self.get_item(flowerbed, i+1) == 0:
                flowerbed[i] = 1
                n -= 1
        if n <= 0:
            return True
        return False
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     flag = False
    #     count = 0
    #     result = 0
    #     for i in flowerbed:
    #         if i == 1:
    #             if not flag:
    #                 flag = True
    #                 result += count//2
    #             else:
    #                 result += (count-1)//2
    #             count = 0
    #         else:
    #             count += 1
    #         if n <= result:
    #             return True
    #     if not flag:
    #         result += math.ceil(count/2)
    #     else:
    #         # seen 1
    #         result += count//2
        
    #     if n <= result:
    #             return True
    #     return False

print(Solution().canPlaceFlowers([0,0,0, 1], 1))
