from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = False
        if len(arr) < 3 or arr[1] < arr[0]: 
            return False
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1

        if i == len(arr):
            return False

        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1

        return i == len(arr)
    
print(Solution().validMountainArray([9,8,7,6,5,4,3,2,1,0]))