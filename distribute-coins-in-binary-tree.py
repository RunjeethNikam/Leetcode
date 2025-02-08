from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        result = 0
        def solve(root):
            if not root:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            extra = root.val - 1 + left + right
            result += abs(extra)
            return extra
        solve(root)
        return result
