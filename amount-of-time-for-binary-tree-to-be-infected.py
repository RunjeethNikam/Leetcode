from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = dict()

        def dfs(root, p):
            if root:
                nonlocal parent
                dfs(root.left, root)
                parent[root.val] = (root, p)
                dfs(root.right, root)

        dfs(root, None)
        visited = set([start])
        q = deque()
        q.append((parent[start][0], 0))
        result = float("-inf")
        while q:
            node, step = q.popleft()
            p = parent.get(node.val, (None, None))[1]
            for n in [p, node.left, node.right]:
                if n and (n.val not in visited):
                    visited.add(n.val)
                    q.append((n, step + 1))
                    result = max(result, step + 1)
        return result
