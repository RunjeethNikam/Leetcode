from typing import List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        q = deque([None])
        q.extend([key for key, value in g.items() if len(value) == 1])
        while q:
            l = q.popleft()
            if l is not None:
                p = g[l].pop()
                del g[l]
                n -= 1
                g[p].remove(l)
                if len(g[p]) == 1:
                    q.append(p)
            else:
                if n > 2:
                    q.append(None)
                else:
                    return list(q)


print(Solution().findMinHeightTrees(2, [[1,0]]))
