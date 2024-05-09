from typing import List
import heapq


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # h = []
        # result = 0
        sm = sum(milestones)
        mx = max(milestones)
        # for milestone in milestones:
        #     heapq.heappush(h, -milestone)
        
        if mx >= (sm-mx):
            return 2 * (sm-mx) + 1
        else:
            return sm

        # while len(h):

        #     if h[0] >= (sm-h[0]):
        #         return 2 * (sm-h[0]) + 1


        #     a = []
        #     count = 0
        #     while count < 2 and len(h):
        #         count += 1
        #         milestone = -heapq.heappop(h)
        #         if milestone > 1:
        #             a.append(milestone - 1)

        #     for milestone in a:
        #         heapq.heappush(h, -milestone)

        #     result += count
        #     sm -= count
        #     if count < 2:
        #         break
        # return result
    


print(Solution().numberOfWeeks([5]))

