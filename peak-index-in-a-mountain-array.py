from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1


print(Solution().peakIndexInMountainArray(arr=[18, 29, 38, 59, 98, 100, 99, 98, 90]))
