from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        lt = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        while len(lt) and k > 0:
            _, i, j = heappop(lt)
            k -= 1
            result.append((nums1[i],nums2[j]))
            if j+1 < len(nums2) and (i,j+1) not in visited:
                visited.add((i, j+1))
                heappush(lt, (nums1[i] + nums2[j+1], i, j+1))
            if i+1 < len(nums1) and (i+1,j) not in visited:
                visited.add((i+1, j))
                heappush(lt, (nums1[i+1] + nums2[j], i+1, j))
        return result

print(Solution().kSmallestPairs([1,7,11], [2,4,6], 3))
                                                                                                                                                                                 