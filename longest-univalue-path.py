from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def solve(root):
            if root:
                l, lf = solve(root.left)
                r, rf = solve(root.right)
                f = 0
                if l == root.val:
                    f += (lf + 1)
                if r == root.right:
                    f += (rf + 1)
                nonlocal mx
                mx = max(mx, f)
                return root.val, f
            return float('inf'), 0

        solve(root)
        return mx
