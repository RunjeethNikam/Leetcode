# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode, sum: int = 0) -> TreeNode:
        def solve(r, sum: int):
            if r:
                sm = solve(r.right)
                r.val += sm + sum
                return solve(r.left, r.val)

        solve(root, 0)
        return root
