from typing import List

class Graph:
    def __init__(self, n) -> None:
        self.number_of_nodes = n
        self.g = [[] for _ in range(n)]

    def addNode(self, u, v):
        self.g[u].append(v)
    
    def top_sort(self):
        visited = [False for _ in range(self.number_of_nodes)]
        result = []
        for i in range(self.number_of_nodes):
            if not visited[i]:
                self.dfs(result, i, visited)
        return result

    def dfs(self, result, i, visited):
        if not visited[i]:
            visited[i] = True
            for ng in self.g[i]:
                self.dfs(result, ng, visited)
            result.append(i)
    
    def cycle(self, i, visited, sk):
        if not visited[i]:
            visited[i] = True
            sk[i] = True
            for ng in self.g[i]:
                if not visited[ng] or self.cycle(ng, visited, sk):
                    return True
                if sk[ng]:
                    return True
            sk[i] = False
        return False

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = Graph(numCourses)
        for u, v in prerequisites:
            g.addNode(u, v)
        if g.cycle(0, [False for _ in range(g.number_of_nodes)], [False for _ in range(g.number_of_nodes)]):
            return []
        return g.top_sort()
    
print(Solution().findOrder(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))