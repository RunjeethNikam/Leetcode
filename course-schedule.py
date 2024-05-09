class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for i in prerequisites:
            graph[i[1]].append(i[0])

        in_degree = [0 for _ in range(numCourses)]
        for node in graph:
            for ng in node:
                in_degree[ng] += 1

        q = list()
        for index, indegree in enumerate(in_degree):
            if indegree == 0:
                q.append(index)
        
        nodes_visited = 0

        while len(q) != 0:
            index = q.pop()
            for ng in graph[index]:
                in_degree[ng] -= 1
                if in_degree[ng] == 0:
                    q.append(ng)
                    nodes_visited += 1

        return nodes_visited == numCourses

