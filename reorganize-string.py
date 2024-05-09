from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        f = Counter(s)
        h = []
        for key, value in f.items():
            heapq.heappush(h, (-value, key))
        
        result = []
        while len(h):
            used_ch = []
            a = []
            while len(used_ch) < 2 and len(h):
                value, key = heapq.heappop(h)
                value = -value
                used_ch.append(key)
                if value > 1:
                    a.append((key, value-1))
            
            for key, value in a:
                heapq.heappush(h, (-value, key))

            if len(used_ch) < 2 and len(h):
                return ""
            else:
                result.extend(used_ch)

        return "".join(result)
            

print(Solution().reorganizeString("aaab"))