from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        result = 0
        curr = 0
        last = None
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                curr = 1
                last = None
            elif last is not None:
                if last != (arr[i-1] < arr[i]):
                    curr += 1
                else:
                    curr = 2
                last = arr[i-1] < arr[i]
            else:
                curr = 2
                last = arr[i-1] < arr[i]
            if curr > result:
                result = curr
        return result


print(Solution().maxTurbulenceSize([4]))
