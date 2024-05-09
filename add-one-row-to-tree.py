from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        def solve(root: TreeNode, curr_depth: int, direction: bool):
            if root:
                if depth == curr_depth:
                    r = TreeNode(val)
                    if direction:
                        r.right = solve(root, curr_depth + 1, direction)
                    else:
                        r.left = solve(root, curr_depth + 1, direction)
                    return r
                else:
                    root.left = solve(root.left, curr_depth + 1, False)
                    root.right = solve(root.right, curr_depth + 1, True)
                    return root
            elif curr_depth == depth:
                return TreeNode(val)

        return solve(root, 1, False)
