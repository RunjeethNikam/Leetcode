from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = float('-inf')
        
        def solve(root):
            if root:
                nonlocal mx
                left = 0
                if root.left:
                    left = solve(root.left) + 1
                right = 0
                if root.right:
                    right = solve(root.right) + 1
                
                mx = max(mx, left + right)
                return max(left, right)
            return 0
            
        solve(root)