from typing import List

class Solution:

    def number_of_elements(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            expected = (total // 2) + 1
            start = 0
            end = len(nums1) - 1
            found = False
            while start <= end:
                mid = (start + end) // 2
                count = self.number_of_elements(nums2, nums1[mid])
                if count + mid + 1 == expected:
                    return nums1[mid]
                elif count + mid + 1 < expected:
                    start = mid + 1
                else:
                    end = mid - 1 

            start = 0
            end = len(nums2) - 1
            while start <= end:
                mid = (start + end) // 2
                count = self.number_of_elements(nums1, nums2[mid])
                if count + mid + 1 == expected:
                    found = True
                    return nums2[mid]
                elif count + mid + 1 < expected:
                    start = mid + 1
                else:
                    end = mid - 1 
        else:
            expecteds = [(total // 2), (total // 2) + 1]
            result = 0
            for expected in expecteds:
                start = 0
                end = len(nums1) - 1
                found = False
                while start <= end:
                    mid = (start + end) // 2
                    count = self.number_of_elements(nums2, nums1[mid])
                    if count + mid + 1 == expected:
                        result += nums1[mid]
                        found = True
                        break
                    elif count + mid + 1 < expected:
                        start = mid + 1
                    else:
                        end = mid - 1 

                if not found:
                    start = 0
                    end = len(nums2) - 1
                    while start <= end:
                        mid = (start + end) // 2
                        count = self.number_of_elements(nums1, nums2[mid])
                        if count + mid + 1 == expected:
                            found = True
                            result += nums2[mid]
                            break
                        elif count + mid + 1 < expected:
                            start = mid + 1
                        else:
                            end = mid - 1 
            return result / 2

print(Solution().findMedianSortedArrays([2,2,4,4], [2,2,4,4]))