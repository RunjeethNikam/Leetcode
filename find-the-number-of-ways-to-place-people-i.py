from typing import List


class Solution:

    def checkRectangle(self, ca, cb, ta, tb) -> bool:
        return ca <= ta and cb >= tb

    def checkCondition(self, ca, cb, ta, tb, ma, mb) -> bool:
        return ca <= ma and cb >= mb and ma <= ta and mb >= tb

    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        for ci, [ca, cb] in enumerate(points):
            for ti, [ta, tb] in enumerate(points):
                if ci != ti:
                    if self.checkRectangle(ca, cb, ta, tb):
                        for mi, [ma, mb] in enumerate(points):
                            if mi != ci and mi != ti:
                                if not self.checkCondition(ca, cb, ta, tb, ma, mb):
                                    continue
                                else:
                                    break
                        else:
                            count += 1
        return count

print(Solution().numberOfPairs([[1,1],[2,2],[3,3]]))
