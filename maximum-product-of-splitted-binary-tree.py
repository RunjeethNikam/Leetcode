# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    MOD = 10**9 + 7

    def sum_of_tree(self, root):
        if root:
            return self.sum_of_tree(root.left) + self.sum_of_tree(root.right) + root.val
        return 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mx = float("-inf")
        totol_sum = self.sum_of_tree(root)

        def solve(root):
            if root:
                left = solve(root.left)
                right = solve(root.right)
                nonlocal mx
                nonlocal totol_sum
                mx = max(mx, ((totol_sum - right) * right))
                mx = max(mx, ((totol_sum - left) * left))
                return root.val + left + right
            return 0

        solve(root)
        return mx%self.MOD
