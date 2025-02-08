from typing import List
from collections import defaultdict
from heapq import *


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        g = defaultdict(list)
        visited = set()
        for s, d, cost in flights:
            g[s].append((d, cost))

        h = [(0, 0, src)]  # cost, steps, node

        while h:
            cost, steps, node = heappop(h)
            # visited.add(node)
            if node == dst:
                return cost
            if steps > k:
                continue
            for adj_node, path_cost in g[node]:
                # if adj_node not in visited:
                heappush(h, (cost + path_cost, steps + 1, adj_node))
        return -1


print(
    Solution().findCheapestPrice(
        n=11,
        flights=[
            [0, 3, 3],
            [3, 4, 3],
            [4, 1, 3],
            [0, 5, 1],
            [5, 1, 100],
            [0, 6, 2],
            [6, 1, 100],
            [0, 7, 1],
            [7, 8, 1],
            [8, 9, 1],
            [9, 1, 1],
            [1, 10, 1],
            [10, 2, 1],
            [1, 2, 100],
        ],
        src=0,
        dst=2,
        k=4,
    )
)
