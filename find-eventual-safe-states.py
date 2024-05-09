from typing import List
from collections import defaultdict



class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False] * len(graph)
        cycles = [False] * len(graph)
        cycle = set()
        result = []

        def solve(root):
            cycle_element = False
            cycle.add(root)
            for adj_node in graph[root]:
                if not visited[adj_node]:
                    visited[adj_node] = True
                    cycle_element = cycle_element or solve(adj_node)
                elif adj_node in cycle:
                    cycle_element = True
                else:
                    cycle_element = cycle_element or cycles[adj_node]
            if not cycle_element:
                result.append(root)
            cycles[root] = cycle_element
            cycle.remove(root)
            return cycle_element

        for node in range(len(graph)):
            if not visited[node]:
                solve(node)
        
        result.sort()
        return result


print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))