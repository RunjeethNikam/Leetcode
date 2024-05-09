# class Solution:
#     def mySqrt(self, x: int) -> int:
#         low = 1
#         high = x
#         while low <= high:
#             mid = (low + high) // 2
#             if mid ** 2 == x:
#                 return mid
#             elif mid ** 2 < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return high
#         # i = 0
#         # j = 0
#         # while i**2 <= x:
#         #     while (i + (j+1) ** 2) <= x:
#         #         j += 1
#         #     if j == 0:
#         #         return i
#         #     else:
#         #         i = i + j ** 2
#         #         j = 0
#         # return i
            

# print(Solution().mySqrt(4))

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        i = 5
        while i <= n:
            result += n//i
            i *= 5
        return result
    
print(Solution().trailingZeroes(10))