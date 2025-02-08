from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(dist):
            number_of_balls_placed = 0
            last = float("-inf")
            i = 0
            while i < len(position) and number_of_balls_placed < m:
                p = position[i]
                if (p - last) >= dist:
                    number_of_balls_placed += 1
                    last = p
                else:
                    pass
                i += 1
            return number_of_balls_placed >= m

        position.sort()
        low = 1
        high = position[-1] + position[0]
        mid = None
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result


print(Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))
