from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # def solve(
    #     self, node: Optional["Node"], new_nodes: dict = {}
    # ) -> Optional["Node"]:
    #     if not node:
    #         return None
    #     if node.val in new_nodes:
    #         return new_nodes[node.val]
    #     else:
    #         new_node = Node(node.val)
    #         new_nodes[new_node.val] = new_node
    #         for ng in node.neighbors:
    #             if ng.val in new_nodes:
    #                 new_node.neighbors.append(new_nodes[ng.val])
    #             else:
    #                 new_node.neighbors.append(self.solve(ng, new_nodes))
    #         return new_node
    # def cloneGraph(
    #     self, node: Optional["Node"]
    # ) -> Optional["Node"]:
    #     return self.solve(node, {})

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        clone = {node.val: Node(node.val)}
        q = deque(node)
        while len(q):
            n =  q.popleft()
            c_node = clone[n.val]
            for ng in n.neighbors:
                if ng.val not in clone:
                    clone[ng.val] = Node(ng.val)
                q.append(ng)
                c_node.neighbors.append(clone[ng.val])
        return clone[node.val]


a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

Solution().cloneGraph(a)
