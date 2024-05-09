from collections import defaultdict
from typing import List

class Solution:

    def solv(self, g, source, destination, visited):
        if not visited[source]:
            visited[source] = True
            if source == destination:
                return True
            for ng in g[source]:
                if self.solv(g, ng, destination, visited):
                    return True
        return False


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict([])
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False for _ in len(g.keys())]

        return self.solv(g, source, destination, visited)