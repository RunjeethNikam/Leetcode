from bisect import *


# class Solution:
#     def inversionCount(self, arr, n):
#         def solve(arr):
#             n = len(arr)
#             if n > 1:
#                 mid = n // 2
#                 left, l_count = solve(arr[:mid])
#                 right, r_count = solve(arr[mid:])

#                 count = 0
#                 for num in left:
#                     position = bisect_left(right, num)
#                     count += position

#                 temp = []
#                 i = 0
#                 j = 0
#                 while i < len(left) and j < len(right):
#                     if left[i] < right[j]:
#                         temp.append(left[i])
#                         i += 1
#                     else:
#                         temp.append(right[j])
#                         j += 1
#                 if i != len(left):
#                     temp.extend(left[i:])
#                 if j != len(right):
#                     temp.extend(right[j:])

#                 return temp, l_count + r_count + count
#             return arr, 0

#         return solve(arr)[1]


class Solution:
    def inversionCount(self, arr, n):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, inv_count_left = merge_sort(arr[:mid])
            right, inv_count_right = merge_sort(arr[mid:])

            merged_arr, inv_count_merge = merge(left, right)

            return merged_arr, inv_count_left + inv_count_right + inv_count_merge

        def merge(left, right):
            merged = []
            inv_count = 0
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    # inv_count += j
                    inv_count += len(left) - i  # Counting inversions
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        sorted_arr, inversions = merge_sort(arr)
        return inversions

print(Solution().inversionCount([2, 4, 1, 3, 5], 5))



# print(Solution().inversionCount([2, 4, 1, 3, 5], 5))


[5]
[3,4,5,6]
