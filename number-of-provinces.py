from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        p = 0
        visited = set()
        nodes = len(isConnected)

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for adj_node, connected in enumerate(isConnected[node]):
                    if connected and adj_node not in visited:
                        dfs(adj_node)

        for node in range(nodes):
            if node not in visited:
                p += 1
                dfs(node)
        return p


print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
