from typing import List

from collections import defaultdict


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        in_degree = [0] * n
        for a, b in roads:
            in_degree[a] += 1
            in_degree[b] += 1
            g[a].append(b)
            g[b].append(a)
        in_degree = list(enumerate(in_degree))
        in_degree.sort(key=lambda item: item[1])
        cost = [0] * n
        for index, (vertex, _) in enumerate(in_degree):
            cost[vertex] = index + 1
        visited = set()
        result = 0

        def dfs(node):
            nonlocal result
            if node not in visited:
                visited.add(node)
                for adj in g[node]:
                    result += cost[node] + cost[adj]
                    dfs(adj)

        for index in range(n):
            if index not in visited:
                dfs(index)
        return result // 2


print(Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]))
