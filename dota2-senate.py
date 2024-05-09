from collections import deque


class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for index, value in enumerate(senate):
            if value == "R":
                r.append(index)
            else:
                d.append(index)
        index += 1

        

        while len(r) and len(d):
            if r[0] < d[0]:
                r.append(index)
            else:
                d.append(index)
            r.popleft()
            d.popleft()
            index += 1
        
        if len(r):
            return "Radiant"
        else:
            return "Dire"
        
print(Solution().predictPartyVictory("RDD"))