from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def solve(root: Optional[TreeNode]):
            nonlocal result
            if root:
                left = solve(root.left)
                right = solve(root.right)
                result = max(
                    result,
                    root.val,
                    root.val + left,
                    root.val + right,
                    root.val + left + right,
                )
                return max(
                    root.val,
                    root.val + left,
                    root.val + right
                )
            return float("-inf")

        solve(root)
        return result


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(Solution().maxPathSum(root))
