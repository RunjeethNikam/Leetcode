from collections import defaultdict
from heapq import *


class Solution:
    def dijkstra(self, V, adj, S):
        g = defaultdict(list)
        for index, edge in enumerate(adj):
            g[index].append(edge)
            g[edge[0]].append((index, edge[1]))
        pq = []
        src = 0
        heappush(pq, (0, src))
        d = [float('inf')] * len(V)
        d[src] = 0
        while pq:
            dist, u = heappop(pq)
            for v, weight in g[u]:
                if d[v] > (d[u] + weight):
                    d[v] = d[u] + weight
                    heappush(pq, (d[v], v))
        print(d)





