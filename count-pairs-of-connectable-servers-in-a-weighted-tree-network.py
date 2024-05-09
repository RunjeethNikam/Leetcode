from typing import List
from collections import defaultdict


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        g = defaultdict(list)
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])

        def dfs(node, w, visited):
            count = 0
            if w % signalSpeed:
                count += 1
            
            for adj_node, adj_w in g[node]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    count += dfs(adj_node, w + adj_w, visited)

            return count
        
        result = []

        for node_to_be_processed in sorted(g.keys()):
            if len(g[node_to_be_processed]) > 1:
                nodes = []
                for adj_node, w in g[node_to_be_processed]:
                    visited = set([adj_node, node_to_be_processed])
                    nodes.append(dfs(adj_node, w, visited))
                S = sum(nodes)
                temp = 0
                for node in nodes:
                    S -= node
                    temp += (node * S)
                result.append(temp)
        return result 
    

print(Solution().countPairsOfConnectableServers([[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], 1))