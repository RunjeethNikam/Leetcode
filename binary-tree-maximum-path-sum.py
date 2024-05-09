from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = float('-inf')
        def solve(node):
            global mx
            if node:
                left = solve(node.left)
                right = solve(node.right)
                mx = max(node.val, node.val + left, node.val + right, node.val + left + right)
                curr_mx = max(node.val, node.val + left, node.val + right, node.val + left + right)
                return curr_mx
            return 0
            
        solve(root)
        return mx