from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        nodes = 0
        index = {}
        for u, v in equations:
            if u not in index:
                index[u] = nodes
                nodes += 1
            if v not in index:
                index[v] = nodes
                nodes += 1
        g = [[float("inf") for _ in range(nodes)] for _ in range(nodes)]
        for [u, v], d in zip(equations, values):
            i = index[u]
            j = index[v]
            g[i][i] = 1
            g[j][j] = 1
            g[i][j] = float(d)
            g[j][i] = float(1 / d)
        print(g)
        print(index)
        for i in range(nodes):
            for j in range(nodes):
                for k in range(nodes): 
                    g[i][j] = min(g[i][j], g[i][k] * g[k][j])
        print(g)
        result = []
        for u, v in queries:
            if u in index and v in index:
                value = g[index[u]][index[v]]
                if value != float('inf'):
                    result.append(g[index[u]][index[v]])
                else:
                    result.append(-1)
            else:
                result.append(-1.0)

        return result


Solution().calcEquation(
    [["a","c"],["b","e"],["c","d"],["e","d"]],
    [2.0,3.0,0.5,5.0],
    [["a","b"]]
)
