from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = defaultdict(list)

        def dfs(root, p):
            if p:
                g[root.val].append(p.val)
            if root.left:
                g[root.val].append(root.left.val)
                dfs(root.left, root)
            if root.right:
                g[root.val].append(root.right.val)
                dfs(root.right, root)

        dfs(root, None)
        q = deque([(target, 0)])
        result = []
        visited = set()
        while q:
            node, dist = q.popleft()
            visited.add(node)
            if dist == k:
                result.append(node)
            else:
                for adj in g[node]:
                    if adj not in visited:
                        q.append((adj, dist + 1))
        return result


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(Solution().distanceK(root, 5, 2))