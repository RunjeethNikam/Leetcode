from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def solve(r: TreeNode, left: int, right: int):
            nonlocal result
            result = max(result, left, right)

            if r.left:
                solve(r.left,  right + 1, 0)
            if r.right:
                solve(r.right, 0, left + 1)
        solve(root, 0, 0)

        return result


t = TreeNode(
    1,
    None,
    TreeNode(
        1,
        TreeNode(1),
        TreeNode(
            1,
            TreeNode(
                1,
                None,
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        1,
                        None,
                        TreeNode(
                            1,
                        ),
                    ),
                ),
            ),
            TreeNode(
                1,
            ),
        ),
    ),
)
