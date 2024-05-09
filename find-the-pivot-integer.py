class Solution:
    def pivotInteger(self, n: int) -> int:
        sm = n * (n + 1) / 2
        left = 0
        for i in range(1, n + 1):
            right = sm - left
            left += i
            if left == right:
                return i
        return -1
    

print(Solution().pivotInteger(4))
