from heapq import *


class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        ft = [True] * len(s)
        for index, ch in enumerate(s):
            if ch != "*":
                heappush(h, (ord(ch), -index))
            else:
                ft[index] = False
                _, i = heappop(h)
                ft[-i] = False
        result = [ch for flag, ch in zip(ft, s) if flag]
        return "".join(result)


print(Solution().clearStars("abc"))
