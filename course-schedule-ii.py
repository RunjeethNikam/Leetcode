from typing import List
from collections import defaultdict


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
                if sk[ng]:
                    return True
                if visited[ng] or self.cycle(ng, visited, sk):
                    return True
            sk[i] = False
        return False


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            indegree[a] += 1
            g[b].append(a)
        lt = []
        for index, degree in enumerate(indegree):
            if degree == 0:
                lt.append(index)
        
        processed_nodes = 0
        result = []
        while lt:
            node = lt.pop()
            result.append(node)
            processed_nodes += 1
            for adj_node in g[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    lt.append(adj_node)
        if processed_nodes != numCourses:
            return []
        return result

        

    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     g = Graph(numCourses)
    #     indegree = [0] * numCourses
    #     for a, b in prerequisites:
    #         indegree[b]+= 1
    #         g.addNode(a, b)
    #     visited = [False for _ in range(g.number_of_nodes)]
    #     sk = [False for _ in range(g.number_of_nodes)]
    #     for i in range(numCourses):
    #         if not visited[i] and indegree[i] == 0:
    #             if g.cycle(i, visited, sk):
    #                 return []
    #     return g.top_sort()


print(Solution().findOrder(2, [[1, 0]]))
