class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda item: (item[0], item[1]))
        result = []
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            else:
                if result[-1][-1] > interval[-1]:
                   continue
                elif result[-1][-1] >= interval[0]:
                    result[-1][-1] = interval[-1]
                else:
                    result.append(interval)
        print(result)



Solution().merge([[2,6], [1,3],[8,10],[15,18]])