from typing import List


class Solution:

    def longestMountain(self, arr: List[int]) -> int:
        direction = None
        left = None
        result = 0
        for index in range(1, len(arr)):
            if arr[index] > arr[index - 1]:
                if direction is None:
                    direction = True
                    left = index - 1
                elif not direction:
                    direction = True
                    left = index - 1

            elif arr[index] < arr[index - 1]:
                if direction is not None:
                    if direction == True:
                        direction = False
                    result = max(result, index - left + 1)
            else:
                direction = None
        return result

print(Solution().longestMountain([0,2,0,2,1,2,3,4,4,1]))
