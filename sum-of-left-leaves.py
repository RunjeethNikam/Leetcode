from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sm = 0
        def solve(r, d):
            if r:
                solve(r.left, True)
                solve(r.right, False)
                if (not r.left) and (not r.right) and d:
                    sm += r.val

        solve(root)
        return sm
