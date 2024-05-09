class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count  = 0
        end = None
        for point in points:
            if end is None:
                count += 1
                end = point[1]
            else:
                if end < point[0]:
                    end = point[1]
                    count += 1
                elif end == point[0]:
                    pass
                elif end > point[0]:
                    end = min(point[1], end)
        return count
print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
                    
