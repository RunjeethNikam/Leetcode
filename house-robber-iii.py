from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root.left is None and  root.right is None:
                return [root.val, root.val] # with, without
            
            l = (0, 0)
            if root.left:
                l = solve(root.left)
            
            r = (0, 0)
            if root.right:
                r = solve(root.right)

            return [root.val + l[0]+ r[0], max(l) + max(r)]
            
        return min(solve(root))