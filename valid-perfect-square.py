
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            sq = mid * mid
            if sq < num:
                low = mid + 1
            elif num < sq:
                high = mid - 1
            if sq == num:
                return True
        return False
    
print(Solution().isPerfectSquare(14))