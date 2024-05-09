import itertools
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solve(h: TreeNode):
            if h:
                yield from solve(h.left)
                if h.left is None and h.right is None:
                    yield h.val
                yield from solve(h.right)

        g1 = solve(root1)
        g2 = solve(root2)

        for a, b in itertools.zip_longest(g1, g2, fillvalue=None):
            if a == b:
                continue
            else:
                return False
        return True


t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(3), TreeNode(2))

print(Solution().leafSimilar(t1, t2))