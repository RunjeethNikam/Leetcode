from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def helper(self, r, s):
        if r and s:
            if r.val == s.val:
                return self.helper(r.left, s.left) and self.helper(r.right, s.right)
            else:
                return False
        if r is None and s is None:
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.helper(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) and self.isSubtree(
                root.right, subRoot
            )
